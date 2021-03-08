from models.Product import Product
from models.Warehouse import Warehouse
import cherrypy

# product = Product()
# products = product.get_all_products(with_quantity=True)
# print(products)
# for elem in products:
#     print(elem)
# product.add_new_product(product_name='Hotpoint', price=29790, article='6262YAA')

# warehouse = Warehouse()
# warehouse.update_product_quantity(2, 15)


class Web(Product):

    @cherrypy.expose
    def index(self):
        return """
        <html>
           <head>
                <title>TestWeb</title>
           </head>
           <body>
              <form action="products" method="GET">
                 <input type="submit" name="submit" value="Посмотреть все товары"/>
              </form>
           </body>
        </html>
        """

    @cherrypy.expose
    def products(self, submit):
        product = Product()
        products = product.get_all_products(with_quantity=True)
        res = ''
        for elem in products:
            # res = res.join(f"<li>{i}</li>" for i in elem)+"<br>"
            res = res + "<li> ID: " + str(elem[0]) + "</li>"
            res = res + "<li> Product name: " + str(elem[1]) + "</li>"
            res = res + "<li> Price: " + str(elem[2]) + "</li>"
            res = res + "<li> Article: " + str(elem[3]) + "</li>"
            res = res + "<li> Quantity: " + str(elem[4]) + "</li> <br>"
        return f"""
            <html>
               <head>
                    <title>ProductsView</title>
               </head>
               <body>
                    <ul>
                        {res}
                    </ul>
               </body>
            </html>
        """


cherrypy.quickstart(Web())
