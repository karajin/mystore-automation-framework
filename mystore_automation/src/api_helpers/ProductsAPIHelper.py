
from src.utilities.wooAPIUtility import WooAPIUtility


class ProductsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()
    
    def call_get_product_py_id(self, product_id):
        return self.woo_api_utility.get(f"products/{product_id}", expected_status_code=200)
    
    def call_create_product(self, payload, status_code=201):
        return self.woo_api_utility.post('products', params=payload, expected_status_code=status_code)

    def call_update_product(self, product_id, payload):
        return self.woo_api_utility.put(f"products/{product_id}", params=payload, expected_status_code=200)
    
    def call_get_product(self, payload):
        return self.woo_api_utility.get(f"products",  params=payload, expected_status_code=200)
    