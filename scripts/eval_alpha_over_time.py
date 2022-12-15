import maya.cmds as mc
import pymel.core as pm
import maya.mel as mel

def evalAlpha():

    midLocT = pm.xform('loc_mid_alphaBox', q=True, t=True, ws=True)
    midLocTy = round(midLocT[1], 4)
    #print 'midLocTy is ' + str(midLocTy)
    
    topLocT = pm.xform('loc_top_alphaBox', q=True, t=True, ws=True)
    maxYDistance = round(topLocT[1] - midLocTy, 4)
    #print 'maxYDistance is ' + str(maxYDistance)
    
    jntSel = pm.ls(sl=True)
    for j in jntSel:
        jntT = pm.joint( j, q=True, p=True)
        jntTy = round(jntT[1], 4)
        #print 'jntTy is ' + str(jntTy)
    
        distanceY = abs(jntTy - midLocTy)
        #print 'distanceY is ' + str(distanceY)
        alphaValue = round(abs((distanceY/maxYDistance)-1), 4)
        newAlphaValue = pm.setAttr(j + '.Alpha', alphaValue)
        

        
    

def evalAlp():
    time = mc.currentTime(q = True)
    for i in range(0, int(time)):
        evalAlpha()
        alVal = mc.getAttr('btm1.Alpha' )
        print alVal
        mc.currentTime((i+1), edit = True)

aPlayBackSliderPython = maya.mel.eval('$tmpVar=$gPlayBackSlider')
mc.timeControl( aPlayBackSliderPython,edit=True,pressCommand='evalAlp()')
