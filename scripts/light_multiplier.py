#import maya.standalone as ms
#ms.initialize(name = 'Python')
import maya.cmds as mc
import maya.mel as mel
import os
import re
mc.loadPlugin("GGGMayaToolUpdaterPlugin2018.mll")
#set project
def set_project(project):    
    cur_proj = mc.workspace(active = True, q = True)
    if cur_proj == project:
        pass
    else:
        mel.eval('setProject \"'+ project +'\"')
 
#DoAction
def lightIntensityMultiplier(folder, multiplier):
    for root, dirs, files in os.walk(folder, topdown = False):
        for name in files:         
            if name.endswith('.mb'):               
                mc.file(os.path.join(root, name), o = True, iv = True, f = True)
                sel = mc.ls(type = 'light')
                if sel:
                    for item in sel:
                        anim_curve = mc.listConnections(item + '.intensity' )
                        if anim_curve:
                            for c in anim_curve:
                                if re.search('.intensity*', c):
                                    mc.scaleKey(item + '.intensity', valueScale = multiplier)
                        else:
                            cur_int = mc.getAttr(item + '.intensity')
                            mc.setAttr(item + '.intensity', cur_int*multiplier)
                        mc.file(save = True, f = True)
   
 
set_project('C:/SVNs/art/')
lightIntensityMultiplier('C:/SVNs/art/Models/Terrain/PrisonDungeon', 5)
