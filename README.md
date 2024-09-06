# trappyframe

Repository of hardware design files for trappy scopes.

![assmbly_image](images/Assembly1_2024-Jan-12_12-07-07AM-000_CustomizedView5221869374_png_alpha.png)

## Frame Components

Notes:

1. The rod holes are currently set to 6.3mm corresponding to the specific 3D printer and nozzle sizes. Ity might have to be modified based on your settings.
2. 3D printer used: Bambu Lab X1E 0.4mm nozzle.
3. Filament of choice: PLA Black 3D.

| No   | Peripheral                                | Filename                                                     | Latest versionª |
| ---- | ----------------------------------------- | ------------------------------------------------------------ | --------------- |
| -    | **TOP - Illumination controller**         | -                                                            | -               |
| 1    | Top plate (frame support)                 | [Top Plate w Magnets(FSSBTv2) v13.stl](/frame/Top Plate w Magnets(FSSBTv2) v13.stl) | 13              |
| 2    | LED mount plate                           | [SBTv2 LED mount w studs v11.stl](/frame/SBTv2 LED mount w studs v11.stl) | 11              |
| 3    | Condensor mount plate                     | [Condensor Mount 25mm wo tube  (SBTv2) v3 6.3mm rod holes.stl](/frame/Condensor Mount 25mm wo tube  (SBTv2) v3 6.3mm rod holes.stl) | 3               |
| 4    | Sample stage plate                        | [Sample Mount Agile w Small magnets (SBTv2) v7.stl](/frame/Sample Mount Agile w Small magnets (SBTv2) v7.stl) | 7               |
| 5    | Mid plate (frame support)                 | [Mid Plate Magnets 6.3mm  (FSSBTv2) v14.stl](/frame/Mid Plate Magnets 6.3mm  (FSSBTv2) v14.stl) | 14              |
| 6    | Tube lens upper mount plate               | [Tube Lens Holder 6.3 upper (SBTv2) v2.stl](/frame/Tube Lens Holder 6.3 upper (SBTv2) v2.stl) | 2               |
| 7    | Tube lens lower mount plate               | [Tube Lens Holder 6.3 lower (SBTv2) v3.stl](/frame/Tube Lens Holder 6.3 lower (SBTv2) v3.stl) | 3               |
| 8    | Base plate w camera mount (frame support) | [Base Plate 6.3mm (FSSBTv3) v2.stl](/frame/Base Plate 6.3mm (FSSBTv3) v2.stl) | 2               |
| -    | **BOTTOM - Breadboard**                   | ThorLabs MB3060/M                                            | -               |

ª : the version numbers correspond to the filename version for Fusion 365. 



## Standard Block Templates

The parts are designed from standard design blocks. Two different versions exist. One for the normal parts, and one for parts which support the rods, and the box for the frame.

| No   | Peripheral Block Template                     | Filename                                          | Latest versionª |
| ---- | --------------------------------------------- | ------------------------------------------------- | --------------- |
| 1    | Standard block template (SBT)                 | [SBTv2 v3.stl](/frame_templates/SBTv2 v3.stl)     | 2               |
| 2    | Frame support standard block template (FSSBT) | [FSSBTv3 v3.stl](/frame_templates/FSSBTv3 v3.stl) | 3               |

ª : the version numbers correspond to the filename version for Fusion 365. 
