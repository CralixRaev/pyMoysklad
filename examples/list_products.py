from pymoysklad.json.client import JSONApi
from pymoysklad.json.entity.product import Product

client = JSONApi(("admin@company", "examplePassword"))
# or by using token
# client = JSONApi("your_token_goes_here")

products = client.product.list_product()
print(products.rows[0])
print(products.meta)
client.product.create_product(Product(name="test"))
