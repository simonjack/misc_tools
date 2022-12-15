import maya.cmds as mc
   

def get_texture_name(objs):
    absolute_shaders= []
    shaders = []

    for item in objs:
        shd = mc.listConnections(mc.listHistory(item, f=1), type = 'lambert')
        absolute_shaders.append(shd)    

    for shd in absolute_shaders:
        if shd not in shaders:
            shaders.append(shd)

    if len(shaders)>1:        
        mc.confirmDialog(title='Confirm', message='run Shader Cleanup and try again!', button=['OK'], defaultButton='OK', dismissString='OK')        

    elif len(shaders) == 1:
        abs_shader = str(shaders[0])
        texture_name = mc.listConnections(str.split(abs_shader,"'")[1] + '.color')
        texture_path = mc.getAttr(texture_name[0] + '.fileTextureName')
        texture_file = texture_path.split('/')[-1].split('.')[0]        
        if '_colour' in texture_file:
            texture_file = texture_file.split('_colour')[0]            
        else:
            pass
    return texture_file, abs_shader
    
def dumb_combine():
    meshes = mc.ls(sl = True)
    for m in meshes:
        mc.delete(m, constructionHistory = True)
        
    pnt_full = mc.listRelatives(meshes[0], fullPath = True)[0]
    pnt = mc.listRelatives(meshes[0], parent = True)
    target_path =  str.replace(str.split(str(pnt_full[0]), str(pnt[0]))[0],"|", "")
    target_path = str.split(str(pnt_full), "|")[1]
    if len(target_path) == 0:
        target_path =  str.split(str(pnt_full[0]), "|")[1]
    else:
        pass
    
    
    
    combined_mesh = mc.polyUnite(meshes, n = 'testCombine')
    mc.parent(combined_mesh, pnt)  
    
    combined = mc.ls(sl = True)
    for c in combined:
        mc.delete(c, ch = True)
        shd = str.split(get_texture_name(c.split("'"))[1], "'")[1]
        print shd
        sg = [x for x in mc.listConnections(shd, d = True) if mc.nodeType(x) == 'shadingEngine'][0]
        mc.sets(c, e = True, forceElement = sg)
        mc.setAttr(c + '.doubleSided', 0)        
        mc.rename(c, get_texture_name(mc.ls(sl = True))[0])
    return meshes

def cleanup():
    check = dumb_combine()
    for c in check:
        if mc.nodeType(c) == 'transform':
            mc.delete(c)

cleanup()
