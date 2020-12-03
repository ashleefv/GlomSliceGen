#import CompuCell
import numpy as np
#from Circle import CircleDraw
import types

##########################################################
#
# Intstructions:
#
# Place this file in the same folder as your CC3D code.
# Then, add this import to the top of your file:
#
# from CellGeom import *
# 
# Use either AttachCreateBlob(obj) or AttachCreateCircleCell(obj)
# to add these functions to your steppables
#
# Ex.:
# class CellInitializer(SteppableBasePy):
#	 def __init__(self,_simulator,_frequency=1):
# 		SteppableBasePy.__init__(self,_simulator,_frequency)
# 		AttachCreateBlob(self)
# 		AttachCreateCircleCell(self)

def CreateBlob(self, blobDiameter, blobCenter, cellWidth, cellType, fill = 1):
	blobCellWidth = blobDiameter/cellWidth
	print(blobCellWidth)
	blobPoints = np.where(CircleDraw(blobCellWidth,fill))
	print(blobPoints)
	circleOffset = [np.floor(x-blobDiameter/2.0) for x in blobCenter]
	cellsToAdd = []
	for i in range(len(blobPoints[0])):
		cellExtents = (circleOffset[0] + cellWidth*blobPoints[0][i], circleOffset[0] + cellWidth*blobPoints[0][i] +cellWidth,
			circleOffset[1] + cellWidth*blobPoints[1][i], circleOffset[1] + cellWidth*blobPoints[1][i] +cellWidth)
		
		self.cellField[cellExtents[0]:cellExtents[1], cellExtents[2]:cellExtents[3], 0] = self.newCell(cellType)
		
def AttachCreateBlob(obj):
#Pass your steppable to this function to add the CreateBlob method to it
	obj.CreateBlob = types.MethodType(CreateBlob, obj)



def CreateCircleCell(self, cellDiameter, cellCenter, cellType, overwrite=0):
	cellPoints = np.where(CircleDraw(cellDiameter,1))
	for i in range(len(cellPoints[0])):
		cellPoints[0][i] = np.floor(cellPoints[0][i]-cellDiameter/2.0) + cellCenter[0]
		cellPoints[1][i] = np.floor(cellPoints[1][i]-cellDiameter/2.0) + cellCenter[1]

		
		
	cell = self.newCell(cellType)
	for i in range(len(cellPoints[0])):
		if overwrite:
			self.cellField[int(cellPoints[0][i]), int(cellPoints[1][i]), 0] = cell
		else:
			if self.cellField[int(cellPoints[0][i]), int(cellPoints[1][i]), 0] == None:
				self.cellField[int(cellPoints[0][i]), int(cellPoints[1][i]), 0] = cell
				
	return cell
	
def AttachCreateCircleCell(obj):
#Pass your steppable to this function to add the CreateCircleCell method to it
	obj.CreateCircleCell = types.MethodType(CreateCircleCell, obj)
	
def CircleDraw(diameter, fill):
#Uses the midpoint circle algorithm with a few tweeks. Namely, it can use a odd valued diameter.
#See https://en.wikipedia.org/wiki/Midpoint_circle_algorithm for more (this code is based on the code in the C example).
    radius = (diameter+1)/2.0
    
    
    
    output = np.zeros((int(radius*2-1), int(radius*2-1)))
    
    x = np.ceil(radius - 1)
    y = 0
    dx = 1
    dy = 1
    err = dx - int(radius * 2)
    x0 = radius - 1
    y0 = radius - 1
    
    while(x >= y):
        output[int(np.floor(x0 + x)), int(np.floor(y0 + y))] = 1
        output[int(np.floor(x0 + y)), int(np.floor(y0 + x))] = 1
        output[int(np.ceil(x0 - y)), int(np.floor(y0 + x))] = 1
        output[int(np.ceil(x0 - x)), int(np.floor(y0 + y))] = 1
        output[int(np.ceil(x0 - x)), int(np.ceil(y0 - y))] = 1
        output[int(np.ceil(x0 - y)), int(np.ceil(y0 - x))] = 1
        output[int(np.floor(x0 + y)), int(np.ceil(y0 - x))] = 1
        output[int(np.floor(x0 + x)), int(np.ceil(y0 - y))] = 1
        
        if(err <= 0):
            y += 1
            err += dy
            dy += 2
            
        if(err > 0):
            x -= 1
            dx += 2
            err += (-radius * 2) + dx
            
    if fill:
        for i in range(len(output)):
            points = np.where(output[i,:])[0]
            if len(points) > 2:
                continue
            for j in range(points[0],points[1]):
                output[i,j] = 1
                
    return output