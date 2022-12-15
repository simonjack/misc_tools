import maya.cmds as mc
import maya.mel as mel

def locToasset():
    asset = mc.ls(selection = True)

    
    for idx, i in enumerate(asset):
        print i
        asset_loc = mc.xform(i,query=True,t=True,worldSpace=True)
        loc = mc.spaceLocator(n = 'fixed_Loc_' +  i )
        mc.parentConstraint(i, loc)
        mc.select(loc)
        mc.delete( cn=True )
        #mel.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1')
        
        mc.select(cl = True)


def assetToloc():
    
    loc = mc.ls(selection = True)
    print len(loc)
    
    if len(loc) == 0:
        print "No Locators found for the selected objects"

    else:
        for i in loc:
            try:
                assetName = i.split("fixed_Loc_")[1]
            except ValueError:
                print "no object by the name " + assetName + " found"

            mc.select(assetName)
            if assetName:
                mc.parentConstraint(i, assetName)
                mc.select(assetName)
                mc.delete(cn = True)
                mc.select(cl = True)

        
            
        
assetToloc()
