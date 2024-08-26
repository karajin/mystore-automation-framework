
import pytest
from src.dao.products_dao import ProductsDAO
from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import random
import string

@pytest.mark.tcid61
@pytest.mark.ecombe30

def test_update_regular_price_should_update_price():
    pass


#if found products no one sale, pick a random prodcut

#if all products on sale, get the full list of the products, and pick a random prodcut, then update the sale price to be ''

#update the product price