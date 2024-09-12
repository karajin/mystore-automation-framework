
import pytest
from src.api_helpers.CustomerAPIHelper import CustomerAPIHelper
from src.generichelpers.generic_customer_helpers import GenericCustomerHelper
from src.dao.customers_dao import CustomersDAO
import pdb

@pytest.mark.customer
@pytest.mark.tcid215
def test_delete_a_customer():
  """Delete a customer and ensure the customer no longer exists in the database and cannot be retrieved via API."""
  customer_dao = CustomersDAO()
  customer_helper = CustomerAPIHelper()
  random_customer = customer_dao.get_random_customer_from_db()
  customer_id = random_customer[0]['ID']
  payload = {"force": True}
  customer_helper.call_delete_customer_by_id(customer_id, payload)
  customer = customer_dao.get_customer_by_ID(customer_id)
  assert customer==(), f"Customer no longer exists in the database, but returned {customer}"

@pytest.mark.customer
@pytest.mark.tcid217
def test_delete_non_exsit_customer():
  generic_customer_helper = GenericCustomerHelper()
  customer_helper = CustomerAPIHelper()
  customer_id = generic_customer_helper.get_maximum_customer_id() +100

  payload = {"force": True}
  non_exsit_customer = customer_helper.call_delete_customer_by_id(customer_id, payload, status_code=400)
  assert non_exsit_customer['code'] == 'woocommerce_rest_invalid_id'
  assert non_exsit_customer['data'] == {'status': 400}
  assert non_exsit_customer['message'] == 'Invalid resource id.'
