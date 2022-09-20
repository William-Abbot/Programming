import zipfile
import os
import time

directory = 'E:\\Documents\\My Games\\Terraria\\Worlds'
file1 = directory + '\\The_Faraway_Highland.wld'
file2 = directory + '\\The_Faraway_Highland.wld.bak'
datestr = time.strftime("%m"+"_"+"%d"+"_"+"%Y")
filename = "terraria_world" + datestr + ".zip"


newZip = zipfile.ZipFile(filename, 'w')
newZip.write(file1)
newZip.write(file2)
