import maya.cmds as mc 
   
def bakeToSkeleton(): 
    #Set up selection 
    selection = mc.ls(sl = True)
     
    mc.select(cl=True) 
    jointList = []
    locList = [] 
    duplicateList = [] 
    rootJoint = "rootJoint"
       
    #Create and attach Skeleton to meshes 
    if mc.objExists("rootJoint")==False: 
        rootJoint = "rootJoint"
        mc.joint(n=rootJoint, p=(0, 0, 0)) 
        mc.select(cl=True) 
 
    for selected in selection: 
        if  "|" in selected: 
            nice_name = selected.split("|") 
            nice_name = nice_name[1] 
        else: 
            nice_name = selected 
    
        locName = nice_name + "_Loc"
        jointName = nice_name + "_joint"
        mc.joint(n=jointName, p=(0, 0, 0)) 
        mc.parent(jointName, rootJoint) 
        mc.spaceLocator(n=locName, p=(0, 0, 0)) 
        mc.pointConstraint(selected,locName) 
        mc.orientConstraint(selected,locName) 
        mc.scaleConstraint(selected,locName) 
        locList.append(locName)
        jointList.append(jointName) 
        mc.select(cl=True) 
         
    #Bake Animation to joints and remove constraints 
    animStartTime = mc.playbackOptions(q=True, minTime=True) 
    animEndTime = mc.playbackOptions(q=True, maxTime=True) 
    currentFrame = animStartTime
     
     
    while(currentFrame <= animEndTime):
        i = 0
        while(i < len(locList)):
            currentT = mc.getAttr(locList[i] + ".translate")
            currentR = mc.getAttr(locList[i] + ".rotate")
            currentS = mc.getAttr(locList[i] + ".scale")
            mc.setKeyframe(jointList[i], at = "translateX", v = currentT[0][0])
            mc.setKeyframe(jointList[i], at = "translateY", v = currentT[0][1])
            mc.setKeyframe(jointList[i], at = "translateZ", v = currentT[0][2])
            mc.setKeyframe(jointList[i], at = "rotateX", v = currentR[0][0])
            mc.setKeyframe(jointList[i], at = "rotateY", v = currentR[0][1])
            mc.setKeyframe(jointList[i], at = "rotateZ", v = currentR[0][2])
            mc.setKeyframe(jointList[i], at = "scaleX", v = currentS[0][0])
            mc.setKeyframe(jointList[i], at = "scaleY", v = currentS[0][1])
            mc.setKeyframe(jointList[i], at = "scaleZ", v = currentS[0][2])
             
            i += 1
             
        mc.currentTime(currentFrame, e = True)
        currentFrame += 1
 
    #Duplicate and attach mesh to joints 
    i = 0
    while i<len(selection): 
           
        if "|" in selection[i]: 
            nice_dup_name = selection[i].split("|") 
            nice_dup_name = nice_dup_name[1] 
        else: 
            nice_dup_name = selection[i] 
               
        dupName = nice_dup_name + "_baked"
        #mc.duplicate(selection[i], n= dupName) 
        shapes = mc.listRelatives(selection[i], s = True)
        tmp = mc.instance(shapes[0])
        mc.duplicate(tmp, n=dupName)
        mc.delete(tmp)
 
 
        mc.parent(dupName, world = True)
        mc.makeIdentity(apply = True)
        duplicateList.append(dupName) 
        mc.select(dupName, jointList[i]) 
        mc.skinCluster(toSelectedBones=True) 
        i+=1
       
    #Collect and clean up scene
    for i in locList:
        mc.delete(i)     
    mc.group("rootJoint", duplicateList, n="skinned_once_animate_debris") 
    #mc.setAttr("Baked_Simulation_Contents.sz",keyable = False,lock=True, channelBox = False) 
    #mc.setAttr("Baked_Simulation_Contents.sy",keyable = False,lock=True, channelBox = False) 
    #mc.setAttr("Baked_Simulation_Contents.sx",keyable = False,lock=True, channelBox = False) 
    mc.setAttr("Baked_Simulation_Contents.tz",keyable = False,lock=True, channelBox = False) 
    mc.setAttr("Baked_Simulation_Contents.ty",keyable = False,lock=True, channelBox = False) 
    mc.setAttr("Baked_Simulation_Contents.tx",keyable = False,lock=True, channelBox = False) 
    mc.setAttr("Baked_Simulation_Contents.rz",keyable = False,lock=True, channelBox = False) 
    mc.setAttr("Baked_Simulation_Contents.ry",keyable = False,lock=True, channelBox = False) 
    mc.setAttr("Baked_Simulation_Contents.rx",keyable = False,lock=True, channelBox = False) 
    for i in selection:
        mc.hide(i)
        print i 
    print "Baked Animation To Skeleton Conversion Done"
   
bakeToSkeleton()
