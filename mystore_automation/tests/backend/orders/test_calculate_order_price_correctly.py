import random
import pytest
from src.generichelpers.generic_order_helpers import GenericOrderHelpers
from src.generichelpers.generic_product_helper import GenericProductHelper

pytestmark = [pytest.mark.orders, pytest.mark.regression]

@pytest.mark.tcid211
@pytest.mark.ecombe68
def test_verify_order_calculates_correct_price_item_not_on_sale():
  """
        Test case to verify that an order calculates the correct price when the item is not on sale.

    """
  generic_product_helper = GenericProductHelper()
  generic_order_helper = GenericOrderHelpers()
  product = generic_product_helper.create_a_product()
  assert product['on_sale'] == False
  product_id = product['id']
  regular_price = product['regular_price']
  payload = {
    'line_items':[
      {
        "product_id": product_id, 
        "quantity": 1
        }
      ]
  }

  order = generic_order_helper.create_order(additional_args=payload)
  price = order['total']
  assert float(price) == float(regular_price)

@pytest.mark.ecombe69
@pytest.mark.tcid212
def test_verify_order_calculates_correct_price_item_is_on_sale():
  generic_product_helper = GenericProductHelper()
  generic_order_helper = GenericOrderHelpers()
  regular_price = round(random.uniform(10, 100), 2)
  sale_price = round(regular_price * .75, 2)
  product = generic_product_helper.create_a_product(on_sale=True, regular_price=str(regular_price), sale_price=str(sale_price))
  info = {
    'line_items':
    [
      {
        "product_id": product['id'], 
        "quantity": 1
        }
      ]
  }
  order = generic_order_helper.create_order(additional_args=info)
  assert str(sale_price) == order['total']
  
  