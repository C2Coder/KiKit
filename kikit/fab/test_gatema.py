import os
import shutil

gerberdir = "/home/c2coder/Codes/RoboCamp/RP-HUB75/hw/panel/gerber"
outputdir = "/home/c2coder/Codes/RoboCamp/RP-HUB75/hw/panel"

ext_list = [("-CuTop.gtl", ".top"), ("-CuBottom.gbl", ".bot"), ("-MaskTop.gts", ".smt"), ("-MaskBottom.gbs", ".smb"), ("-NPTH.drl", ".mill"), ("-PTH.drl", ".pth"), ("-SilkTop.gto", ".plt"), ("-SilkBottom.gbo", ".plb"), ("-EdgeCuts.gm1", ".dim")]
for f in os.listdir(gerberdir):
    unneded = True
    # mayby drrilling should be using the map - not tested
    for old, new in ext_list:
        if f.endswith(old):
            unneded = False
            newname = f.replace(old, new)
            os.rename(os.path.join(gerberdir, f), os.path.join(gerberdir, newname))
            break 
    if unneded:
        os.remove(os.path.join(gerberdir, f))  # remove unneeded files
    

shutil.make_archive(os.path.join(outputdir, "gerbers"), "zip", outputdir, "gerber")
