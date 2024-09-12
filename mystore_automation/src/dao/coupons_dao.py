from src.utilities.dbUtility import DBUtility
import random
import logging as logger

class CouponsDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_expired_coupon(self, qty=1):
        sql = f'''SELECT post_id as coupon_id, post_title as coupon_code FROM {self.db_helper.database}.{self.db_helper.table_prefix}postmeta pm 
                  JOIN {self.db_helper.database}.{self.db_helper.table_prefix}posts p ON pm.post_id = p.id
                  WHERE p.post_type = 'shop_coupon' AND pm.meta_key = 'date_expires'
                  AND FROM_UNIXTIME(meta_value) < NOW() LIMIT 1000;'''
       
       
        """SELECT post_id as coupon_id, post_title as coupon_code FROM mystore.wp_postmeta JOIN mystore.wp_posts ON mystore.wp_postmeta.post_id = mystore.wp_posts.id
                  WHERE mystore.wp_posts.post_type = 'shop_coupon' AND mystore.wp_postmeta.meta_key = 'date_expires'
                  AND FROM_UNIXTIME(meta_value) < NOW() LIMIT 100;"""
        
        coupons = self.db_helper.execute_select(sql)

        return random.sample(coupons, int(qty))
    

    def get_random_coupon_from_db(self, qty=1):
        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
                       WHERE post_type = "shop_coupon" LIMIT 5000;'''
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))