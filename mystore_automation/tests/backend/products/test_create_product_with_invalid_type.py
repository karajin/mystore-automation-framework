
import pytest
from src.dao.products_dao import ProductsDAO
from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger

@pytest.mark.ecombe118
def test_create_product_with_invalid_type():
  payload ={'name':'shirt',
            'type':'abcd',
            'price':'12.99'}
  product_helper = ProductsAPIHelper()
  product_rs = product_helper.call_create_product(payload, status_code=400)
  assert product_rs['code']=='rest_invalid_param', f"prodcut type {payload['type']} is invalid"



