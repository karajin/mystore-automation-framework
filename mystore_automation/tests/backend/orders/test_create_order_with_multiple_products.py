from src.dao.products_dao import ProductsDAO
from src.generichelpers.generic_order_helpers import GenericOrderHelpers
import pytest
import random

@pytest.mark.ecombe107
def test_create_order_with_multiple_product():
  product_dao = ProductsDAO()
  order_helper = GenericOrderHelpers()
  products = product_dao.get_random_product_from_db(qty=2)
  product1_id = products[0]['ID']
  product2_id = products[1]['ID']
  customer_id=0
  payload = {
    'line_items':[
      {'product_id':product1_id,
       'quantity':1},
      {'product_id':product2_id,
       'quantity':1}
    ],
    'customer_id':customer_id
  }

  rs_api = order_helper.create_order(additional_args=payload)
  assert rs_api
  line_items = rs_api['line_items']
  product_id_list = []
  for item in line_items:
    product_id_list.append(item['product_id'])

  assert product1_id in product_id_list and product2_id in product_id_list