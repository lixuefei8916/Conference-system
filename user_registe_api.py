#-*- coding: utf-8 -*-
import view
import controller
# import view 是获取用户输入 username,passwd和mail
#回显注册成功 和 注册信息

class User__(object):
	def __init__(self):
		pass

	def get_user_name(self):
		user_name = view.user_name
		return user_name

	def get_user_password(self):
		user_password = view.user_password
		return user_password

	def get_user_mail(self):
		user_mail = view.user_mail
		return user_mail

	#def push_api(self):
	#	self.controller.get_api()

'''
此时可以传入数据，并且打印
lxf = User()
lxf.get_user_name()
lxf.get_user_password()
lxf.get_user_mail()
'''

