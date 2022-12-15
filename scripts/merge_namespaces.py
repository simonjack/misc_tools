import maya.cmds as mc
import pymel.core as pymel
            

def MergeNameSpaces():
    mc.select(all = True)
    objects = mc.ls(sl = True)
    mc.select(clear = True)

    children = []

    for object in objects:
        children.append(mc.listRelatives(object, ad = True))

    for child in children:
        if child is None:
            pass
        else:
            for item in child:
                if ':' in item:
                    abs_name = str.split(str(item), ':')[-1]
                    try:
                        mc.rename(item, abs_name)
                    except RuntimeError:
                        pass
    for object in objects:
        if ':' in object:
            abs_name = str.split(str(object), ':')[-1]
            try:
                mc.rename(object, abs_name)
            except RuntimeError:
                pass

    ''' 
    Find all namespaces in scene and remove them.
    Except for default namespaces
    '''

    # Get a list of namespaces in the scene
    # recursive Flag seraches also children
    # internal Flag excludes default namespaces of Maya
    namespaces = []
    for ns in pymel.listNamespaces( recursive  =True, internal =False):
        namespaces.append(ns)
        
    # Reverse Iterate through the contents of the list to remove the deepest layers first
    for ns in reversed(namespaces):
        currentSpace = ns
        pymel.namespace(removeNamespace = ns, mergeNamespaceWithRoot = True)
        print currentSpace.split(':')[-1] + ' has been merged with root'

    # Empty the List
    namespaces[:] = []
   

MergeNameSpaces()
