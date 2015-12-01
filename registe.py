#-*- coding: utf-8 -*-
# from Python08.docx (no web view)
# just has registe account
# Learn to walk before you run.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql://lixuefei:123456@127.0.0.1')
db.execute('USE conference')
db.echo=True
Base = declarative_base()

class Account_model(Base):
	__tablename__ = 'account'
	#原mysql语句
	#CREATE TABLE account(user_id INT PRIMARY KEY AUTO_INCREMENT,user_name VARCHAR(250),user_password VARCHAR(250),user_mail VARCHAR(250));
	user_id = Column(Integer,primary_key=True)	# id自增id=id+1 AUTO_INCREMENT ; PRIMARY KEY 拥有自动定义的 UNIQUE 约束。
	user_name = Column(String(250))				# user_name 唯一性 UNIQUE
	user_password = Column(String(250))
	user_mail = Column(String(250))
	#def __repr__(self):
	#	return "<account(user_id='%s',user_name='%s',user_password='%s',user_mail='%s')>"%(self.user_id,self.user_name,self.user_password,self.user_mail)
'''
# Insert数据
account = Account_model(user_name='example0',user_password='123456',user_mail='test0@lixuefei.com')
'''
class View(object):
	pass

class Account_Controller(object):
	def __init__(self):
		self.model = Account_model()
		self.view = View()

		self.__user_name = ''
		self.__user_password = ''
		self.__user_mail = ''

	def registe_user_name(self,user_name):
		self.__user_name = user_name

	def registe_user_password(self,user_password):
		self.__user_password = user_password

	def registe_user_mail(self,user_mail):
		self.__user_mail = user_mail

	def account_detail(self):
		account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)
		session = sessionmaker(bind=db)
		session = session()
		session.add(account)
		session.commit()

username = 'example1'
userpassword = 'xxxxxxx'
usermail = 'example1xxxxx@lixuefei.com'

if __name__ == '__main__':
	lxf = Account_Controller()
	lxf.registe_user_name(username)
	lxf.registe_user_password(userpassword)
	lxf.registe_user_mail(usermail)
	lxf.account_detail()




