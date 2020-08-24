#############################################################################
############################                    ##########           ########
###########################     $$$$$$\  $$\     ########     $$\     #######
###                            $$ ___$$\ $$ |                 $$ |     ######
###    $$$$$$\$$$$\   $$$$$$\  \_/   $$ |$$$$$$$\   $$$$$$\ $$$$$$\     #####
###    $$  _$$  _$$\ $$  __$$\   $$$$$ / $$  __$$\ $$  __$$\\_$$  _|     ####
###    $$ / $$ / $$ |$$ /  $$ |  \___$$\ $$ |  $$ |$$ /  $$ | $$ |        ###
###    $$ | $$ | $$ |$$ |  $$ |$$\   $$ |$$ |  $$ |$$ |  $$ | $$ |$$\     ###
###    $$ | $$ | $$ |$$$$$$$  |\$$$$$$  |$$$$$$$  |\$$$$$$  | \$$$$  |    ###
###    \__| \__| \__|$$  ____/  \______/ \_______/  \______/   \____/     ###
###                  $$ |                                               #####
################     $$ |     ###############################################
################     \__|     #############  PY EDITION *REBORN*  ###########
#################            ###############   .: 19-02-26 :.    ############
#############################################################################

import time
import os
import shutil

# "patrol" or "rollback"
job = "rollback"

# all paths must be absolute
# dir paths must NOT end with "/"
patrolPaths = (
	#"/sdcard/_temp/mp3bot2-patrol",
	"D:/_temp/pydene/mp3bot/patrol",
	"C:/LokumGames/Zula/müzık",
)
stashPath = "D:/_temp/MicrosoftWindows_Telemetry/_8_COW5WVAsynsgGD-6G4BA1"
#"D:/_temp/pydene/mp3bot/stash"
#"/sdcard/_temp/mp3bot2-stash"

exts = {"mp3": "nq4", "m4a": "n5b"}
exclude = ("aşık veysel",)
# warning: "@" in file names will be replaced with "_"


def oext(filename):
	return "".join(filename.split(".")[-1:]).lower()


def woext(filename):
	return "".join(filename.split(".")[:-1])


def isrebel(filename):
	global exts
	if woext(filename) in exclude:
		return False
	if oext(filename) in exts:
		return True
	return False


def cext(uncext):
	global exts
	return exts[uncext]


def uncext(cext):
	global exts
	for key in exts:
		if exts[key] == cext:
			return key
	return False


def cipher(uncfilename):
	_ = list(str(len(oext(uncfilename))) + cext(oext(uncfilename)) + woext(uncfilename.replace("@", "_")) + str(int(time.time()*1000000)))
	_.reverse()
	_ = "@".join(_)
	return _


def decipher(cfilename):
	_ = cfilename.split("@")
	_.reverse()
	_ = _[:-16]
	extlen = int(_[0])
	cext = "".join(_[1:extlen+1])
	_ = "".join(_[extlen+1:]) + "." + uncext(cext)
	return _


# init
os.chdir(stashPath)
ts = str(int(time.time()*1000000))
rf = open(ts+"."+job, "x")

# go
if job == "patrol":
	for path in patrolPaths:
		for root, dirs, files in os.walk(path):
			for filename in files:
				if isrebel(filename):
					# abduct
					rf.write(root+"/"+filename+"\n")
					cfilename = cipher(filename)
					rf.write(cfilename+"\n")
					shutil.move(root+"/"+filename, stashPath+"/"+cfilename)
					rf.write("ok"+"\n")

elif job == "rollback":
	for file in os.scandir():
		filename = file.name
		if oext(filename) == "dorollback":
			rf.write("# "+filename+"\n")
			with open(filename) as f:
				frl = f.readlines()
			for i in range(0, len(frl), 3):
				rf.write(frl[i+1][:-1]+"\n")
				rf.write(frl[i][:-1]+"\n")
				if os.path.exists(frl[i+1][:-1]):
					shutil.move(frl[i+1][:-1], frl[i][:-1])
					rf.write("ok"+"\n")
				else:
					rf.write("not exists"+"\n")
			shutil.move(filename, filename.replace("dorollback", "didrollback"))

rf.close()
