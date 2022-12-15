import maya.cmds as mc
import maya.mel as mel
 
sel = mc.ls(selection = True)
 
 
if(mel.eval('objExists DoubleSided')):
    for i in sel:
        dbs = mc.getAttr(i + '.doubleSided')
       
        if dbs:
            mc.select(i, r = True)
            mc.editDisplayLayerMembers('DoubleSided', i)
        else:
            pass
else:
    layer = mel.eval('createDisplayLayer -name "DoubleSided" -number 0 -empty;')
   
    for i in sel:
       
        dbs = mc.getAttr(i + '.doubleSided')
       
        if dbs:
            mc.select(i, r = True)
            mc.editDisplayLayerMembers('DoubleSided', i)
        else:
            pass
            
            
            
if mc.editDisplayLayerMembers('DoubleSided', q = True) is None:
    mel.eval('delete DoubleSided;')
    
else:
    pass
