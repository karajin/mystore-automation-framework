from src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from src.generichelpers.generic_order_helpers import GenericOrderHelpers
from src.utilities.genericUtilities import generate_random_string
from src.dao.products_dao import ProductsDAO
import pytest


@pytest.mark.ecombe105
def test_add_product_to_existing_order():
    """
        Test to verify the functionality of adding a product to an existing order.
    """ 
    order_helper = OrdersAPIHelper()
    product_dao = ProductsDAO()
    generic_order_helper = GenericOrderHelpers()
    order_json = generic_order_helper.create_order()
    order_id = order_json['id']
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']
    payload = {"line_items": [
                {
                  "product_id": product_id,
                  "quantity": 1
                }
              ]}
    rs_api = order_helper.update_order(order_id,payload)
    
    line_items = rs_api['line_items'] 
    product_ids = []

    for item in line_items:
        product_ids.append(item['product_id'])

    assert product_id in product_ids




