# Assembly instructions

How to assemble the trappy-scopes microscopes in easy to follow 100 steps:

1. Take a **baseplate** and mount the Rasperry Pi HQ Camera on the pegs using M2-10mm screws (X4). Remove the tripod mount from the camera as it is not required. We recommend long CSI cables (24" from Adafruit 1731). Pass the CSI cable from the slits to the camera connector. Prefer using a side which is adjacent to the **flexures**. Connect the cable (it should pass under the Baseplate and to the camera. Do not twist the cable and handle it gently.) The connectors (shiny-side) should face up towards you when you connect them to the camera.

2. Take four 6mm diameter 50cm Stainless steel rods. You can get your own cheaper ones or buy from ThorLabs. Mount them to the baseplate and tighten the flexures using M4-10mm screws. Make sure that there is no imbalance and the rods are evently inserted. You should consider additional steps to improve rod adhesion to the baseplate:
	1. Use a bit of stanard electrical tape at the end of the rods to improve fitting.
	2. Additional headless-screws that can be mounted (holes already inbuilt.) TODO-add screw specifications
	3. Use a strong glue at the baseplate to bond the rods to the plate.
	
3. Mount the baseplate on an **M6 breadboard** temporrily to aid assembly. We recommend a smaller breadboard for the assemby.  Subsequently the unit should be transported to its final place after certain assembly steps. M6-10mm screws are recommended for this.

4. Add the **Lower-Tube lens mount** (has a smaller central hole compared to the Upper-Tube mount) to the frame from the top (The flexure side should align with the flexure side of the baseplate).

5. Add the **zoomlens** to the mount without taking of its covers.

6. Add the **Upper-zoom lens mount**. The zoomlens should snuggly align with mounts. We will connect it to the camera and align it later.

7. Add the **midplate** to the frame and place it approximately near the knulred ring of the zoomlens.

8. Assemble the **sample stage**:
	1. The magentic mount sample stage needs to be assembled beforehand. It used four 1.9mm high 6.2mm diameter magnets in a cylinder form-factor. The magnets should directly fit in their respective holes. But since 3D printing is not an exact science, we can use the help of some glue. Use only sufficiently enough glue and fit the magents in place. Decide which pole should stay up and stick with it! Do not randomly place the magents. 
	2. If you used glue, let it dry for a sufficent time. Clean the stage of any access glue beforehand.
	3. If you plan to use any additional peripherals that mount from below, you should also install the magents under the stage in the same prescribed way.
	4. Add the sample mount to the assembly (align the flexures!). Z-position is irrelvant. Place it above the tubelens ofcourse.
	
9. Add the **asphere/condensor mount** to the assembly (align the flexures!). Check this part specifically for imperfections on the inside. Clean it, if required.

10. Add the **ED/illumination mount** to the assembly sans the LED clip. Pick a conventional side for the slit and stick with it (extra careful in aligning the flexures! Todo-explain more.

11. Assemble the **top plate**:
	1. Add two magnets (the centre should be sufficient). Follow the same rules as the **sample stage**.
	2. Add it to the saaembly.
	
12. Attaching the camera to the tubelens: it helps a lot to be clean. Clean the dust. Wash your hands and wear gloves if you can!
	1. Lift the componets gently until there is some space bwtween the camer and the tubelens.
	2. Remove the caps first from the tubelens and then the camera. Bring the two componets close and they should perfectly align! If they don't then you made a mistake somewhere. Cover the camera immediately and start again. Remember to choose the apropriate adapter (the HQ camera comes with both C and CS mounts.)
	3. Rotate the tubelens very slowly as access speed causes friction and that chips off small pieces of metal that contaminate the camera surface.
	4. Turn until you can't and ensure that the tube lens is firmly mounted on the camera.
	5. Move the upper and lower zoomlens mount plate to fix the tubelens properly.
	6. Use eight M4-10mm screws to fix both the plates in position.
	7. Sometime, the alignment mark on the tubelens gets shaded by the box, so better add a haptic cue, like a piece of coarse tape that you can feel.
13. Assmble the **trappybox side sections** (the long ones) (M3-5mm screws):
	1. Take the back-side and mount it on the topplate (central and a side screw).
	2. Now add the central screw on the baseplate. Screwing is difficult but not immpossible. If its too difficult for you, then leave it for the end!
	3. Now try and align the midplate with its respective screw holes (first the center and then a side one).
	4. Repeat these steps for the front side  (long one)!
	5. Add extra screws to improve the stability, these many should work fine.
	
	1. With the last steps, we have also properly aligned the midplate and the topplate, so fix them with M4-5mm screws.
	2. Unscrew the scope assembly from the breadboard (all four screws). But keep the screws there. Release the screws that connect the box to the baseplate to release some tension. Now attach the small flaps with one M3-5mm screw each on the baseplate. Do not tighten it, keep them such that they are like a flap. You can skip this step if you have no space constrains!
	3. No put the scope on its designated position and tighten the M6 screws again! Tighten them well! It's permanent. You should be able to access the screws through the flaps.
	4. Pass the CSI cable to the SoC (RPi 4B or smth) and tug the extra cable between the tubelens and the box. Now tighten the small portions of the box and fix them. If you have many CSI cables that are overlapping, insulate them further with Aluminium foil or something, or there will be a lot of interferance.
	5. Add the pico board that connects to LEDs and the temperature sensor on top of the topplate. There is a breadboard and standard M2.6 screws should work well.
	6. Now add an appropriate temperature and humidity sensor (swinging near the sample stage and run the wires through the top plate flexure on your left side).
	7. On the right side. Add a closed Rod support clamp and use two M3-20mm screws and M3 nuts to secure them.
	8. Assembling the LED climp complex:
		1. TODO
	9. Connect the sensors and LEDs to the RPi Pico based controller. Make sure to connect to the right pins and keep the connections tight.
	10. 
