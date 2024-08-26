
import pytest
from src.dao.products_dao import ProductsDAO
from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import random
import string

@pytest.mark.tcid216
@pytest.mark.ecombe23

def test_create_product():
  product_dao = ProductsDAO()
  product_helper = ProductsAPIHelper()

  first_name = ''.join(random.choices(string.ascii_letters, k=5))
  last_name = ''.join(random.choices(string.ascii_letters, k=5))
  name = first_name+' '+last_name
  payload = {
    'name': name,
    'type': "simple",
    'price': '21.99'
  }
  rs_api = product_helper.call_create_product(payload)
  product_id = rs_api['id']
  assert name == rs_api['name']
  rs_db = product_dao.get_product_by_id(product_id)
  #import pdb; pdb.set_trace()
  assert rs_api['id'] == rs_db[0]['ID']
  assert rs_api['generated_slug'] == rs_db[0]['post_name']




