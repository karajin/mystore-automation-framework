from src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from src.generichelpers.generic_order_helpers import GenericOrderHelpers
from src.utilities.genericUtilities import generate_random_string
import pytest
import random


@pytest.mark.ecombe101
def test_delete_order_note_with_vaid_note_id():
  generic_order_helper = GenericOrderHelpers()
  order_api_helper = OrdersAPIHelper()
  order = generic_order_helper.create_order()
  order_id = order['id']
  random_str = generate_random_string(length=10)
  info = {"note": random_str}
  order_note=order_api_helper.call_create_order_note(order_id=order_id, payload=info)
  note_id = order_note['id']
  deleted_order_note = order_api_helper.call_delete_order_note_by_id(order_id=order_id, note_id=note_id)
  assert deleted_order_note['id'] == note_id, f"order note not deleted"


@pytest.mark.ecombe102
def test_delete_order_note_with_invaid_note_id():
  generic_order_helper = GenericOrderHelpers()
  order_api_helper = OrdersAPIHelper()
  order = generic_order_helper.create_order()
  order_id = order['id']
  note_id = random.randint(1000, 2000)
  payload={'force':True}
  rs_api = order_api_helper.call_delete_order_note_by_id(payload=payload, order_id=order_id, note_id=note_id, expected_code=404)

  assert rs_api['code'] == "woocommerce_rest_invalid_id", f"Delete order note with invalid id , response has bad 'code'."
