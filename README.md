![luluflix](https://user-images.githubusercontent.com/73078250/195168917-cd8de02a-777c-4d0b-82f8-2d42a8b0d27a.png)

<h1 align='center'> Projeto final Luiza &lt;code&gt;: carrinho de compra <br> Grupo 13: filmes e séries </h1>

![luluflix-api](https://user-images.githubusercontent.com/73078250/195190270-a51615cc-37dd-4021-850e-ab44499aad35.svg)
![versão-1 0](https://user-images.githubusercontent.com/73078250/195189793-cc7802c8-3c9a-4222-939d-7154fb6fc4bf.svg)
[![forthebadge](https://forthebadge.com/images/badges/it-works-why.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


## Membros da equipe
:star2: <a href="https://www.linkedin.com/in/amandapq/"> Amanda Pacheco</a>

:star2: <a href="https://www.linkedin.com/in/naomyduarteg/"> Naomy Duarte Gomes</a>

:star2: <a href="https://www.linkedin.com/in/tamaradscosta/">Tamara Santos Costa</a>


## Objetivos

Este é o projeto final do bootcamp de aceleração em Python promovido pelo Luiza labs, que sumariza tudo o que foi aprendido durante as semanas por meio da criação de um carrinho de compras. Nosso grupo recebeu como objetos de venda filmes e séries e nomeamos nossa aplicação ![luluflix (1)](https://user-images.githubusercontent.com/73078250/195190456-941ad59c-ca69-4e47-89d6-f7060299cba7.svg).

Utilizamos Python como linguagem de programação, o framework FastAPI e a base de dados não-relacional MongoDB. 
Para a criação do carrinho, as informações que utilizamos no projeto foram: clientes, produtos e o próprio carrinho. Os clientes podem cadastrar mais de um endereço e podem alugar ou comprar filmes e séries em formato digital (nenhum produto físico é utilizado). 
A estrutura do projeto é a seguinte:

<pre>
<code>
├── Projeto_final_luiza_code
│   │── env.example
│   ├── src
│   │    ├── __init__.py
│   │    ├── business_objects
│   │    │      ├── cart_bo.py
│   │    │      ├── product_bo.py
│   │    │      └── user_bo.py
│   │    │
│   │    ├── endpoints
│   │    │      ├── __init__.py
│   │    │      ├── carts.py
│   │    │      ├── products.py
│   │    │      └── users.py
│   │    │
│   │    ├── models
│   │    │      ├── carts.py
│   │    │      ├── carts_item.py
│   │    │      ├── products.py
│   │    │      └── users.py
│   │    │
│   │    └── routes
│   │           └── api.py
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
    └── README.md
 </code>
</pre>

## Detalhes da estrutura

### Models
Nesta pasta, definimos a estrutura dos objetos utilizados.
- Clientes: id, nome completo, email único e válido, senha.
- Endereço dos clientes: apelido do endereço, email do cliente (que associa o endereço a ele), logradouro, número, cidade, estado e CEP.
- Itens (filmes e séries): id, tipo, nome, descrição, preço de aluguel, preço de compra, gênero, ano, duração, linguagens, legendas.
- Itens do carrinho: id, quantidade, preço.
- Carrinho: id, id do usuário ao qual o carrinho pertence, produtos, preço total, quantidade de produtos.

### Business objects
Nesta pasta, definimos as regras pelas quais clientes, endereços, itens e carrinhos serão solicitados pela API de acordo com os requerimentos do projeto. Além disso, como características próprias deste projeto, temos:
- Clientes não são removidos.
- Endereços são removidos.
- Os produtos possuem a opção de alugar ou comprar.
- Como não são produtos físicos, não fazemos balanço de estoque.
- Os produtos podem ser removidos do banco de dados de produtos, porém não são removidos do carrinho. 


### Endpoints
Nesta pasta, definimos os canais de comunicação da API.

## Swagger
Para testar a API de forma interativa, podemos utilizar o Swagger, que é uma documentação automática. A API ![luluflix (1)](https://user-images.githubusercontent.com/73078250/195190456-941ad59c-ca69-4e47-89d6-f7060299cba7.svg) possui a seguinte documentação:

![image](https://user-images.githubusercontent.com/73078250/195345570-bb539dd8-9136-458a-8240-3703f21511be.png)

## Banco de dados
Utilizando o MongoDB Compass, podemos visualizar o banco de dados deste projeto, que possui as seguintes coleções:
![mongodb](https://user-images.githubusercontent.com/73078250/195186801-d12a0243-c25d-4c97-adde-09fe30ea2198.png)

## Execução da API ![luluflix (1)](https://user-images.githubusercontent.com/73078250/195190456-941ad59c-ca69-4e47-89d6-f7060299cba7.svg)
A API pode ser executada seguindo os passos abaixo:
1. Clone o repositório

```
https://github.com/naomyduarteg/Projeto_final_luiza_code.git
```
2. Crie um ambiente virtual

```
python3 -m venv <name_of_venv>
```
3. Vá até a pasta onde foi criada seu ambiente virtual e ative-o

No Windows:
```
Scripts/activate
```
No Linux/Mac:
```
bin/activate
```
4. Insale os módulos requeridos

```
pip install -r requirements.txt
```

6. Rode a API utilizando o uvicorn

```
uvicorn main:app --reload
```

7. Leia o QR Code abaixo para acessar a documentação
<img src="https://user-images.githubusercontent.com/73078250/195349991-6953b178-b36b-4b23-9b9d-a202285d1e78.png" width="400" height="420" />
