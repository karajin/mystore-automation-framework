from src.utilities.wooAPIUtility import WooAPIUtility

from src.utilities.genericUtilities import generate_random_email_and_password
class CustomerAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def update_customer_by_id(self, customer_id, payload, status_code = 200):
        return self.woo_api_utility.put(f'customers/{customer_id}', params=payload, expected_status_code=status_code)
    
    def get_customer_by_id(self, customer_id):
        return self.woo_api_utility.get(f'customers/{customer_id}')
    
    def get_customer_by_invalid_id(self, customer_id, status_code=200):
        return self.woo_api_utility.get(f'customers/{customer_id}', expected_status_code=status_code)
    
    def call_delete_customer_by_id(self, customer_id, payload, status_code=200):
        return self.woo_api_utility.delete(f'customers/{customer_id}', params=payload, expected_status_code = status_code)
    
    def retrive_orders_by_customer(self):
        return self.woo_api_utility.get('orders')
    
    def call_list_all_customers(self, payload):
        return self.woo_api_utility.get(f'customers', params=payload)

    def call_create_customer(self, email=None, password=None, expected_status_code=201, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_user_json = self.woo_api_utility.post('customers', params=payload, expected_status_code=expected_status_code)

        return create_user_json