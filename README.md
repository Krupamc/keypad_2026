# My Linux-looking Macropad
The name is a work in progress I know haha. This is my macropad, a small custom shortcut pad with several layers of shortcuts that are changed through the rotary encoder. Different LEDs light up and the OLED with update with the current layer and appropriate image. I created this in order to increase my productivity and overall workflow of my desk.
---

## Features:
- 128x32 OLED Display for customized layer imagary
- EC11 Rotary encoder to switch between layers.
- 5 Layer LEDs to coordinate with the layers (will activate one by one and change colors; layer 0 has 1 navy blue LEDs, layer 1 has 2 dark blue LEDs).
  - (Colors are customizable) 
- 4 Keys
- 1 Status/Ambient LED
- Being a really cool thing to flex.
---
## PCB:
The PCB (Printed Circuit Board) was created using KiCad. Awesome open source software.
You can open the PCB here:
[![View PCB on KiCanvas](https://hack.club/pcb-badge)](https://kicanvas.org/?repo=https://github.com/Krupamc/keypad_2026/tree/main/PCB)


### Schematic: 
<img width="1448" height="846" alt="image" src="https://github.com/user-attachments/assets/77350930-4a07-4100-afd7-55d89742bf7f" />
Here is the plan for the PCB laid out with my wiring.

### PCB:
<img width="1113" height="790" alt="image" src="https://github.com/user-attachments/assets/ab07fcac-1e97-40f8-84d2-4aab02a39310" />
<img width="1612" height="1042" alt="image" src="https://github.com/user-attachments/assets/26b2031d-601e-4e98-b566-8e5043f15849" />
Very cool looking PCB. I added as much silkscreen I could to really sell the terminal-inspired design.

## CAD:
<img width="1032" height="1037" alt="image" src="https://github.com/user-attachments/assets/d59b9d4a-7e73-44c5-a8b3-a325aa96bc55" />
I created a case in Fusion. Excuse how it is not very good/original as it is my first time doing CAD before. I have two parts: the bottom and top case. 
### Bottom Case:
The bottom case is a box with standoffs to hold (on the top-right, and bottom-left) the PCB. M3x16mm screws go through the screw holes on the bottom through the standoffs. The bottom case also has a single foot that has a 40° angle for one inch. (same as my current keyboard to be consistant) The foot has small circle indents for rubber feet in future or hot glue. There is also a USB-C cutout for the microcontroller 
<img width="771" height="881" alt="image" src="https://github.com/user-attachments/assets/69445ee5-ca5e-429f-9118-72f7b1b41fb6" />
### Top Case:  
This section has extrusions for heat inserts to go (for the screws mentioned before) as well as holes for the OLED, LEDs, keys, and the rotary encoder.
<img width="1405" height="773" alt="image" src="https://github.com/user-attachments/assets/2f2f0d04-59ad-47f6-98e5-54af34663eba" />

<img width="1357" height="920" alt="image" src="https://github.com/user-attachments/assets/1aa192d2-27c8-46cf-a3fe-6677966cd68e" />

---

## Firmware Functions:
Coded in KMK (Micro-python based keyboard framework). On each layer, a configurable photo, text splash and color (for LEDs) is shown. The number of LEDs active is based on the layer number.

Right now the short cuts include:
- Copy, Paste, Undo, Redo
- CTRL + F, clipboard, File explorer, Screenshots
- Pause unpause, mute discord mic, defen discord, mute pc

Planned to add ones for games I play/other applications later.

---

## BOM:
- 1X Seeed XIAO RP2040
- 1x 0.91" 128x32 OLED Display
- 4x Cherry MX Switches
- 4x DSA Keycaps
- 1x EC11E Rotary encoders
- 6x SK6812 MINI-E LEDs
- 2x M3x16mm screws
- 2x M3x5mx4mm heatset inserts
- 3x Parts for 3D Case (Top, Bottom, and Knob).
