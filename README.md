# pyMoysklad
Work-in-Progress api wrapper for [Moysklad JSON API 1.02](https://dev.moysklad.ru/doc/api/remap/1.2/)

# Usage
Create JSON API client:
```python
from pymoysklad.json.client import JSONApi

client = JSONApi(("admin@company", "examplePassword"))
# or by using token
# client = JSONApi("your_token_goes_here")
```
Access one of an API entities:
```python
products = client.product.list_product()
```
List method will return CollectionAnswer object, from that you can access rows or get an request meta\context
```python
print(products.rows)
print(products.meta)
print(products.context)
```
Get method will return object itself by his UUID
```python
product = client.product.get_product(UUID("10cb9bc1-1544-4245-bb79-fece6074544f"))
```
Delete method will delete object by his UUID
```python
client.product.delete_product(UUID("10cb9bc1-1544-4245-bb79-fece6074544f"))
```
Create method will create and return newly created object or multiple objects, if you provide a list of them
```python
from pymoysklad.json.entity.product import Product

product = client.product.create_product(Product(name="test"))
```
Edit method will edit and return edited object 
```python
edited_product = client.product.edit_product(UUID("10cb9bc1-1544-4245-bb79-fece6074544f"), Product(name="edited name", description="i can edit any field, by just providing it in this product object"))
```
Mass delete method will mass delete objects using theirs metas
```python
products_to_delete = client.product.list_product(search="DELETEME")
metas = [product.meta for product in products_to_delete.rows]
client.product.mass_delete_product(metas)
```
### [Sorting](https://dev.moysklad.ru/dc/api/remap/1.2/#mojsklad-json-api-obschie-swedeniq-sortirowka-ob-ektow)
To sort a collection just provide `order` keyword argument in `list` method.
Order argument can contain list of tuples (`order=[("name", "desc"), ("code", "asc")]`) to provide sorting direction or simply be a list of strings (`order=["name", "code"]` to use default ascending sorting:
```python
sorted_products = client.product.list_product(order=["price", ("name", "desc")])
```

### [Filtering](https://dev.moysklad.ru/doc/api/remap/1.2/#mojsklad-json-api-obschie-swedeniq-fil-traciq-wyborki-s-pomosch-u-parametra-filter)
To filter a collection provide `filter` keyword argument in `list` method.
Filter argument should be a tuple of strings with format described in [documentation](https://dev.moysklad.ru/doc/api/remap/1.2/#mojsklad-json-api-obschie-swedeniq-fil-traciq-wyborki-s-pomosch-u-parametra-filter) (`filter=('name!=Товар', 'price>=100')`)
```python
filtered_products = client.product.list_product(filter=('name!=Товар', 'price>=100'))
```

### [Searching](https://dev.moysklad.ru/doc/api/remap/1.2/#mojsklad-json-api-obschie-swedeniq-kontextnyj-poisk)
To search in a collection provide `search` keyword argument in `list` method.
Search argument should be a string.
```python
searched_products = client.products.list_product(search="Капибара")
```

### [Expanding](**https://dev.moysklad.ru/doc/api/remap/1.2/#mojsklad-json-api-obschie-swedeniq-zamena-ssylok-ob-ektami-s-pomosch-u-expand)
To expand some field in request use `expand` keyword argument in `list` method.
Expand argument should be a string, containing field name, multiple field names delimited with commas or nested fields delimited by dots. `demand.agent,organization`
```python
products_with_images = client.product.list_product(expand="images")
```

### Limit and offset
To limit and offset collection use `limit` and `offset` keyword arguments


# I encountered an problem\there isn't some entity like ...
Just create an issue and I will try to resolve it ASAP. Yup, even add some entity that i didn't added before
