import sys
from cc3d import CompuCellSetup
from glomeruluscrosssectionSteppables import ConstraintInitializerSteppable

CompuCellSetup.register_steppable(steppable=ConstraintInitializerSteppable(frequency=1))

from glomeruluscrosssectionSteppables import GrowthSteppable
from glomeruluscrosssectionSteppables import CellInitializer
# from glomeruluscrosssectionSteppables import MitosisSteppable
# from glomeruluscrosssectionSteppables import DeathSteppable
# from glomeruluscrosssectionSteppables import LoggingSteppable

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
        
        