# trappyframe

`trappyframe` is a **low-cost** and **open-source** microscopy system that is **highly customisable**. It is an inverted low-magnification system (1-2X) that is built on a 3D printed opto-mechanical cage system, a few optical components, and the Raspberry Pi Hardware ecosystem. The microscope can be printed and assembled in any laboratory/school/home with a few simple tools. 

The microscope is primarily designed to track motile algae and is optimised for parallelisation. Multiple units can be assembled, mounted, and operated in parallel. Instructions on parallelisation, including the assmmbly of a Raspberry Pi cluster/bramble can be found in the parallel project [Trappy-Scopes/raspberry_shrub](https://github.com/Trappy-Scopes/raspberry_shrub/tree/main). The control layer software can be found in the parallel project [Trappy-Scopes/trappyscopes](https://github.com/Trappy-Scopes/trappyscopes) and instructions to configure it for `trappyframe`can be found in the [here](docs/notes/software_configuration.md).

| ![assmbly_image](images/Assembly1_2024-Jan-12_12-07-07AM-000_CustomizedView5221869374_png_alpha.png) | <img src="images/Clusterv4.png" alt="cluster_image" style="zoom: 50%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                         Single Unit                          |                     Parallelised Cluster                     |



## Scope of this repository

1. Repository for the 3D models of the opto-mechanical components: [trappyframe](/trappyframe)
2. Repository for other bill of materials (BOM): [BOM](/docs/notes/bom.md)
3. Provide assembly instructions: [Assembly Instructions](/docs/notes/assembly_instructions.md)



## trappyframe

`trappyframe` is a 3D-printed optical cage system that is ready to use after printing. It does not require thread-inserts because it relies on flexure of the material. The system is similar  to [ThorLabs Optical Cage system](https://www.thorlabs.com/optical-cage-systems) or the [Edumund Optics Optical Cage system](https://www.edmundoptics.com/c/optical-cage-system/763/ and is compatible with them. It uses **6mm support rods** and is primarily based on the a **60mm** cage footprint.

The system is derived from a few block templates and allows further customisations from the same.

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |



<model-viewer alt="Neil Armstrong's Spacesuit from the Smithsonian Digitization Programs Office and National Air and Space Museum" src="Astronaut-Unlit.glb" shadow-intensity="1" camera-controls touch-action="pan-y" style="width: 400px; height: 400px;"></model-viewer>









## Frame Components

Notes:

1. The rod holes are currently set to 6.3mm corresponding to the specific 3D printer and nozzle sizes. Ity might have to be modified based on your settings.
2. 3D printer used: Bambu Lab X1E 0.4mm nozzle.
3. Filament of choice: PLA Black 3D.

| No   | Peripheral                                | Filename                                                     | Latest versionª |
| ---- | ----------------------------------------- | ------------------------------------------------------------ | --------------- |
| -    | **TOP - Illumination controller**         | -                                                            | -               |
| 1    | Top plate (frame support)                 | [Top Plate w Magnets(FSSBTv2) v13.stl]("frame/Top%20Plate%20w%20Magnets(FSSBTv2)%20v13.stl") | 13              |
| 2    | LED mount plate                           | [SBTv2 LED mount w studs v11.stl](frame/SBTv2%20LED%20mount%20w%20studs%20v11.stl) | 11              |
| 3    | Condensor mount plate                     | [Condensor Mount 25mm wo tube  (SBTv2) v3 6.3mm rod holes.stl](/frame/Condensor%20Mount%2025mm%20wo%20tube%20%20(SBTv2)%20v3%206.3mm%20rod%20holes.stl) | 3               |
| 4    | Sample stage plate                        | [Sample Mount Agile w Small magnets (SBTv2) v7.stl](/frame/Sample%20Mount%20Agile%20w%20Small%20magnets%20(SBTv2)%20v7.stl) | 7               |
| 5    | Mid plate (frame support)                 | [Mid Plate Magnets 6.3mm  (FSSBTv2) v14.stl](/frame/Mid%20Plate%20Magnets%206.3mm%20%20(FSSBTv2)%20v14.stl) | 14              |
| 6    | Tube lens upper mount plate               | [Tube Lens Holder 6.3 upper (SBTv2) v2.stl](/frame/Tube%20Lens%20Holder%206.3%20upper%20(SBTv2)%20v2.stl) | 2               |
| 7    | Tube lens lower mount plate               | [Tube Lens Holder 6.3 lower (SBTv2) v3.stl](/frame/Tube%20Lens%20Holder%206.3%20lower%20(SBTv2)%20v3.stl) | 3               |
| 8    | Base plate w camera mount (frame support) | [Base Plate 6.3mm (FSSBTv3) v2.stl](/frame/Base%20Plate%206.3mm%20(FSSBTv3)%20v2.stl) | 2               |
| -    | **BOTTOM - Breadboard**                   | [ThorLabs MB3060/M](https://www.thorlabs.com/thorproduct.cfm?partnumber=MB3060/M) | -               |

ª : the version numbers correspond to the filename version for Fusion 365. 



## Standard Block Templates

The parts are designed from standard design blocks. Two different versions exist. One for the normal parts, and one for parts which support the rods, and the box for the frame.

| No   | Peripheral Block Template                     | Filename                                      | Latest versionª |
| ---- | --------------------------------------------- | --------------------------------------------- | --------------- |
| 1    | Standard block template (SBT)                 | [SBTv2 v3.stl](frame_templates/SBTv2.stl)     | 2               |
| 2    | Frame support standard block template (FSSBT) | [FSSBTv3 v3.stl](frame_templates/FSSBTv3.stl) | 3               |

ª : the version numbers correspond to the filename version for Fusion 365. 
