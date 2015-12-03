#-*- coding: utf-8 -*-
# 测试用例

import unittest
from registe_api import *

class Test_registe_api(unittest.TestCase):
	def test_user_Submit(self):
		self.registe_api = User__()
		user_Submit = self.registe_api.push_userdetail_to_Controller('example20','202020','example20@lixuefei.com')
		self.assertEquals(user_Submit,'OK')

if __name__ == '__main__':
	unittest.main()