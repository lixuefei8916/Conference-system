#-*- coding: utf-8 -*-

'''
# from Python08.docx (no web view)
# Learn to walk before you run.

学习目的：简单的MVC及ORM实现，希望代码思路正确 (Model使用sqlalchemy / View 暂时print / Controller从model取值，传递给view打印)
程序介绍：账户注册，insert用户名、密码和邮箱(假设用户输入的符合规范，更成熟功能后期完善)，
          print出查询结果
学习日期：2015.12.01
'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text

db = create_engine('mysql://lixuefei:123456@127.0.0.1')
db.execute('USE conference')
#db.echo=True
Base = declarative_base()

class Account_model(Base):						# Account_model = account表名(mysql)
	__tablename__ = 'account'
	#原mysql语句
	#CREATE TABLE account(user_id INT PRIMARY KEY AUTO_INCREMENT,user_name VARCHAR(250),user_password VARCHAR(250),user_mail VARCHAR(250));
	user_id = Column(Integer,primary_key=True)	# id自增id=id+1 AUTO_INCREMENT ; PRIMARY KEY 拥有自动定义的 UNIQUE 约束。
	user_name = Column(String(250))				# user_name 唯一性 UNIQUE
	user_password = Column(String(250))
	user_mail = Column(String(250))

	def __repr__(self):
		return "<account(user_id='%s',user_name='%s',user_password='%s',user_mail='%s')>"%(self.user_id,self.user_name,self.user_password,self.user_mail)

class View(object):
	def __init__(self):
		pass

	def print_account_detail(self,account_detail):		#接收 class Account_Controller.(def)get_account_detail的查询结果，然后print出来
		print account_detail

class Account_Controller(object):
	def __init__(self):
		self.model = Account_model()
		self.view = View()

		self.__user_name = ''
		self.__user_password = ''
		self.__user_mail = ''

	def registe_user_name(self,user_name):					# 接收用户的 username (暂且 先假设用户输入的符合规范，更成熟功能后期完善)
		self.__user_name = user_name

	def registe_user_password(self,user_password):			# 接收用户的 password(暂且 先假设用户输入的符合规范，更成熟功能后期完善)
		self.__user_password = user_password

	def registe_user_mail(self,user_mail):					# 接收用户的 邮箱(暂且 先假设用户输入的符合规范，更成熟功能后期完善)
		self.__user_mail = user_mail

	def insert_account_detail(self):						# insert 进mysql
		#Insert数据
		#Account_model(user_name='example0',user_password='123456',user_mail='test0@lixuefei.com')

		account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)
		session = sessionmaker(bind=db)
		session = session()
		session.add(account)
		session.commit()

	def get_account_detail(self):							# select user_id==13 from account
		username = self.__user_name
		account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)
		session = sessionmaker(bind=db)
		session = session()
		account_detail = session.query(Account_model).filter(Account_model.user_id==13).one()
		self.view.print_account_detail(account_detail)



username = 'example13'
userpassword = '22222222222'
usermail = 'example3@lixuefei.com'

if __name__ == '__main__':
	lxf = Account_Controller()
	lxf.registe_user_name(username)
	lxf.registe_user_password(userpassword)
	lxf.registe_user_mail(usermail)
	lxf.insert_account_detail()
	lxf.get_account_detail()



