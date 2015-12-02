#-*- coding: utf-8 -*-

# 【该方法是错误的思路】
# 【该方法是错误的思路】
# 【该方法是错误的思路】
# 【该方法是错误的思路】

'''
封装session避免重复链接

session 应该封装在 init里， 不应该在 def session_keeping中
1. 初始化工作在 init 中
2. 对象是要给别人赋值的， 比如把'mysql://lixuefei:123456@127.0.0.1'封装成 {}://{}:{}@{}

'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text



class Mysql_(object):
	def __init__(self):
		self.__db = 'mysql'
		self.__

	def session_keeping(self):
		db = create_engine('mysql://lixuefei:123456@127.0.0.1')
		db.execute('USE conference')
		Session = sessionmaker(bind=db)
		session = Session()
		return session

Base = declarative_base()	# 声明ORM父类 Base

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
		self.mysql = Mysql_()
		self.session = self.mysql.session_keeping()	# 把 class Mysql_operation()中session带进来

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
		session1 = self.session.add(account)
		session1.commit()


#account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)
#session = sessionmaker(bind=db)
#session = session()
#session.add(account)
#session.commit()


	def get_account_detail(self):							# select user_id==13 from account
		username = self.__user_name
		account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)
		account_detail = self.session.query(Account_model).filter(Account_model.user_id==13).one()
		self.view.print_account_detail(account_detail)



username = 'example14'
userpassword = '141414141414'
usermail = 'example14@lixuefei.com'

if __name__ == '__main__':
	lxf = Account_Controller()
	lxf.registe_user_name(username)
	lxf.registe_user_password(userpassword)
	lxf.registe_user_mail(usermail)
	#lxf.insert_account_detail()
	lxf.get_account_detail()




