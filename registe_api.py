#-*- coding: utf-8 -*-
# 用户提交 username  passwd  mail信息

from controller import *  

class User__(object):
	def __init__(self):
		self.controller = Controller()

	def push_userdetail_to_Controller(self,user_name,user_password,user_mail):
		return self.controller.get_user_detail(user_name,user_password,user_mail)

'''
user_name = 'example19'
user_password = '191919191919'
user_mail = 'example19@lixuefei.com'

lxf = User__()
lxf.push_userdetail_to_Controller(user_name,user_password,user_mail)
'''