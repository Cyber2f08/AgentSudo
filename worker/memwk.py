from rich import print
import time
import os, sys

CONDITION_INFO = {
	'UNABLE': '''
	[MEM] Unable to restore any health of a python file. (*)
	''',
	'DENIED': '''
	Access Denied. (*) [MEM:0]
	'''
}



class memCOM():
	def restore_(all=True):
		if all == True:
			try:
				os.system('python -m autopep8 -i ../server.py')
				print("[MEM] Done restoring, restart the script and see if the problem solved!")
				sys.exit()
			except OSError:
				print(CONDITION_INFO['DENIED'])
				print("[MEM] Unable to restore any health of a python file. (*)")
		print(CONDITION_INFO['UNABLE'])
	def mule():
		return True
