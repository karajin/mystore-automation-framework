from src.utilities.wooAPIUtility import WooAPIUtility

class CustomerAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def update_customer_by_id(self, customer_id, payload):
        return self.woo_api_utility.put(f'customers/{customer_id}', params=payload)
    
    def get_customer_by_id(self, customer_id):
        return self.woo_api_utility.get(f'customers/{customer_id}')
    
    def get_customer_by_invalid_id(self, customer_id, status_code):
        return self.woo_api_utility.get(f'customers/{customer_id}', expected_status_code=status_code)
    

    def call_delete_customer_by_id(self, customer_id, payload):
        return self.woo_api_utility.delete(f'customers/{customer_id}', params=payload)
    
    def retrive_orders_by_customer(self):
        return self.woo_api_utility.get('orders')