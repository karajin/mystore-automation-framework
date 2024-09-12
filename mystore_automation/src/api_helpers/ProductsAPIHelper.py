
from src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger

class ProductsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()
    
    def call_get_product_py_id(self, product_id):
        return self.woo_api_utility.get(f"products/{product_id}", expected_status_code=200)
    
    def call_create_product(self, payload, status_code=201):
        return self.woo_api_utility.post('products', params=payload, expected_status_code=status_code)

    def call_update_product(self, product_id, payload):
        return self.woo_api_utility.put(f"products/{product_id}", params=payload, expected_status_code=200)
    
    def call_get_product(self, payload=None):
        if not payload:
            payload={'per_page':100}
        elif 'per_page' not in payload.keys():
            payload['per_page']=100
        rs_api = self.woo_api_utility.get('products',  params=payload, return_headers=True, expected_status_code=200)
        total_number_of_pages = rs_api['headers']['X-WP-TotalPages']
        
        all_products = []
        all_products.extend(rs_api['response_json'])

        for i in range(2, int(total_number_of_pages)+1):
            logger.debug(f"List products page number: {i}")
            payload['page'] = i
            rs_api = self.woo_api_utility.get('products', params=payload, return_headers=True)
            all_products.extend(rs_api['response_json'])

        return all_products
    
    def call_delete_product(self, product_id, expected_status_code):
        return self.woo_api_utility.delete(f"products/{product_id}", expected_status_code=expected_status_code)
    
    def call_list_products(self, payload=None):

        # if max number of products per page is not provided then use the max to reduce number of calls
        if not payload:
            payload = {'per_page': 100}
        elif 'per_page' not in payload.keys():
            payload['per_page'] = 100

        rs_api = self.woo_api_utility.get('products', params=payload, return_headers=True)
        total_number_of_pages = rs_api['headers']['X-WP-TotalPages']

        all_products = []
        all_products.extend(rs_api['response_json']) # since the first page is fetched use that
        for i in range(2, int(total_number_of_pages) + 1):  # start from 2 because this will be used for page number and page 1 is fetched already
            logger.debug(f"List products page number: {i}")
            payload['page'] = i
            rs_api = self.woo_api_utility.get('products', params=payload, return_headers=True)
            all_products.extend(rs_api['response_json'])

        return all_products