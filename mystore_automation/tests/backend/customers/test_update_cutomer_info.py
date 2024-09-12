import pytest
from src.api_helpers.CustomerAPIHelper import CustomerAPIHelper
from src.dao.customers_dao import CustomersDAO
from src.utilities.genericUtilities import generate_random_email_and_password
import random
import string
@pytest.mark.customer
@pytest.mark.tcid214
def test_update_cutomer_info():
        """Update an existing customer's details like name, email, or password and verify the changes are reflected in the database."""
        cutomer_dao = CustomersDAO()
        customer_helper = CustomerAPIHelper()
        #get a cutomer info from db
        random_customer = cutomer_dao.get_random_customer_from_db()
        length = 5
        first_name = ''.join(random.choices(string.ascii_lowercase, k=length))
        last_name = ''.join(random.choices(string.ascii_lowercase, k=length))
        customer_id = random_customer[0]['ID']
        get_api = customer_helper
        data = {
          "first_name": first_name,
          "last_name": last_name,
          "billing": {
              "first_name": first_name,
              "last_name": last_name,
          },
          "shipping": {
              "first_name": first_name,
              "last_name": last_name,
          }
        }
        rs_api = customer_helper.update_customer_by_id(customer_id, data)
        #pdb.set_trace()
        assert rs_api['first_name'] == data['first_name'] and rs_api['last_name'] == data['last_name']

        #update the email
        #make the call
        #verify with the db


@pytest.mark.customer
@pytest.mark.tcid213
def test_update_customer_invalid_data():
        customer_helper = CustomerAPIHelper()
        customer_dao = CustomersDAO()
        customer = customer_dao.get_random_customer_from_db()
        #rs_api = customer_helper.get_customer_by_id(customer[0]['ID'])

        payload = {
                  "first_name": "",
                  "email": "invalid_email"
        }

        rs_api = customer_helper.update_customer_by_id(customer[0]['ID'], payload, status_code = 400)
  
        assert rs_api['code'] == 'rest_invalid_param'
        assert rs_api['data'] == {'details': {'email': {'code': 'rest_invalid_email',
                                'data': None,
                                'message': 'Invalid email address.'}},
          'params': {'email': 'Invalid email address.'},
          'status': 400}
        assert rs_api['message'] == 'Invalid parameter(s): email'