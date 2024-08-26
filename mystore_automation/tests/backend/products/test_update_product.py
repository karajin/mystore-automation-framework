import pytest
from src.dao.products_dao import ProductsDAO
from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import random
import string

@pytest.mark.products
@pytest.mark.ecombe29
@pytest.mark.tcid230

def test_create_product():
  product_dao = ProductsDAO()
  product_helper = ProductsAPIHelper()

  random_product = product_dao.get_random_product_from_db()
  #import pdb; pdb.set_trace()
  product_id = random_product[0]['ID']
  product_name = ''.join(random.choices(string.ascii_letters, k=10))

  payload = {
    'name': product_name,
    'type': "simple",
    'price': '21.99'
  }

  rs_api = product_helper.call_update_product(product_id, payload)
  product_id = rs_api['id']

  assert product_name == rs_api['name']
  rs_db = product_dao.get_product_by_id(product_id)
  #import pdb; pdb.set_trace()
  assert rs_api['id'] == rs_db[0]['ID']
  

