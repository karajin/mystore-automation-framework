from src.utilities.wooAPIUtility import WooAPIUtility

class ProductsTagAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_product_tag(self, payload, expected_status_code=200):
        return self.woo_api_utility.post('products/tags', params=payload, expected_status_code=expected_status_code)

    def call_retrive_product_tag_by_id(self, tag_id, expected_status_code=200):
        return self.woo_api_utility.get(f'products/tags/{tag_id}', expected_status_code=expected_status_code)
    
    def call_list_all_product_tags(self, expected_status_code=200):
        return self.woo_api_utility.get('products/tags', expected_status_code=expected_status_code)

    def call_update_product_tag(self, tag_id, payload, expected_status_code=200):
        return self.woo_api_utility.put(f'products/tags/{tag_id}', params=payload, expected_status_code=expected_status_code)
    
    def call_delete_product_tag_by_id(self, tag_id, expected_status_code=200):
        return self.woo_api_utility.delete(f'products/tags/{tag_id}', params={'force':True}, expected_status_code=expected_status_code)