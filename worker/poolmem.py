from rich import print
import base64 as fox

INIT_FORMAT = {
	'SECRET': 'IamKnownAsSUS', 
	'SECRET_KEY': 'jeSUS', 
	'Author': 'Cyber2f08', 
	'ADMIN': 'sp0f.p12', 
	'MODERATOR': 'Cyber2f08', 
	'EMAIL': 'cyber.2f08@gmail.com',
	'LOCKER': 'LET_ME_IN!'
}


MEM_LOCK_INFO = {
	'Not Found': 'Sorry the item is not found!',
	'Not String': 'This kind of variable is not a string!'
}

CONDITION_INFO = {
	'DECODE': 'Cannot continue to decode...',
	'ENCODE': 'Cannot continue to encode...'
}

LOCKER_PASS = {
	'BOOT_Ubyt': 'Cyber2f08',
	'BOOT_Pbyt': '1234'
}

class memGIX():
	def load(INITVAR):
		if INITVAR in INIT_FORMAT:
			return fox.b64encode(INIT_FORMAT[str(INITVAR)].encode('ascii')).decode('ascii')
		print(MEM_LOCK_INFO['Not Found'])
	def lock_BYT0(LOCKER):
		if LOCKER in LOCKER_PASS:
			return LOCKER_PASS[LOCKER]
		print(MEM_LOCK_INFO['Not Found'])
	def dec_BYT0(STRING):
		if STRING is str():
			return fox.b64decode(STRING.encode('ascii')).decode('ascii')
		print(MEM_LOCK_INFO['Not String'], CONDITION_INFO['DECODE'])
	def enc_BYT0(STRING):
		if STRING is str():
			return fox.b64encode(STRING.encode('ascii')).decode('ascii')
		print(MEM_LOCK_INFO['Not String'], CONDITION_INFO['ENCODE'])