from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import random
import string
from src.utilities.genericUtilities import generate_random_string

class GenericProductHelper(ProductsAPIHelper):

  def get_random_products(self, qty=1, **kwargs):
    payload = {"per_page": 100}
    product_list = self.call_list_products(payload=payload)
    return random.sample(product_list, int(qty))
  
  def get_product_detail_via_api(self, product_id):
        return self.call_get_product_py_id(product_id)
  
  def create_a_product(self, product_type="simple", **kwargs):
      payload = {}
      payload['type'] = product_type
      if 'name' not in kwargs.keys():
        payload['name'] = generate_random_string()

      if 'regular_price' not in kwargs.keys():
        price = round(random.uniform(10, 100), 2)
        payload['regular_price'] = str(price)

      payload.update(kwargs)

      rs_api = self.call_create_product(payload=payload)
      assert rs_api
      return rs_api
