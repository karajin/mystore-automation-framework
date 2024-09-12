import pytest

from src.generichelpers.generic_order_helpers import GenericOrderHelpers
from src.dao.coupons_dao import CouponsDAO
from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import logging
import random
import math
pytestmark = [pytest.mark.orders, pytest.mark.regression]

@pytest.fixture(scope='module')
def setup_teardown():
    coupon_code = '50OFF'
    discount_pct = '50.00'
    product_helper = ProductsAPIHelper()
    products = product_helper.call_list_products()
    random.shuffle(products)
    for product in products:
        if product['price']:
            break
    else:
        raise Exception('Unable to find product with price')
    
    info = {}
    info['generic_order_helper'] = GenericOrderHelpers()
    info['coupon_code'] = coupon_code
    info['discount_pct'] = discount_pct
    info['product_id'] = product['id']
    info['product_price'] = product['price']
    return info

@pytest.mark.tcid60
@pytest.mark.ecombe127
def test_apply_valid_coupon_to_order(setup_teardown):
    """
    Validates when x% coupon is applied to an order, the 'total' amount is reduced by x%
    """
    generic_order_helper= setup_teardown['generic_order_helper']
    info = {
        "line_items": [{"product_id": setup_teardown['product_id'], "quantity": 1}],
        "coupon_lines": [{"code": setup_teardown['coupon_code']}],
        "shipping_lines": [{"method_id": "flat_rate", "method_title": "Flat Rate", "total": "0.00"}]
        }
     
    order = generic_order_helper.create_order(additional_args=info)
    # calculate expected total price based on coupon and product price
    expected_total = float(setup_teardown['product_price']) * (float(setup_teardown['discount_pct'])/100)

    # get total from order response and verify
    total = math.ceil(float(order['total']))
    expected_total = math.ceil(expected_total)

    assert total == expected_total, f"Order total is not reduced after applying 50% coupon. Expected cost: {expected_total}, Actual: {total}"

@pytest.mark.tcid190
@pytest.mark.ecombe66
def test_create_order_with_expired_coupon():
    """
        Test case to verify that creating an order with an expired coupon fails.
    """
    coupon_dao = CouponsDAO()
    expired_coupon = coupon_dao.get_expired_coupon(qty=1)
    import pdb; pdb.set_trace()

    payload = {'coupon_lines':expired_coupon}

    generic_order_helper = GenericOrderHelpers()

    order = generic_order_helper.create_order(additional_args=payload, expected_status_code=400)




    


