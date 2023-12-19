# Introduction

Arduino PDI (Peripheral Device Interface) is a tool set designed to autonomously generate a python wrapper for an Arduino Sketch that allows the functions of that sketch to be executed and evaluated by the computer connected to the Arduino via USB. This can be useful during development as a debugging tool that allows the user to test the functions of the sketch individually and directly. This can also be useful in designing the Arduino to be part of a larger system faciliated by the computer running the PDI code. 

# Workflow
1. Write the Arduino Sketch and adorn the functions that should be made accessible over the serial interface using the [callable] attribute
2. Run the PDI Precompiler, which writes the needed C code into the Arduino Sketch as well as writing the python wrapper code
3. Load the sketch to the device, and load the python wrapper code to run in the interpreter
4. Send commmands over the interface to run the specified functions, get the return values.

   





