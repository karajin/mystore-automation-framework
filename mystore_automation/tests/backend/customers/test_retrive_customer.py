
import pytest
from src.api_helpers.CustomerAPIHelper import CustomerAPIHelper
from src.dao.customers_dao import CustomersDAO
import pdb
import random
@pytest.mark.customer
@pytest.mark.tcid210
def test_retive_customer_by_invalid_id():
  """Attempt to retrieve a customer using an invalid ID and verify that the API returns a 404 error."""

  customer_helper = CustomerAPIHelper()
  random_id = random.randint(1000, 2000)
  rs_api = customer_helper.get_customer_by_invalid_id(random_id, status_code = 404)

  assert rs_api['data']['status'] == 404, f"Expected status code is 404, but actual status code is {rs_api['data']['status']}"


  
  
