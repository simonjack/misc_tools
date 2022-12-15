def UI():
    buttonWidth = 200
    buttonHeight = 100
    winID = 'averageVertices'

    if mc.window(winID, exists=True):
        mc.deleteUI(winID)
    mc.window(winID)
    mc.rowColumnLayout()

    # Add controls into this Layout
    # whatUSay = cmds.textField()
    mc.button(label='X', command='printTxtField(whatUSay)', width=buttonWidth, height=buttonHeight,
            highlightColor=(0, 1, 0), c='averagePosition("X")')
    mc.button(label='Y', command='printTxtField(whatUSay)', width=buttonWidth, height=buttonHeight, c= 'averagePosition("Y")')
    mc.button(label='Z', command='printTxtField(whatUSay)', width=buttonWidth, height=buttonHeight, c = 'averagePosition("Z")')
    mc.showWindow()
    
    
def averagePosition(axes):
   
  if axes == 'X':
     axis = 0
  elif axes == 'Y':
     axis = 1
  elif axes == 'Z':
     axis = 2
  sel = mc.ls(selection = True, fl = True)

  vtxWorldPosition = []
  vtxID = []    



  for i in sel :
      
        curPointPosition = mc.pointPosition(i)
        vtxWorldPosition.append( curPointPosition )
        vtxID.append(i)




  vertexPosition, vtx_id = getVtxPos()

  print vertexPosition
  #vtxIndexList = mc.getAttr( shape + ".vrts", multiIndices=True )


  avgPos = sum([p[axis] for p in vtxWorldPosition]) / len(vtxWorldPosition)
  print avgPos
  for idx, i in enumerate(vtxWorldPosition):
     #print vtx_id[idx]   
     i.remove(i[axis])
     i.insert(axis, avgPos)
     print i

     mc.xform(vtxID[idx] , ws = 1, t = i)

UI()
