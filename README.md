# GlomSliceGen



## Overview
This simulation showcases using procedural generation to create geometry of slices of glomeruli. This repository archives the code presented in Chapter 4 of the PhD thesis "Tools to Accelerate and Advance Modeling Disease Progression" by Steve M. Ruggiero. The repo contains a CompuCell3D simuation that produces glomerular geometry with a parameterized algorithm.

## Authors
Steve M. Ruggiero and Ashlee N. Ford Versypt (ashleefv@okstate.edu), School of Chemical Engineering, Oklahoma State University

## Usage
The simulation stored here requires [CompuCell3D, availible here.](https://compucell3d.org/)


The code discussed in the thesis are the following components:
* the CellInitializer class in Simulation/glomeruluscrosssectionSteppables.py
* the functions defined in Simulation/CellGeom.py

The geometry parameters are defined in the constructor of the CellInitializer class.

To produce the geometry, simply open the simulation in CompuCell3D

## Supporting software

The following software were used in this project and are needed to generate the geometry and run the simulation:
* [NumPy][1]
* [CompuCell3D][2]

[1]: https://www.numpy.org/ "NumPy"
[2]: https://compucell3d.org/ "CompuCell3D"

## Acknowledgments

The software package described here was made possible in part by funding through the award for project number HR17-057, from the Oklahoma Center for the Advancement of Science and Technology.

## Community Guidelines

This repository serves to explictly archive the state of this code at the publication of the aforementioned thesis.
