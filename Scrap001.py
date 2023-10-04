from bs4 import BeautifulSoup
import requests

#Conectamos URL.
#Despues pedimos la respuesta con el response.
#Despues se activa bs4
#Despues con bs4 buscamos todos los productos,
#Despues dividimos en que podemos buscar.


i = 1

while i<=2:
    
    url = (f'https://www.hardgamers.com.ar/brands/amd?page={i}&limit=21&brand=amd')
    
    result = requests.get(url).text
    
    soup=BeautifulSoup(result, 'html.parser')
    
    lista_productos=soup.find_all('div', class_="product-description padding-top-20")
    
    for lista_producto in lista_productos:
        nombre_producto = lista_producto.find('h3', class_="product-title").text.strip().replace('- ACUARIO','')
        precio_producto = lista_producto.find('h2',attrs={'itemprop':'price'}).text.strip()
        print(f'{nombre_producto} sale: \n ${precio_producto}')
        
    i+=1


'''
El codigo por el momento lo que hace es.
1)Busca del html div inside.
2)Hace un bucle for para obtener todos los nombres y precios.
3)Hice un bucle while para que vaya aumentando de pagina y traiga todos los precios y nombres de las paginas a las que le indico.
4)Se podria seguir modularizando para obtener diferentes formas u objetos.
'''



    
    







                    


    
    



    









    
    
    



    
