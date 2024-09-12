import pytest
from src.dao.products_dao import ProductsDAO
from src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import random


@pytest.mark.tcid61
@pytest.mark.ecombe30
def test_update_regular_price_should_update_price():
  product_helper=ProductsAPIHelper()
  filters={
      'on_sale':False,
      'per_page':100
  }
  prodcuts_not_on_sale = product_helper.call_get_product(filters)
  #if found products no one sale, pick a random prodcut
  if prodcuts_not_on_sale:
    random_product = random.choice(prodcuts_not_on_sale)
    product_id = random_product['id']
  else:
    products = product_helper.call_get_product()
    random_product = random.choice(products)
    product_id = random_product['id']
    product_helper.call_update_product(product_id=product_id, payload={'sale_price':''})

  new_price = str(random.randint(10, 100)) + '.' + str(random.randint(10, 99))
  payload = {'regular_price':new_price}
  rs_update = product_helper.call_update_product(product_id=product_id, payload=payload)
# import pdb; pdb.set_trace()

  assert rs_update['price'] == new_price
  assert rs_update['regular_price'] == new_price

  rs_product = product_helper.call_get_product_py_id(product_id)

  assert rs_product['price'] == new_price
  assert rs_product['regular_price'] == new_price


@pytest.mark.ecombe34
@pytest.mark.tcid65
@pytest.mark.ecombe37
def test_adding_sale_price_should_set_on_sale_flag_true():
    """Verifies When the sale price of a product is updated, then it should set the field 'on_sale' = True"""
    product_helper=ProductsAPIHelper()
    filters={
      'on_sale':False,
      'per_page':100
    }
    prodcuts_not_on_sale = product_helper.call_get_product(filters)
    random_product = random.choice(prodcuts_not_on_sale)

    assert random_product['on_sale'] == False

    product_id = random_product['id']
    sale_price = float(random_product['regular_price']) * 0.75
    payload = {'sale_price': str(sale_price)}
    product_helper.call_update_product(product_id=product_id, payload=payload)
    rs_product = product_helper.call_get_product_py_id(product_id)

    assert rs_product['sale_price'] == str(sale_price)


@pytest.mark.ecombe32
@pytest.mark.ecombe33
@pytest.mark.tcid63
@pytest.mark.tcid64
@pytest.mark.ecombe32
@pytest.mark.ecombe33
def test_update_on_sale_field_buy_updating_sale_price():
    """
    Two test case.
    First case update the 'sale_price' and verify the field changes to 'on_sale=True'.
    Second case update the 'sale_price=""' and verify the field changes to 'on_sale=False'.
    """
    product_helper=ProductsAPIHelper()
    #create a product 
    payload ={
       "name": "Hat ",
      "type": "simple",
      "regular_price": "21.99",
    }
    product = product_helper.call_create_product(payload)
    product_id = product['id']
    #make sure 'on_sale' is Flase, 'sale_price' is empty
    assert not product['on_sale']
    assert not product['sale_price']
    #update the sale_pice by 25% off
    sale_price = float(product['regular_price']) * 0.75
    payload = {'sale_price': str(sale_price)}
    product_helper.call_update_product(product_id=product_id, payload=payload)
    #test 'on_sale' is True, 'sale_price' is not empty
    product_after_update = product_helper.call_get_product_py_id(product_id)
    assert product_after_update['on_sale']
    product_helper.call_update_product(product_id, {'sale_price': ''})
    product_after_update = product_helper.call_get_product_py_id(product_id)
    assert not product_after_update['on_sale']
    
