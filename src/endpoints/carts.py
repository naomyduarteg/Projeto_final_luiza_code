from fastapi import APIRouter, Request, HTTPException, status
from typing import List
from fastapi.encoders import jsonable_encoder
from src.models.carts import Cart
from src.models.carts_item import CartsItem

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/",response_description="Get all carts", response_model=List[Cart])
def return_cart(request: Request):
    
    return list(request.app.database["carts"].find(limit=100))

@router.get("/{user_id}/",response_description="Get a cart by user id",response_model=Cart)
def return_cart(user_id: str,request: Request):
               
    if (cart := request.app.database["carts"].find_one({"user_id": user_id})) is not None:
        return cart
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cart with user id {user_id} not found")

@router.post("/{user_id}/{product_id}/{product_qtt}/{buy_or_rent}", response_description="Create a cart", status_code=status.HTTP_201_CREATED)
def create_cart(user_id: str, product_id: str, product_qtt: int, buy_or_rent: str, request: Request):
    product = request.app.database["items"].find_one({"_id": product_id})    
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
   
    user = request.app.database["users"].find_one({"_id": user_id})    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
   
    if buy_or_rent == "Comprar":
        price = product["price_buy"]
    else:
        price = product["price_rent"]
    cart = request.app.database["carts"].find_one({"user_id": user_id})
    cart_item = CartsItem(product_id=product_id, quantity=product_qtt, price=price)
   
    
    if cart is None:    
        if buy_or_rent == "Comprar":    
            total = product["price_buy"] * product_qtt
        else:       
            total = product["price_rent"] * product_qtt
        list_products = [cart_item]     
        cart = Cart(user_id= user_id, products= list_products, total_price= total, quantity_products = product_qtt)
        cart = jsonable_encoder(cart)
        new_item = request.app.database["carts"].insert_one(cart)
        created_cart = request.app.database["carts"].find_one(
                     {"_id": new_item.inserted_id}
                    )
        return created_cart


   
    products = cart["products"]
    addProductItem(products,cart_item)   
    total = calculateTotalPrice(products)
    total_amount = calculateTotalAmount(products)    
    
    filter = {"_id": cart["_id"]}
    request.app.database["carts"].update_one(filter, {"$set": {"products": jsonable_encoder(products)}})       
    request.app.database["carts"].update_one(filter, {"$set": {"total_price": round(total,2)}})
    request.app.database["carts"].update_one(filter, {"$set": {"quantity_products": total_amount}})
        
    cart["products"] = products
    cart["total_price"] = round(total,2) 
    cart["quantity_products"] = total_amount
    
    return cart

def calculateTotalPrice(itemList: List[CartsItem]):
    total = 0
    
    for item in itemList:        
        total += item["quantity"] * item["price"]        
    return total
 
def addProductItem(item_list: List[CartsItem], item: CartsItem):        
    is_update = False
   
    for cart_item in item_list:
        if (cart_item["product_id"] == item["product_id"]):
            cart_item["quantity"] = item["quantity"]
            is_update = True
           
    if (is_update == False):      
        item_list.append(item)
           
    return item_list

def calculateTotalAmount(itemList: List[CartsItem]):
    total_amount = 0
   
    for item in itemList:        
        total_amount += item["quantity"]
    return total_amount

@router.delete("/{user_id}/{product_id}", response_description="Delete an item from cart", status_code=status.HTTP_200_OK)
def delete_product(user_id: str, product_id: str,request: Request):
    cart = request.app.database["carts"].find_one({"user_id": user_id})
        
    if cart is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cart with user id {user_id} not found")
    
    list_products = cart["products"]
    product_found = False
    for product in list_products:
        if (product["product_id"] == product_id):                
            list_products.remove(product)
            product_found = True            
            cart["total_price"] = calculateTotalPrice(list_products)            
            cart["quantity_products"] = calculateTotalAmount(list_products)
            
    if(product_found == False):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
         
    if list_products == []:
        delete_cart(user_id,request)                
        return "Cart with no products. Successfully deleted!" 
    
    filter = {"_id": cart["_id"]}
    request.app.database["carts"].update_one(filter, {"$set": {"products": jsonable_encoder(list_products)}})
    request.app.database["carts"].update_one(filter, {"$set": {"total_price": cart["total_price"]}})
    request.app.database["carts"].update_one(filter, {"$set": {"quantity_products": cart["quantity_products"]}})
    
    cart["products"] = list_products
    return cart

@router.delete("/{user_id}/", response_description="Delete a cart", status_code=status.HTTP_200_OK)
def delete_cart(user_id: str, request: Request):
    cart = request.app.database["carts"].find_one({"user_id": user_id})
        
    if cart is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cart with user id {user_id} not found")
    
    request.app.database["carts"].delete_one({"user_id": user_id})
    return "Cart successfully deleted!"