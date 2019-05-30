import unittest
import HTMLTestReportEN
import os
import datetime


#获取当前时间
nowTime=datetime.datetime.now().strftime('%Y-%m-%d')
proDir=os.path.realpath(__file__)
print(proDir)
class MyTest(unittest.TestCase):
    def terDown(self):
        print('每个测试用例执行之后做操作')

    def setUp(self):
        print('2每个测试用例执行之前做操作')

    @classmethod
    def tearDownClass(self):
        print('必须使用 @ classmethod装饰器, 所有test运行完后运行一次')
    @classmethod
    def setUpClass(self):
        print('必须使用 @ classmethod装饰器, 所有test运行完钱运行一次')

    def test_first_run(self):
        print('test_a_run')
        self.assertEqual(1,1)

    def test_b_run(self):
        print('1test_b_run')
        self.assertEqual(2,2)


if __name__ == '__main__':
    test_suite=unittest.TestSuite()
    test_suite.addTest(MyTest('test_first_run'))
    test_suite.addTest(MyTest('test_b_run'))
    reportName='APITestReport '+nowTime+'.html'
    fp=open(reportName,'wb')
    runner=HTMLTestReportEN.HTMLTestRunner(stream=fp,title='api测试报告',tester='ZhaoJun')
    runner.run(test_suite)


