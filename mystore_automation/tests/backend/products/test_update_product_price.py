
import pytest
from src.dao.products_dao import ProductsDAO
from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import random
import string

@pytest.mark.tcid61
@pytest.mark.ecombe30

def test_update_regular_price_should_update_price():
  prodcut_helper = ProductsAPIHelper()
  product_dao = ProductsDAO()
# find the prodcut list that's no onsale
  payload = {
    'on_sale': False,
    'per_page' : 100
  }

  product_not_on_sale = prodcut_helper.call_get_product(payload)

  if product_not_on_sale:
    selected_product = random.choice(product_not_on_sale)
    product_id = selected_product['id']
  else:
    


#if found products no one sale, pick a random prodcut

#if all products on sale, get the full list of the products, and pick a random prodcut, then update the sale price to be ''

#update the product price