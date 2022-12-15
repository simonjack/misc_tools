import maya.cmds as mc

class centerPiv():
    
    def __init__(self, *args):
        if (mc.window('centerPivotUI', exists=True)):
            mc.deleteUI('centerPivotUI')
        GGGShaderWindow = mc.window('centerPivotUI', title='centerPivotUI', wh = [100,100])
        
        mc.rowColumnLayout()
        
        self.inputData = mc.textField()
        flattenPiv = mc.button(label = 'Flatten Pivot', c = self.centerPivotFn)
        
        mc.setParent("..")
        mc.textField(self.inputData, edit = True, enterCommand = (self.centerPivotFn), aie = True)
        
        mc.showWindow()
        


    def centerPivotFn(self, *args):
        
        datafromUI = mc.textField(self.inputData, q = True, tx = True)
        
        
        try:
            nosplit = mc.select(datafromUI + '*')
            
        except ValueError:
            mc.confirmDialog( title='Confirm', message='Found no ' + datafromUI, button=['OK'], defaultButton='OK', dismissString='OK' )
            

        sel = mc.ls(selection = True)
        print sel
        
        if len(sel)>0:
            for i in sel:
                print i
                pivpos = mc.xform(i, q = 1, ws = 1, rp = 1)
                #print pivpos
    
                mc.move(pivpos[0], 0, pivpos[2], i+".scalePivot",i+".rotatePivot", absolute=True)
            
        else:
            mc.confirmDialog( title='Confirm', message='Found no ' + datafromUI, button=['OK'], defaultButton='OK', dismissString='OK' )
            
        if (mc.window('centerPivotUI', exists=True)):
            mc.evalDeferred(lambda:mc.deleteUI('centerPivotUI'))
        

centerPiv()
