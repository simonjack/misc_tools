import maya.api.OpenMaya as om
import maya.cmds as mc


def getClosestVertex(targetMesh, pos):
    mVector = om.MVector(pos)

    obj1 = mc.ls(selection=True)[0]
    selectionList = om.MSelectionList()
    selectionList.add(targetMesh)
    dPath = selectionList.getDagPath(0)
    mMesh = om.MFnMesh(dPath)
    ID = mMesh.getClosestPoint(om.MPoint(mVector), space=om.MSpace.kWorld)[1]
    list = mc.ls(mc.polyListComponentConversion(targetMesh + '.f[' + str(ID) + ']', ff=True, tv=True), flatten=True)
    d = mVector - om.MVector(mc.xform(list[0], t=True, ws=True, q=True))
    smallestDist2 = d.x * d.x + d.y * d.y + d.z * d.z
    closest = list[0]
    for i in range(1, len(list)):
        d = mVector - om.MVector(mc.xform(list[i], t=True, ws=True, q=True))
        d2 = d.x * d.x + d.y * d.y + d.z * d.z
        if d2 < smallestDist2:
            smallestDist2 = d2
            closest = list[i]
    return closest


def snapPosition():
    vertx = mc.ls(selection=True, fl=True)[:-1]
    source_object = mc.ls(selection = True, fl = True)[-1]

    for vert in vertx:
        position = mc.xform(vert, q=True, ws=True, t=True)

        nearVert = getClosestVertex(source_object, position)

        mc.xform(nearVert, ws=True, t=(position[0], position[1], position[2]))


snapPosition()
