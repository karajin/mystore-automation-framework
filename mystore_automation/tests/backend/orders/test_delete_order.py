import pytest
import logging as logger
import random
from src.dao.products_dao import ProductsDAO
from src.dao.orders_dao import OrdersDAO
from src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from src.generichelpers.generic_order_helpers import GenericOrderHelpers

@pytest.fixture(scope='module')
def init():
    product_dao = ProductsDAO()
    order_helper = OrdersAPIHelper()
    generic_order_helper = GenericOrderHelpers()
    order_dao = OrdersDAO()
    return {
        'product_dao':product_dao,
        'order_helper':order_helper,
        'generic_order_helper':generic_order_helper,
        'order_dao' : order_dao
    }
@pytest.mark.orders
@pytest.mark.ecombe60
@pytest.mark.tcid218
def test_deleting_an_order(init):
    """
        Test case to verify the functionality of deleting an order.
    """
    product_dao = init['product_dao']
    order_helper = init['order_helper']
    generic_order_helper = init['generic_order_helper']
    order_dao = init['order_dao']
    product = product_dao.get_random_product_from_db(qty=1)
    
    product_id = product[0]['ID']
    info =  {"line_items": [
    {
      "product_id": product_id,
      "quantity": 1
    }
  ]}
    
    order = generic_order_helper.create_order(additional_args=info)
    rs_api = order_helper.delete_order_by_id(order_id = order['id'])

    assert order['id'] == rs_api['id']
   

@pytest.mark.orders
@pytest.mark.ecombe61
@pytest.mark.tcid219
def test_delete_an_order_with_invalid_id(init):
    order_id = random.randint(1000, 2000)
    order_helper = init['order_helper']
    rs_api = order_helper.delete_order_by_id(order_id = order_id, expected_status_code=404)

    assert rs_api == {'code': 'woocommerce_rest_shop_order_invalid_id',
    'data': {'status': 404},
    'message': 'Invalid ID.'}