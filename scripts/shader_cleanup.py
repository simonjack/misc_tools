import os
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
    pnt = mc.ls(sl = True, long = True)[0].split('|')[1:-1]
    combined_mesh = mc.polyUnite(meshes, n = 'testCombine')       
    
    try:
        if len(pnt)>1:
            common_ancestor =  pnt[-1]
        else:
            common_ancestor = pnt[0]
        mc.parent(combined_mesh, common_ancestor)
    except IndexError:
        pass
        
    
    for m in meshes:
        try:
            mc.delete(m)
        except ValueError:
            pass
    
    mc.delete(combined_mesh[0], ch = True)
    shd = get_texture_name(mc.ls(sl = True))[1].split("'")[1]
    sg = [x for x in mc.listConnections(shd, d = True) if mc.nodeType(x) == 'shadingEngine'][0]
    mc.rename(combined_mesh[0], get_texture_name(mc.ls(sl = True))[0])
    mc.sets(mc.ls(sl = True)[0], e = True, forceElement = sg)
    
          

    
dumb_combine()
