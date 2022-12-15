import maya.cmds as mc
 
 
def texPathChange(pathToCull): 
	sel = mc.ls(textures = True) 
	for i in sel:
		texPath = mc.getAttr(i + '.fileTextureName')
		finalPath = str.replace(str(texPath), pathToCull, "")
		mc.setAttr(i + ".fileTextureName", finalPath, type = "string")
 
 
texPathChange("C:/SVN/art/")
