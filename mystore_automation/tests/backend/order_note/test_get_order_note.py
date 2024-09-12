from src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from src.generichelpers.generic_order_helpers import GenericOrderHelpers
from src.utilities.genericUtilities import generate_random_string
import pytest
import random


@pytest.mark.ecombe103
def test_list_all_order_notes():
  generic_order_helper = GenericOrderHelpers()
  order_api_helper = OrdersAPIHelper()
  order = generic_order_helper.create_order()
  order_id = order['id']
  order_notes = order_api_helper.call_list_all_order_notes(order_id=order_id )
  assert order_notes


@pytest.mark.ecombe104
def test_get_order_note_with_vaid_note_id():
  generic_order_helper = GenericOrderHelpers()
  order_api_helper = OrdersAPIHelper()
  order = generic_order_helper.create_order()
  order_id = order['id']
  random_str = generate_random_string(length=10)
  payload = {"note":random_str}
  order_note = order_api_helper.call_create_order_note(order_id, payload)
  note_id = order_note['id']
  note = order_api_helper.retrive_order_note_by_id(order_id, note_id)
  assert note['id'] == note_id


@pytest.mark.ecombe106
def test_get_order_note_with_invaid_note_id():
  generic_order_helper = GenericOrderHelpers()
  order_api_helper = OrdersAPIHelper()
  order = generic_order_helper.create_order()
  order_id = order['id']
  
  note_id = random.randint(1000, 2000)
  note = order_api_helper.retrive_order_note_by_id(order_id, note_id, expected_code=404)


  assert note['code'] == "woocommerce_rest_invalid_id", f"Delete order note with invalid id , response has bad 'code'."