from src.api_helpers.CustomerAPIHelper import CustomerAPIHelper

class GenericCustomerHelper(CustomerAPIHelper):
        
        def get_maximum_customer_id(self):
            payload = {
                  'order': 'desc',
                  'orderby': 'id'
            }
            customer_list = self.call_list_all_customers(payload)
            return customer_list[0]['id']

