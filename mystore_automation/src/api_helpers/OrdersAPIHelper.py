from src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger

class OrdersAPIHelper(WooAPIUtility):

    def call_create_order(self, payload, expected_status_code=201):
        return self.post('orders', params=payload, expected_status_code=expected_status_code)
    
    def update_order(self, order_id, payload, status_code=200):
        return self.put(f'orders/{order_id}', params=payload, expected_status_code=status_code)
    
    def retrive_order(self, order_id, status_code=200):
        return self.get(f'orders/{order_id}', expected_status_code=status_code)
    
    def delete_order_by_id(self, order_id,expected_status_code=200):
        return self.delete(f'orders/{order_id}', expected_status_code=expected_status_code)

    def call_create_order_note(self,order_id, payload, expected_status_code=201):
        return self.post(f'orders/{order_id}/notes', params=payload, expected_status_code=expected_status_code)

    def call_retrieve_an_order_note(self,order_id, note_id,expected_status_code=200):
        return self.get(f"orders/{order_id}/notes/{note_id}", expected_status_code=expected_status_code)

    def delete_order_note(self, order_id,note_id,expected_status_code=200,force=True):
        return self.delete(f'orders/{order_id}/notes/{note_id}', expected_status_code=expected_status_code, params={"force": force})
  
    def call_list_orders(self, payload, expected_status_code=200):
        return self.get('orders', params=payload, expected_status_code=expected_status_code)

    def call_create_order_note(self, order_id, payload, expected_code=201):
        return self.post(f'orders/{order_id}/notes',params=payload, expected_status_code=expected_code)

    def call_delete_order_note_by_id(self,order_id, note_id, expected_code=200):
  
        return self.delete(f'orders/{order_id}/notes/{note_id}', params={'force':True},expected_status_code=expected_code)
    
    def call_list_all_order_notes(self, order_id, expected_code=200):
        return self.get(f'orders/{order_id}/notes', expected_status_code=expected_code)
    
    def retrive_order_note_by_id(self, order_id, note_id, expected_code=200):
        return self.get(f'orders/{order_id}/notes/{note_id}', expected_status_code=expected_code)