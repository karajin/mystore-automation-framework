

from src.utilities.dbUtility import DBUtility
import random
import logging as logger

class CustomersDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"""SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}users 
                  WHERE user_email = '{email}';"""

        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_customer_from_db(self, qty=1):
        sql = f"SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}users order by id desc LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)
        logger.info(f"Found {len(rs_sql)} random users from db.")
        return random.sample(rs_sql, int(qty))

    def get_customer_by_ID(self, ID):
        sql = f"""SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}users 
                  WHERE ID = {ID};"""

        rs_sql = self.db_helper.execute_select(sql)
        
        return rs_sql

    
