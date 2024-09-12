from src.utilities.genericUtilities import generate_random_string
from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from src.dao.products_dao import ProductsDAO
import pytest


@pytest.mark.ecombe119
def test_create_variable_product():
    product_helper = ProductsAPIHelper()
    products_dao = ProductsDAO()
    # generate some data
    payload = {
    "name": generate_random_string(20),
    "type": "variable",
    'regular_price': "10.99",
    "attributes": [
        {
            "id": 6,
            "position": 0,
            "visible": False,
            "variation": True,
            "options": [
                "Black",
                "Green"
            ]
        },
        {
            "name": "Size",
            "position": 0,
            "visible": True,
            "variation": True,
            "options": [
                "S",
                "M"
            ]
        }
    ],
    "default_attributes": [
        {
            "id": 6,
            "option": "Black"
        },
        {
            "name": "Size",
            "option": "S"
        }
      ]
    }
    # make the call
    rs_api = product_helper.call_create_product(payload)

    # verify the response is not empty
    assert rs_api

    # verify the product exists in db
    ID =  rs_api['id']

    rs_db = products_dao.get_product_by_id(ID)
    #import pdb; pdb.set_trace()
    assert rs_api['name'] == rs_db[0]['post_name']
