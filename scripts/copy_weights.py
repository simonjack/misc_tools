import maya.cmds as mc
import maya.mel as mel

def copyWeights(source, target):
    source_list = mc.listRelatives(source, c = True)
    target_list = mc.listRelatives(target, c = True)
    
    if len(source_list) != len(target_list):
        print "source and target are different"
    else:
        for idx, i in enumerate(source_list):
            mc.select(source_list[idx])
            mc.select(target_list[idx], add = True)
            mel.eval('copySkinWeights  -noMirror -surfaceAssociation closestPoint -uvSpace uv uv -influenceAssociation closestJoint -influenceAssociation oneToOne;')
            

sl = mc.ls(sl = True)
if len(sl) == 2:
	copyWeights(sl[0], sl[1])
