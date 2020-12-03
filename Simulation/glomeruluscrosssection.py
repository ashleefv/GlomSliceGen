import sysfrom os import environfrom os import getcwdimport string
from cc3d import CompuCellSetup
from glomeruluscrosssectionSteppables import ConstraintInitializerSteppable

CompuCellSetup.register_steppable(steppable=ConstraintInitializerSteppable(frequency=1))

from glomeruluscrosssectionSteppables import GrowthSteppableGrowthSteppableInstance=GrowthSteppable(frequency=50)CompuCellSetup.register_steppable(steppable=GrowthSteppableInstance)
from glomeruluscrosssectionSteppables import CellInitializerinstanceOfCellInitializer=CellInitializer(frequency=1)CompuCellSetup.register_steppable(steppable=instanceOfCellInitializer)
# from glomeruluscrosssectionSteppables import MitosisSteppable# MitosisSteppableInstance=MitosisSteppable(sim,_frequency=1)# steppableRegistry.registerSteppable(MitosisSteppableInstance)
# from glomeruluscrosssectionSteppables import DeathSteppable# DeathSteppableInstance=DeathSteppable(frequency=1)# CompuCellSetup.register_steppable(steppable=DeathSteppableInstance)
# from glomeruluscrosssectionSteppables import LoggingSteppable# instanceOfLoggingSteppable=LoggingSteppable(frequency=1)# CompuCellSetup.register_steppable(steppable=instanceOfLoggingSteppable)

if "injectors_WA" in globals():
    for func in injectors_WA:
        func(_i_WA)
                


# from glomeruluscrosssectionSteppables import fppLinkTracker
# instanceOffppLinkTracker=fppLinkTracker(frequency=10)
# CompuCellSetup.register_steppable(steppable=instanceOffppLinkTracker)

if "output_WA" in globals():
    print("indicies: ", _i_WA, _j_WA)
    instanceOffppLinkTracker.output_WA = output_WA
    instanceOffppLinkTracker._i_WA = _i_WA
    instanceOffppLinkTracker._j_WA = _j_WA
    instanceOffppLinkTracker.CC3DoutputDir_WA = CC3DoutputDir_WA
    print(instanceOffppLinkTracker._i_WA, instanceOffppLinkTracker._j_WA)
    

CompuCellSetup.run()
        
        