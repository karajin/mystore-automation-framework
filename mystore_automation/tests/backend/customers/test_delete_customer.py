
import pytest
from src.api_helpers.CustomerAPIHelper import CustomerAPIHelper
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