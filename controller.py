#-*- coding: utf-8 -*-
from db_operation import Sql_Statement,Table_account

'''
账户注册 工作流：
	1. view.py		  		用户提交  暂用raw_input代替web(提交username,passwd和mail)
	2. view.py		  		提交参数  给controller.py
	4. controller.py  		提交参数  给model执行insert

用户在view注册，利用api  传给controller，然后insert给model
用户在view查询，利用api  传给controller，然后到model里select
'''


class Controller(object):
	def __init__(self):
		self.model = Sql_Statement()

	# api提交后，将参数传到这里,然后return给同对象的insert_account_detail函数
	def get_user_detail(self,user_name,user_password,user_mail):
		return self.insert_account_detail(user_name,user_password,user_mail)

	def insert_account_detail(self,user_name,user_password,user_mail):		# insert 进mysql
		self.model.insert_new_account(user_name,user_password,user_mail)
		return 'OK'
	def get_account_detail(self,user_name):							# select user_id==13 from account
		account_detail = self.mysql.select_account_detail(user_name)
		self.view.print_account_detail(account_detail)
