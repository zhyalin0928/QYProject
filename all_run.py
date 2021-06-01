"""
@Time      ：2021/5/14 17:09
@Author    ：赵亚林
@Function  ：all_run
"""
import pytest
import os

if __name__ == '__main__':
    pytest.main(['-vs', './cases', '--alluredir', 'result'])
    os.system('allure generate result -o report --clean')
