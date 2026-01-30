<img width="1125" height="883" alt="Screenshot_20260130_153652" src="https://github.com/user-attachments/assets/6281638c-926c-41b1-a1e5-9e27b903302e" /><img width="1255" height="1003" alt="Screenshot_20260130_153802" src="https://github.com/user-attachments/assets/fd22075c-7b99-49df-8490-aaaeaedaa168" /># Hackpad
My personal macropad with 9 keys. There is also a mini led that indicates status.

I made this for Hack Club's Blueprint.

# Parts
- PCB (1)
- Seeed XIAO RP2040 (1)
- MX-Style Switches (9)
- Blank DSA Keycaps (9)
- SK6812 MINI-E LED (1)
- M3x16mm Screws (4)
- M3x5mx4mm Heatset Inserts (4)
- 3d Printed Case (1)

# Hardware
The macropad uses a 90mm x 61mm PCB board.
I used KiCAD to design the PCB.
It includes a Seeed Studio XIAO RP2040 as the micrcontroller, 9 switches for keys, and a mini led.
Each key is wired to its own pin on the XIAO, and they all connect to ground.

# Case
The case for the macropad was made using Onshape.
The stylish design is a box with filleted edges.
It includes a base as well as a cover to fit the PCB.
It can also be held together by screws in each corner.

# Software
The macropad uses kmk firmware, which is Python-based and found at https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/Getting_Started.md.
The XIAO also needs circuitpython to be fully compatible.

For assembly, download circuitpython to the XIAO drive, then upload the kmk file and main.py to the board.

<img width="1125" height="883" alt="Screenshot_20260130_153652" src="https://github.com/user-attachments/assets/81679bad-a276-474f-8ede-e2910f074055" />

<img width="1255" height="1003" alt="Screenshot_20260130_153802" src="https://github.com/user-attachments/assets/24c402d8-9a27-48e3-a34b-8b6dcfe5c17e" />

<img width="1336" height="912" alt="Screenshot_20260130_153828" src="https://github.com/user-attachments/assets/35f2bc26-9f98-4f1b-8c6f-d9ec250c84dd" />

<img width="579" height="856" alt="Screenshot_20260130_154007" src="https://github.com/user-attachments/assets/e266e348-c39f-4470-9412-c1693464450a" />
