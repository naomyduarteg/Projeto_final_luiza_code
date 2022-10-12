from fastapi import Request, HTTPException, status
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import Request
from typing import List

from src.models.carts import Cart
from src.models.carts_item import CartsItem
from src.models.carts_item_new import CartsItemNew

def get_collection_carts(request: Request):
  return request.app.database["carts"]
              
def get_all_carts(request: Request, limit: int):
  return list(get_collection_carts(request).find(limit=limit))

def get_cart_by_user_id(request: Request, user_id: str):
  return request.app.database["carts"].find_one({"user_id": user_id})

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
            cart_item["price"] = item["price"]
            is_update = True
           
    if (is_update == False):      
        item_list.append(item)
           
    return item_list

def calculateTotalAmount(itemList: List[CartsItem]):
    total_amount = 0
   
    for item in itemList:        
        total_amount += item["quantity"]
    return total_amount
  
def get_cart(request: Request,user_id: str):
               
    if (cart := get_cart_by_user_id(request, user_id)) is not None:
        return cart
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cart with user id {user_id} not found")
  
def create_cart(request: Request, cartsItemNew: CartsItemNew):
    user_id = cartsItemNew["user_id"]
    product_id = cartsItemNew["product_id"]
    quantity = cartsItemNew["quantity"]
    category = cartsItemNew["category"]
    
    product = request.app.database["items"].find_one({"_id": product_id})    
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
   
    user = request.app.database["users"].find_one({"_id": user_id})    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
   
    if category == "Buy":
        price = product["price_buy"]
    elif category == "Rent":
        price = product["price_rent"]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Option not found")
    
    cart = get_collection_carts(request).find_one({"user_id": user_id})
    cart_item = CartsItem(product_id=product_id, quantity=quantity, price=price)

    if cart is None:  
        if category == "Buy":
            total = product["price_buy"] * quantity 
        elif category == "Rent":
            total = product["price_rent"] * quantity
        
        list_products = [cart_item]        
        cart = Cart(user_id= user_id, products= list_products, total_price= total, quantity_products = quantity)
        cart = jsonable_encoder(cart)
        new_item = get_collection_carts(request).insert_one(cart)
        created_cart = get_collection_carts(request).find_one(
            {"_id": new_item.inserted_id}
        )
        return created_cart
   
    products = cart["products"]
    addProductItem(products,cart_item)   
    total = calculateTotalPrice(products)
    total_amount = calculateTotalAmount(products)    
    
    filter = {"_id": cart["_id"]}
    get_collection_carts(request).update_one(filter, {"$set": {"products": jsonable_encoder(products)}})       
    get_collection_carts(request).update_one(filter, {"$set": {"total_price": round(total,2)}})
    get_collection_carts(request).update_one(filter, {"$set": {"quantity_products": total_amount}})
    
        
    cart["products"] = products
    cart["total_price"] = round(total,2)       
    cart["quantity_products"] = total_amount
    
    return cart
  
def delete_product(request: Request, user_id: str, product_id: str):
  cart = get_collection_carts(request).find_one({"user_id": user_id})
      
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
      delete_cart(request, user_id)
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cart with no products. Cart deleted!")                
       
  
  filter = {"_id": cart["_id"]}
  get_collection_carts(request).update_one(filter, {"$set": {"products": jsonable_encoder(list_products)}})
  get_collection_carts(request).update_one(filter, {"$set": {"total_price": cart["total_price"]}})
  get_collection_carts(request).update_one(filter, {"$set": {"quantity_products": cart["quantity_products"]}})
  
  cart["products"] = list_products
  return cart

def delete_cart(request: Request, user_id: str):
    cart = get_collection_carts(request).find_one({"user_id": user_id})
        
    if cart is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cart with user id {user_id} not found")
    
    get_collection_carts(request).delete_one({"user_id": user_id})
    return "Cart successfully deleted!"