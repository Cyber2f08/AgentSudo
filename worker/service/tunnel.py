import subprocess
import os
import utils
from sys import platform

u = utils.flask_conf()

def start():
	if platform == "win32":
		subprocess.call("start ngrok http "+str(u["port"]), shell=True)