from cc3d.core.PySteppables import *
#import CompuCell
import sys
import numpy as np
# from Circle import CircleDraw
from CellGeom import *

#from PySteppablesExamples import MitosisSteppableBase



class ConstraintInitializerSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)
    def start(self):
        return
        
        
        
        
        
        #self.stopSimulation()
            
        
            
        
        
        

class GrowthSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)
    def step(self,mcs):
        for cell in self.cellList:
            if cell.type == self.MESANGIAL:
                cell.targetVolume+=0
                cell.targetSurface+=0
    # alternatively if you want to make growth a function of chemical concentration uncomment lines below and comment lines above        
        # field=CompuCell.getConcentrationField(self.simulator,"PUT_NAME_OF_CHEMICAL_FIELD_HERE")
        # pt=CompuCell.Point3D()
        # for cell in self.cellList:
            # pt.x=int(cell.xCOM)
        
            
            # pt.y=int(cell.yCOM)
            # pt.z=int(cell.zCOM)
            # concentrationAtCOM=field.get(pt)
            # cell.targetVolume+=0.01*concentrationAtCOM  # you can use here any fcn of concentrationAtCOM    
           
          
# class MitosisSteppable(MitosisSteppableBase):
    
#     def __init__(self,_simulator,_frequency=1):
#         MitosisSteppableBase.__init__(self,_simulator, _frequency)
#         self.cellTargetVolume=25
#         self.cellLambdaVolume=3.0
#         self.cellTargetSurface = 20
#         self.cellLambdaSurface = 2.0
        
#     def start(self):
#         self.starting = 1
#         for cell in self.cellList:
#             if cell.type == self.PODOCYTEBODY:
#                 pass
#                 #self.divideCellOrientationVectorBased(cell, 1, 0, 0)
#         self.starting = 0
    
#     def step(self,mcs):
#         # print "INSIDE MITOSIS STEPPABLE"
#         cells_to_divide=[]
#         for cell in self.cellList:
#             if cell.volume>50 and cell.type == self.MESANGIAL:
                
#                 cells_to_divide.append(cell)
            
            
#         #for cell in cells_to_divide:
#             #self.divideCellOrientationVectorBased(cell, 1, 0, 0)  
            
            
#             # self.divideCellRandomOrientation(cell)
#             # self.divideCellOrientationVectorBased(cell,1,0,0)                 # this is a valid option
#             # self.divideCellAlongMajorAxis(cell)                               # this is a valid option
#             # self.divideCellAlongMinorAxis(cell)                               # this is a valid option

#     def updateAttributes(self):
#         if self.starting:
            
#             self.cloneParent2Child()
#             self.childCell.type = self.PODOCYTEFOOT
#             cID = self.parentCell.clusterId 
#             reassignIdFlag=self.inventory.reassignClusterId(self.childCell,cID)
            
#             self.childCell.targetVolume = self.cellTargetVolume/2
#             self.parentCell.targetVolume = self.cellTargetVolume/2
            
            
#             self.childCell.targetVolume = self.cellTargetSurface/2
#             self.parentCell.targetVolume = self.cellTargetSurface/2
            
#             return
        
#         self.parentCell.targetVolume /= 2.0 # reducing parent target volume                 
#         self.cloneParent2Child()
        
        
        
class DeathSteppable(SteppableBasePy):
    def __init__(self,frequency=1):
        SteppableBasePy.__init__(self, frequency)
    def step(self,mcs):

        for cell in self.cellList:
            if cell.type==self.MESANGIAL and (cell.targetVolume - cell.volume) > 6:
                cell.targetVolume=0
                cell.lambdaVolume=100
    

        
        


#from PlayerPython import *
#import CompuCellSetup
from math import *


global numCapillaries 
numCapillaries = 6.0#Needs to be a float because division in Python 2 is stupid. 


# class CellInitializer(MitosisSteppableBase):class CellInitializer(SteppableBasePy):
    def __init__(self, frequency=1):
        MitosisSteppableBase.__init__(self, frequency)
        AttachCreateBlob(self)
        AttachCreateCircleCell(self)
        
        #Glomerulus body initialization variables
        self.glomerulusDiameter = 50
        self.glomerulusCenter = (50,50)
        self.cellWidth = 5
        
        #Parameters for placing capillaries
        self.numCapillaries = numCapillaries 
        self.diameterCapillaries = 12
        self.capillaryDistanceOffset = -2
        self.startTheta = np.pi/3.0
        self.endTheta = 5.0*np.pi/3.0
        
        #Podocyte thickness around capilaries in pixels
        self.numLayers = 4
        
        #Cell and capillary properties
        self.capTargetVolume = 70
        self.capLambdaVolume = 3.0
        self.capTargetSurface = 15
        self.capLambdaSurface =  5.0

        self.cellTargetVolume=25
        self.cellLambdaVolume=3.0
        self.cellTargetSurface = 20
        self.cellLambdaSurface = 2.0
        
        #FFP properties
        self.lambdaFFP = 10
        self.targetDistance = 4
        self.maxDistance = 12
        
        #
        self.numLayers = 4
        self.numCapillaries = numCapillaries
        
    def start(self):
        
         
        
        #Spawn mesangial cells and surrounding podocytes
        self.CreateBlob(self.glomerulusDiameter, self.glomerulusCenter, self.cellWidth, self.MESANGIAL,1)
        self.CreateBlob(self.glomerulusDiameter, self.glomerulusCenter, self.cellWidth, self.PODOCYTEBODY,0)
        
        
        self.CreateCapillaries()
        self.PlacePodocytesAroundCapillaries()    
#         self.LinkPodocytes()
        
        self.starting = 1
#         cellsToDivide = []
#         for cell in self.cellList:
#             if cell.type == self.PODOCYTEBODY:
#                 cellsToDivide.append(cell)
                
#         for cell in cellsToDivide:
#             self.divideCellOrientationVectorBased(cell, cell.xCOM - self.glomerulusCenter[0], cell.yCOM - self.glomerulusCenter[1], 0)
        
#         for compartments in self.clusters:
#             continueFlag = False
#             cellList = []
#             distancesSquared = []
#             for cell in compartments:
#                 if cell.type != self.PODOCYTEBODY:
#                     continueFlag = True
#                     break
#                 cellList.append(cell)
#                 distancesSquared.append((cell.xCOM - self.glomerulusCenter[0])**2 + (cell.yCOM - self.glomerulusCenter[1])**2)
                
#                 print cell.id
#             if continueFlag == True:
#                 continueFlag = False
#                 continue
            
#             if distancesSquared[0] < distancesSquared[1]:
                
#                 replacementCell1 = self.newCell(self.PODOCYTEBODY)
#                 replacementCell2 = self.newCell(self.PODOCYTEFOOT)
                
#                 cID = cellList[0].clusterId
#                 reassignIdFlag=self.inventory.reassignClusterId(replacementCell1,cID)
#                 reassignIdFlag=self.inventory.reassignClusterId(replacementCell2,cID)
                
#                 pixelList = self.getCellPixelList(cellList[0])
#                 for i in pixelList:
#                     pix = i.pixel
#                     self.cellField[pix.x, pix.y, pix.z] = replacementCell2
                    
#                 pixelList = self.getCellPixelList(cellList[1])
#                 for i in pixelList:
#                     pix = i.pixel
#                     self.cellField[pix.x, pix.y, pix.z] = replacementCell1    
                
                
                
                
# #                 cellList[0].type = self.PODOCYTEFOOT
                
#             else:
#                 replacementCell1 = self.newCell(self.PODOCYTEBODY)
#                 replacementCell2 = self.newCell(self.PODOCYTEFOOT)
                
#                 cID = cellList[0].clusterId
#                 reassignIdFlag=self.inventory.reassignClusterId(replacementCell1,cID)
#                 reassignIdFlag=self.inventory.reassignClusterId(replacementCell2,cID)
                
#                 pixelList = self.getCellPixelList(cellList[0])
#                 for i in pixelList:
#                     pix = i.pixel
#                     self.cellField[pix.x, pix.y, pix.z] = replacementCell1
                    
#                 pixelList = self.getCellPixelList(cellList[1])
#                 for i in pixelList:
#                     pix = i.pixel
#                     self.cellField[pix.x, pix.y, pix.z] = replacementCell2 
# #                 cellList[1].type = self.PODOCYTEFOOT
        
        
        
        self.starting = 0
            

        
            
        print("CellInitializer: This function is called once before simulation")
        
    def step(self,mcs):
#         self.stopSimulation()
        self.stop_simulation()
        
        
        
        return
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
        
        
    def CreateCapillaries(self):
        #This method creates the capilaries. 
        #First it identifies evenly spaces points in a circle around the center of the glomerulus and then creates a large circular cell in that position
        

        capillaryCenterDistance = self.glomerulusDiameter/2.0 - self.cellWidth + self.diameterCapillaries/2.0 - self.capillaryDistanceOffset
        
        #If we don't want a full circle, adjust the difference so the arange function will return a range that incluces endTheta
        if self.endTheta - 2*np.pi != self.startTheta and self.numCapillaries !=1:
            self.endTheta = (self.endTheta - self.startTheta)* (1 + 1/float(self.numCapillaries-1)) + self.startTheta
        
        self.thetas = np.arange(self.startTheta, self.endTheta, (self.endTheta - self.startTheta)/self.numCapillaries)
        #Here, pos y direction is theta = 0, theta increases CCW
        self.capillaryPositions = [[capillaryCenterDistance * -np.sin(i) + self.glomerulusCenter[0],
            capillaryCenterDistance * np.cos(i) + self.glomerulusCenter[1]] for i in self.thetas]


        self.capDict = {}
        for i in range(len(self.capillaryPositions)):
            #self.CreateBlob(diameterCapillaries, capillaryPositions[i], cellWidth, self.PODOCYTE, 0)
            self.capDict[self.CreateCircleCell(self.diameterCapillaries, self.capillaryPositions[i], self.CAPILLARY,1).id] = i
            

            
    def PlacePodocytesAroundCapillaries(self):
        
        for cell in self.cellListByType(self.CAPILLARY):
            pixelsToCheck = [] 
            pixelsToFill = []
            pixelBList = []
            
            cellPixelList = self.getCellPixelList(cell)
            print("cellPixelList :", cellPixelList)
            assert cellPixelList != None
            cellBPixelList = self.getCellBoundaryPixelList(cell)
            cellPixelList = self.getCellPixelList(cell)
#             capillaryId = [cell.id]
#             podoIds = []
            
            
            for i in cellBPixelList:
                pix = i.pixel
                pixelsToCheck.append(CompuCell.Point3D(pix.x+1, pix.y, pix.z))
                pixelsToCheck.append(CompuCell.Point3D(pix.x-1, pix.y, pix.z))
                pixelsToCheck.append(CompuCell.Point3D(pix.x, pix.y+1, pix.z))
                pixelsToCheck.append(CompuCell.Point3D(pix.x, pix.y-1, pix.z))
                
            for neighbor, commonSurfaceArea in self.getCellNeighborDataList(cell):
                if neighbor:
                    assert cell != None                                                           
                    assert cellPixelList != None
                    assert neighbor != None
                    
                    neighborPixelBList = self.getCellBoundaryPixelList(neighbor) 
 
                    for i in neighborPixelBList:
                        #i is not a Point3D, but an object that contains the Point3D we need as a property
                        pix = i.pixel
                        pixelsToCheck.append(CompuCell.Point3D(pix.x+1, pix.y, pix.z))
                        pixelsToCheck.append(CompuCell.Point3D(pix.x-1, pix.y, pix.z))
                        pixelsToCheck.append(CompuCell.Point3D(pix.x, pix.y+1, pix.z))
                        pixelsToCheck.append(CompuCell.Point3D(pix.x, pix.y-1, pix.z))
                            
                    assert pixelBList != None
                    
#                     for boundaryPixelTrackerData in pixelList:
#                         print "pixel of cell id=", cell.id, " type:", cell.type, " = ", boundaryPixelTrackerData.pixel, " number of pixels=", pixelList.numberOfPixels()
                    
                    
                    
                    neighbor.type = self.MESANGIAL
                    
                else:
                    pass
            
                
            print("num of pixels to check: ", len(pixelsToCheck))
            
            
        
            for pix in pixelsToCheck:
                contFlag = 0
                for markedPix in pixelsToFill:
                    if pix == markedPix:
                        contFlag = 1
                if contFlag:
                    continue
                if self.cellField[pix.x, pix.y, pix.z] == None:
                    pixelsToFill.append(pix)
                    
            layers = [pixelsToFill]
            
            podo = self.newCell(self.PODOCYTEBODY)
            
 
            for i in range(self.numLayers):
                
                if i == 0:
                    for pix in pixelsToFill:
                        self.cellField[pix.x, pix.y, pix.z] = podo
                    
                else:
                    layers.append([])
                    for pix in layers[i-1]:
                        if self.cellField[pix.x+1, pix.y, pix.z] == None:
                            self.cellField[pix.x+1, pix.y, pix.z] = podo
                            layers[i].append(CompuCell.Point3D(pix.x+1, pix.y, pix.z))
                        if self.cellField[pix.x-1, pix.y, pix.z] == None:
                            self.cellField[pix.x-1, pix.y, pix.z] = podo
                            layers[i].append(CompuCell.Point3D(pix.x-1, pix.y, pix.z))
                        if self.cellField[pix.x, pix.y+1, pix.z] == None:
                            self.cellField[pix.x, pix.y+1, pix.z] = podo
                            layers[i].append(CompuCell.Point3D(pix.x, pix.y+1, pix.z))
                        if self.cellField[pix.x, pix.y-1, pix.z] == None:
                            self.cellField[pix.x, pix.y-1, pix.z] = podo
                            layers[i].append(CompuCell.Point3D(pix.x, pix.y-1, pix.z)) 
            
            capNum = self.capDict[cell.id]
            
            if podo.volume > 1.35 * self.cellTargetVolume:
                numSplits = int(podo.volume/self.cellTargetVolume)
                podoPix = self.getCellPixelList(podo)
                pixAndTheta = []
                for j in podoPix:
                    pix = j.pixel
                    vec = CompuCell.Point3D(int(pix.x - self.capillaryPositions[capNum][0]), int(pix.y - self.capillaryPositions[capNum][1]), pix.z)
                    #pos x = 0  basis
                    thetaVec = np.arccos(float(vec.x)/np.sqrt(vec.y**2 + vec.x**2))
                    if vec.y < 0:
                        thetaVec = 2*np.pi - thetaVec
                    #converting to theta of Capillary COM to center of simulation =0 as a basis
                    thetaVec += - self.thetas[capNum] - 3.0 * np.pi/2.0
                    
                    while thetaVec<0:
                        thetaVec += 2*np.pi
                        
#                     print "theta: ", thetas[i]
#                     print "capillary position: ", capillaryPositions[i]
#                     print "pix pos: [", pix.x, ", ", pix.y, ", ", pix.z, "]"
#                     print "thetaVec: ", thetaVec
                    
                    pixAndTheta.append([pix, thetaVec])
                    
                pixAndTheta.sort(key = lambda element: element[1])
                
                #print "pixAndTheta: ", pixAndTheta
                
                sectionVol = int(podo.volume/(numSplits+1))
                for j in range(numSplits):
                    newPodo = self.newCell(self.PODOCYTEBODY)

                    for k in range(sectionVol):
                        pix = pixAndTheta[j*sectionVol + k][0]
                        self.cellField[pix.x, pix.y, pix.z] = newPodo

            
                    
            print("num of pixels to fill: ", len(pixelsToFill))
            
            
    def LinkPodocytes(self):
        
        podocyteList = list(self.cellListByType(self.PODOCYTEBODY))
        distances = np.full((len(podocyteList), len(podocyteList)), -1)
        #print np.version.version
        for i in range(len(podocyteList)):
            for j in range(i+1, len(podocyteList)):
                
                vec = self.distanceBetweenCells(podocyteList[i], podocyteList[j])
                #print "vec: ", vec
                distances[i,j] = vec

        negOneMatrix = np.full((len(podocyteList), len(podocyteList)), -1)
        tenMatrix = np.full((len(podocyteList), len(podocyteList)), 10.0)
        
        #print np.logical_and(negOneMatrix < distances, distances < tenMatrix)
        indicies = np.where(np.logical_and(negOneMatrix < distances, distances < tenMatrix))
        
        #print "number of links: ", len(indicies[0])
        
        
        for i in range(len(indicies[0])):
            
            self.focalPointPlasticityPlugin.createFocalPointPlasticityLink(podocyteList[indicies[0][i]], podocyteList[indicies[1][i]],
                self.lambdaFFP, self.targetDistance, self.maxDistance)
                
        for cell in self.cellList:
            
            if cell.type == self.CAPILLARY:
                cell.targetVolume = self.capTargetVolume
                cell.lambdaVolume = self.capLambdaVolume
                cell.targetSurface = self.capTargetSurface
                cell.lambdaSurface =  self.capLambdaSurface
                continue
                
            
            cell.targetVolume= self.cellTargetVolume
            cell.lambdaVolume = self.cellLambdaVolume
            
            
            cell.targetSurface = self.cellTargetSurface
                
            cell.lambdaSurface = self.cellLambdaSurface
                                

    def updateAttributes(self):
        if self.starting:
            
            self.cloneParent2Child()
            
#             parentDisSquared = (self.parentCell.xCOM - self.glomerulusCenter[0])**2 + (self.parentCell.yCOM - self.glomerulusCenter[1])**2
#             childDisSquared = (self.childCell.xCOM - self.glomerulusCenter[0])**2 + (self.childCell.yCOM - self.glomerulusCenter[1])**2
            cID = self.parentCell.clusterId
            reassignIdFlag=self.inventory.reassignClusterId(self.childCell,cID)
            self.childCell.targetVolume = 3*self.cellTargetVolume/4
            self.parentCell.targetVolume = self.cellTargetVolume/2
            
            
            self.childCell.targetSurface = 3*self.cellTargetSurface/4
            self.parentCell.targetSurface = self.cellTargetSurface/2
            self.childCell.type = self.PODOCYTEFOOT
            
            
#             if childDisSquared <= parentDisSquared:
#                 self.childCell.type = self.PODOCYTEFOOT
                
#                 self.childCell.targetVolume = self.cellTargetVolume/2
#                 self.parentCell.targetVolume = self.cellTargetVolume/2
            
            
#                 self.childCell.targetSurface = self.cellTargetSurface/2
#                 self.parentCell.targetSurface = self.cellTargetSurface/2
#                 pass
                
#             else:
#                 self.parentCell.type = self.PODOCYTEFOOT
#                 print "set parent type successfully"
                
#                 self.childCell.targetVolume = self.cellTargetVolume/2
#                 self.parentCell.targetVolume = self.cellTargetVolume/2

#                 self.childCell.targetSurface = self.cellTargetSurface/2
#                 self.parentCell.targetSurface = self.cellTargetSurface/2
#                 pass
            return

                    
        
        
            
    
        
    

# from PySteppables import *
# import CompuCell
# import sys

# from PlayerPython import *
# import CompuCellSetup
# from math import *
import datetime


class LoggingSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)
        
    def start(self):
        dateStr = datetime.datetime.today().ctime()
        fileName = 'GCSoutput.csv'
        try:
            self.fileHandle, self.fullFileName = self.openFileInSimulationOutputDirectory(fileName,"w")
        except IOError:
            print("Could not open log file")
            raise
            
        print('test', file=self.fileHandle)
        
        
    def step(self,mcs):
        #PPD Link Logging?
        #Written for 2D sim
        print('Step,', str(mcs), ',', file=self.fileHandle)
        for i in range(self.dim.y):
            yPix = self.dim.y - 1 - i
            rowStr = ''
            for j in range(self.dim.x):
                cell = self.cellField[j, yPix, 0]
                if cell == None:
                    rowStr += 'None,None,'
                else:
                    rowStr += str(cell.id) + ',' + str(cell.type) + ','
            print(rowStr, file=self.fileHandle)
        
        print('', file=self.fileHandle)
#         for cell in self.cellList:
#             print "CELL ID=",cell.id, " CELL TYPE=",cell.type," volume=",cell.volume
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        self.fileHandle.close()
        return
# from PySteppables import *
# import CompuCell
# import sys

# from PlayerPython import *
# import CompuCellSetup
from math import *


class fppLinkTracker(SteppableBasePy):
    def __init__(self, frequency=10):
        SteppableBasePy.__init__(self, frequency)
        
    def start(self):
        print("fppLinkTracker: This function is called once before simulation")
        podocyteList = list(self.cellListByType(self.PODOCYTEBODY))
        i = -1
        idToIndex = {}
        indexToId = {}
        links = []
        distances=[]
        for cell in podocyteList:
            i+=1
            idToIndex[cell.id] = i
            indexToId[i] = cell.id
            for fppd in FocalPointPlasticityDataList(self.focalPointPlasticityPlugin,cell):
                links.append((cell.id, fppd.neighborAddress.id))
                distances.append(self.distanceBetweenCells(cell, fppd.neighborAddress))
            
        #print "links length: ", len(links)
        
        self.initNumLinks = len(links)/2.0
        
        self.pW = self.addNewPlotWindow(
            _title='Number of Links vs time',
            _xAxisTitle='MonteCarlo Step (MCS)',
            _yAxisTitle='Fraction of Remaining Links',
            _xScaleType='linear',
            _yScaleType='linear',
            _grid=True # only in 3.7.6 or higher
        )
        
        self.pW.addPlot('Fraction of Remaining Links', _style='Dots', _color='red', _size=5)
        self.linkData = []
        
    def step(self,mcs):
        print("fppLinkTracker: This function is called every 10 MCS")
        
        podocyteList = list(self.cellListByType(self.PODOCYTEBODY))
        i = -1
        idToIndex = {}
        indexToId = {}
        links = []
        distances=[]
        #For every cell, get the links they are a part of
        for cell in podocyteList:
            i+=1
            idToIndex[cell.id] = i
            indexToId[i] = cell.id
            for fppd in FocalPointPlasticityDataList(self.focalPointPlasticityPlugin,cell):
                links.append((cell.id, fppd.neighborAddress.id))
                distances.append(self.distanceBetweenCells(cell, fppd.neighborAddress))
                
            
        print("links length: ", len(links), len(distances))
        totDist = 0 
        for dist in distances:
            totDist += dist
        avgDist = totDist/float(len(distances))
        
        numLinks = len(links)/2.0 #The above method of getting all of the links ends up double counting the links
        
        #linkMatrix = np.full((len(podocyteList), len(podocyteList)), 0)
        
        for cell in podocyteList:
            pass
            
        self.pW.addDataPoint("Fraction of Remaining Links", mcs, numLinks/self.initNumLinks)
 
        self.linkData.append((mcs, numLinks/self.initNumLinks, avgDist))
        
            
        

            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        fileName = "numLinks.txt"
        self.pW.savePlotAsData(fileName)
        fileName = "numLinksDump.txt"
        try:
            self.fileHandle, self.fullFileName = self.openFileInSimulationOutputDirectory(fileName,"w")
            print('Step,', ',', 'Links', file=self.fileHandle)
            for i in range(len(self.linkData)):
                rowStr = str(self.linkData[i][0]) + ',' + str(self.linkData[i][1]) + ',' + str(self.linkData[i][2]) + ','
                print(rowStr, file=self.fileHandle)

            print('', file=self.fileHandle)
            
            self.fileHandle.close()
#         for cell in self.cellList:
#             print "CELL ID=",cell.id, " CELL TYPE=",cell.type," volume=",cell.volume
        
            
        except IOError:
            print("Could not open log file")
            raise
        
        #print self.linkData[-1][2]
        
        if hasattr(self, 'output_WA'):
            print(str(self._i_WA), str(self._j_WA))
            self.output_WA[self._i_WA, self._j_WA] = self.linkData[-1][1]
            print(CompuCellSetup.simulationPaths.simulationResultStorageDirectory)
            self.CC3DoutputDir_WA.append(CompuCellSetup.simulationPaths.simulationResultStorageDirectory)
            print(self.simulator.getNumSteps())
        else:
            print("no output")
        

        return
    
