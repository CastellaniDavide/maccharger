"""Test maccharger file
"""
from maccharger import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-11-5"

def test():
	"""Tests the maccharger function in the maccharger class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert maccharger.maccharger() == "maccharger", "test failed"
	#assert maccharger.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
