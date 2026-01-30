# Hackpad
My personal macropad with 9 keys. There is also a mini led that indicates status.

I made this for Hack Club's Blueprint.

# Hardware
The macropad uses a 90mm x 61mm PCB board.
I used KiCAD to design the PCB.
It includes a Seeed Studio XIAO RP2040 DIP as the micrcontroller, 9 switches for keys, and a mini led.
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
