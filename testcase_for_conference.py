#-*- coding: utf-8 -*-
# 测试用例

import unittest
from registe_api import *
'''
注册帐号 
1. 新建主持人	api(py).push_userdetail_toController -->  (Model)insert_new_account
2. 新建参会人

会议主持人[新建工作]--工作流
1. 新建会议 +　设置参会人
2. 发表评论

attendee参会人[参与]--工作流
1. 搜索会议（True 自己可参会的会议）
2. 搜索会议（False 无权限参会的会议）
2. 查看参会人（True 自己可参会的会议）
3. 发表评论（True 自己可参会的会议）
4. 查看评论（True 自己可参会的会议）

会议主持人[结束阶段]--工作流
1. 删除评论
2. 删除参会人
3. 删除会议
'''


class Test_registe_api(unittest.TestCase):
	#创建 会议主持人 帐号
	def test_registe_conference_host(self):
		self.registe_api = User__()
		user_Submit = self.registe_api.push_userdetail_to_Controller('host1','111111','host1@lixuefei.com')
		self.assertEquals(user_Submit,'OK')

	# 创建 参会人 账号
	def test_registe_attendee(self):
		self.registe_api = User__()
		user_Submit = self.registe_api.push_userdetail_to_Controller('people1','11111','people1@lixuefei.com')
		self.assertEquals(user_Submit,'OK')		

class Test_conference_host_start(unittest.TestCase):
	# 主持人新建会议
	def test_create_new_meeting(self):
		# 需要一个 conference_host_api.py 文件，meeting对象，用于主持人创建
		self.conference_host_api = Meeting():
		host_Submit = self.conference_host_api.create_new_meeting('新建会议1',参会人any)
		self.assertEquals(user_Submit,'OK')

		host_Submit = self.conference_host_api.create_new_meeting('新建会议2',参会人just=='lixuefei')
		self.assertEquals(user_Submit,'OK')

	# 主持人发表评论
	def test_new_comment(self):
		self.comment_host_api = Meeting():
		host_Submit = self.conference_host_api.new_comment(会议1，'点名')
		self.assertEquals(user_Submit,'OK')
		host_Submit = self.conference_host_api.new_comment(会议1，'静一静')
		self.assertEquals(user_Submit,'OK')

class Test_attendee(unittest.TestCase):
	#搜索会议（True 自己可参会的会议）
	def meeting_search(self):
		searchall = Search_meetings()
		self.assertTrue(isinstance(searchall,只有会议1))
		self.assertTrue(isinstance(searchall,无权查看该会议))

	def attendee_search(self):
		self.assertTrue(isinstance(searchall,参会人))

	def test_new_comment(self):
		self.comment_host_api = Meeting():
		host_Submit = self.conference_host_api.new_comment(会议1，'睡觉')
	# 评论搜索
	def comment_search(self):
		self.assertTrue(isinstance(searchall,只有会议1的评论))

class Test_conference_host_final(unittest.TestCase):
	# 删除评论
	def comment_del(self):
		self.comment_host_api = Meeting():
		host_Submit = self.del_comment(会议1，'睡觉')

	# 踢出参会人
	def Drive participants(self):
		self.comment_host_api = Meeting():
		host_Submit = self.del_attendee(会议1，lixueife)		

	# 删除会议
	def meeting_del(self):
		self.comment_host_api = Meeting():
		host_Submit = self.del_attendee(会议1，lixueife)				

if __name__ == '__main__':
	unittest.main()