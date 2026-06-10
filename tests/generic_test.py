import pytest 

from sample_feature import arg_list

def test_launch():
	assert(True)

def test_addition():
	sum = 2+2
	assert 2+2 == 4

def test_argument_list():
	test_list = [1,2]
	return_list = arg_list(test_list)
	assert return_list[0] == test_list[0]
	assert return_list[1] == test_list[1]
