# Hackpad
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

<img width="1405" height="1013" alt="Screenshot_20260131_113800" src="https://github.com/user-attachments/assets/0831af5f-b5d0-4492-bc58-e6faaf85e881" />

<img width="1434" height="886" alt="Screenshot_20260131_113843" src="https://github.com/user-attachments/assets/47557325-33d2-425c-ab23-2f3be7684e13" />

<img width="1125" height="883" alt="Screenshot_20260130_153652" src="https://github.com/user-attachments/assets/81679bad-a276-474f-8ede-e2910f074055" />

<img width="579" height="856" alt="Screenshot_20260130_154007" src="https://github.com/user-attachments/assets/e266e348-c39f-4470-9412-c1693464450a" />
