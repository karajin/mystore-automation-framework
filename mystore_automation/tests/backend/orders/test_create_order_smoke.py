from src.dao.products_dao import ProductsDAO
from src.dao.customers_dao import CustomersDAO

from src.api_helpers.OrdersAPIHelper import OrdersAPIHelper

from src.api_helpers.CustomerAPIHelper import CustomerAPIHelper
from src.generichelpers.generic_order_helpers import GenericOrderHelpers

import pytest

@pytest.fixture(scope='module')
def my_orders_smoke_setup():
  product_dao = ProductsDAO()
  generic_order_helper = GenericOrderHelpers()

  product = product_dao.get_random_product_from_db(qty=1)
  product_id = product[0]['ID']
  info = {
    'product_id':product_id,
    'generic_order_helper':generic_order_helper
  }
  return info


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.ecombe52
@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_orders_smoke_setup):  
  """
       Test case to verify the creation of a paid order by a guest user.

       Args:
       my_orders_smoke_setup (dict): Information needed for the test.

    """
  
  generic_order_helper = my_orders_smoke_setup['generic_order_helper']
  product_id = my_orders_smoke_setup['product_id']
  customer_id = 0
  
  info = {
    'line_items':
    [
      {
        'product_id':product_id,
        'quantity':1
      }
    ]
  }

  order = generic_order_helper.create_order(additional_args=info)

  #verify response
  product_id = [{'product_id':product_id}]
  generic_order_helper.verify_order_is_created(order, customer_id, product_id)

@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.ecombe53
@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_orders_smoke_setup):
    """
        Test case to verify the creation of a paid order by a newly created customer.

        Args:
            my_orders_smoke_setup

    """
    generic_order_helper = my_orders_smoke_setup['generic_order_helper']
    product_id = my_orders_smoke_setup['product_id']
    customer = CustomerAPIHelper().call_create_customer()
    customer_id = customer['id']
    
  
    info = {
      'line_items':[
        {
          'product_id':product_id,
          'quantity':1
        }],
      'customer_id': customer_id
    }

    order = generic_order_helper.create_order(additional_args=info)

    #verify response
    product_id = [{'product_id':product_id}]
    generic_order_helper.verify_order_is_created(order, customer_id, product_id)


@pytest.mark.ecombe54
def test_create_paid_order_returning_customer(my_orders_smoke_setup):
    """
        Test case to verify the creation of a paid order by a returning  customer.

        Args:
            my_orders_smoke_setup

    """
    generic_order_helper = my_orders_smoke_setup['generic_order_helper']
    product_id = my_orders_smoke_setup['product_id']

    customer_dao = CustomersDAO() 
    customer = customer_dao.get_random_customer_from_db(qty=1)
    #import pdb; pdb.set_trace()
    customer_id = customer[0]['ID']

    info = {
      'line_items':[
        {
          'product_id':product_id,
          'quantity':1
        }],
      'customer_id': customer_id
    }
    
    order = generic_order_helper.create_order(additional_args=info)

    exp_product_id = [{'product_id':product_id}]
    generic_order_helper.verify_order_is_created(order, customer_id, exp_product_id)

