from src.generichelpers.generic_order_helpers import GenericOrderHelpers
from src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
import pytest

@pytest.mark.ecombe108
def test_update_order_shipping_address():
  generic_order_helpers = GenericOrderHelpers()
  order_helper = OrdersAPIHelper()
  order = generic_order_helpers.create_order()
  payload = { 'shipping': {
              'address_1': '123 Disney Road',
              'address_2': '',
              'city': 'Seattle',
              'company': '',
              'country': 'USA',
              'first_name': 'Kara',
              'last_name': 'Jin',
              'phone': '',
              'postcode': '98053',
              'state': 'WA'} }
  rs_api = order_helper.update_order(order_id=order['id'], payload=payload)
  
  assert rs_api['shipping'] == payload['shipping']