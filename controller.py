#-*- coding: utf-8 -*-

import view
from user_registe_api import *
from db_operation import Sql_Statement,Table_account

'''
账户注册 工作流：
	1. view.py		  		用户提交  暂用raw_input代替web(提交username,passwd和mail)
	2. view.py		  		提交参数  给user_registe_api.py
	3. user_registe_api.py  提交参数  给controller.py
	4. controller.py  		提交参数  到数据库db_operation.py（model）

用户在view注册，利用api  传给controller，然后insert给model
用户在view查询，利用api  传给controller，然后到model里select
'''


class Controller(object):
	def __init__(self):

		#self.view = View()
		self.model = Sql_Statement()
		self.api = User__()

		self.__user_name = ''
		self.__user_password = ''
		self.__user_mail = ''

	def get_api(self):
		self.__user_name = self.api.get_user_name()
		self.__user_password = self.api.get_user_password()
		self.__user_mail = self.api.get_user_mail()


	def insert_account_detail(self):						# insert 进mysql
		#Insert数据
		#table_name = Table_account
		self.model.insert_new_account(self.__user_name,self.__user_password,self.__user_mail)

	def get_account_detail(self,user_name):							# select user_id==13 from account
		account_detail = self.mysql.select_account_detail(user_name)
		self.view.print_account_detail(account_detail)

if __name__ == '__main__':
	lxf = Controller()
	lxf.get_api()
	lxf.insert_account_detail()
	#lxf.get_account_detail('example15')