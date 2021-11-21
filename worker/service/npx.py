import os, sys
import random
import glob
import json
import itertools
from rich import print
from sys import platform

# PYINT
import os, sys, requests, platform


import time, random
EMP = "[[cyan]Purify[/cyan]]"
PTS = []
PTM = []
INST = 0
INIT = os.getcwd()
PATH = "\package\scripts\\"
FULL = INIT+PATH
ERR_NOT_FOLD = "[MEM] Error folder not found"
os.chdir("bin/")

class script():
	def install():
		global INST
		#print("[[cyan]NPX[/cyan]] NPX Package management is still going under development... (PLEASE WAIT) ")
		print("[[purple]NPX[/purple]] Initialized... (v1)")
		time.sleep(random.uniform(3, 0.01))
		time.sleep(random.uniform(0.1, 0.001))
		print("[[cyan]NPX[/cyan]] Initiating [green]purify[/green] scripts... ")
		print("[[yellow]NPX[/yellow]] Pulling local addon scripts...")
		for file in os.listdir(FULL):
			if file.endswith(".json"):
				PTM.append(file)
				PTS.append(FULL+file)
				continue
			else:
				continue
		try:
			err_checkout = PTS[0]
			for xf in range(len(PTS)):
				with open(str(PTS[xf])) as f:
					#try:
					rdata = json.load(f)
					print(f"[[green]NPX[/green]] Running purify on, Script: {PTM[xf]}")
					print(f"[[cyan]Purify[/cyan]] Running...")
					try:
						NPXM = rdata["PACKAGE_"]
						VER = rdata["VERSION"]
						STAT = rdata["DISABLE"]
						LOG = rdata["LOG"]
						AUTH = rdata["AUTHOR"]
					except KeyError:
						print("[[red]Purify[/red]] Error, this row must be in requirements.. (PACKAGE_, VERSION, DISABLE, LOG, AUHOR)")
						print(f"[[red]Purify[/red]] Moving to the next one, Remove the script or Modify it. We dont know which one!")
						continue
					try:
						CMD_ = rdata["CMD"]
						PYINT = None
					except KeyError:
						print("[[yellow]Purify[/yellow]] CMD Row is empty or not be displayed.. Checking [green]pyinstance[/green] (PYINT) row... ")
						CMD_ = None
						PYINT = rdata["PYINT"]
					if STAT != "false":
						print(f"[[yellow]Purify[/yellow]] {PTM[xf]} has been disabled, Next!")
						continue
					print(f"[[cyan]Purify[/cyan]] Running package with name of {NPXM} version {VER}")
					time.sleep(1)
					print(f'''[[cyan]Purify[/cyan]] Information about the creator of {NPXM}: \n[[yellow]Purify[/yellow]] Author: {AUTH["NAME"]} \n[[yellow]Purify[/yellow]] Email: {AUTH["EMAIL"]}''')
					time.sleep(1)
					print(f"[[cyan]NPX[/cyan]] Script seems stable...")
					print(f"[[yellow]Purify[/yellow]] Logs: {LOG}")
					if CMD_ == None and PYINT != None:
						print(f"[[cyan]Purify[/cyan]] Running pyint for internal execution... (FUNC ON INTERNAL)")
						rd = PYINT.split()
						if rd[0] == 'REQUEST' or rd[0] == 'REQUEST'.lower:
							try:
								METHOD = rd[1]
							except IndexError:
								print("[[red]Purify[/red]] METHOD for requests isnt specified which is critical...")
								print("[[red]Purify[/red]] Continuing to the next package...")
								continue
							try:
								URL = rd[2]
							except IndexError:
								print("[[red]Purify[/red]] URL for requesting isnt specified which is critical...")
								print("[[red]Purify[/red]] Continuing to the next package...")
								continue
							try:
								TODO = rd[3]
							except IndexError:
								print("[[red]Purify[/red]] What to do isnt specified which is critical...")
								print("[[red]Purify[/red]] Continuing to the next package...")
								continue
							try:
								PATH = rd[4]
							except IndexError:
								print("[[yellow]NPX[/yellow]] Path to file isnt specified which is great!")
							if METHOD == 'GET' or METHOD == 'GET'.lower:
								data = requests.get(URL)
								print(f"[[yellow]Purify[/yellow]] Running requests on {URL}")
								if TODO == 'PRT_STATUS':
									print("[[yellow]Purify[/yellow]] Logs: Server status,", data.ok)
								elif TODO == 'PRINT_TXT_TO_FILE':
									print("[[yellow]Purify[/yellow]] Logs: Retrieving text to file from server... [BETA CANNOT USE IT NOW...]")
								elif TODO == 'PRINT_TXT':
									print("[[green]Purify[/green]] Here comes a nuke requests text... ")
									print(data.text)
								else:
									print("[[red]Purify[/red]] TODO Function isnt match!")
									print("[[red]Purify[/red]] Continuing to the next package...")
									continue
							elif METHOD == 'POST' or METHOD == 'POST'.lower:
								pass
						print(f"[[yellow]Purify[/yellow]] Package successfuly to launch... Moving to next package")
						INST += 1
					elif CMD_ != None and PYINT == None:
						print(f"[[green]Purify[/green]] CMD row comand detected without pyinstance which is good! ")
						print(f"[[yellow]NPX[/yellow]] Running commands available...")
						try:
							os.system(CMD_)
						except Exception as e:
							print(f"[[red]CMD[/red]] Failed to launch, error: {e}. Next package...")
							continue
						print(f"[[yellow]Purify[/yellow]] Package successfuly to launch/install... Moving to next package")
						INST += 1
						#except Exception as e:
						#	print(f"[[purple]NPX[/purple]] Script: {PTM[xf]}, Error: {e}. (*)!, Skipping.. [[red]=====[/red]]")
					continue
		except IndexError:
			print("[[red]NPX[/red]] There is no script available")
		print(f"[[yellow]NPX[/yellow]] Done.. ({INST} Installed packages ).. Happy hacking..")
