from src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from src.generichelpers.generic_order_helpers import GenericOrderHelpers
from src.utilities.genericUtilities import generate_random_string
import pytest
import random


@pytest.mark.ecombe99
def test_create_order_note_with_vaid_id():
  generic_order_helper = GenericOrderHelpers()
  order_api_helper = OrdersAPIHelper()
  order = generic_order_helper.create_order()
  order_id = order['id']
  random_str = generate_random_string(length=10)
  info = {"note": random_str}

  order_note=order_api_helper.call_create_order_note(order_id=order_id, payload=info)

  assert order_note['note'] == random_str


@pytest.mark.ecombe100
def test_create_order_note_with_invaid_id():
  generic_order_helper = GenericOrderHelpers()
  order_api_helper = OrdersAPIHelper()
  order = generic_order_helper.create_order()
  order_id = random.randint(1000, 2000)
  random_str = generate_random_string(length=10)
  info = {"note": random_str}

  order_note=order_api_helper.call_create_order_note(order_id=order_id, payload=info, expected_code=404)
  
  assert order_note['code'] == 'woocommerce_rest_order_invalid_id'
  assert order_note['data'] == {'status': 404}
  assert order_note['message'] == 'Invalid order ID.'
