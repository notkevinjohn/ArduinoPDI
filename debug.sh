#!/bin/bash
cp Sketch.c Firmware/Firmware.ino

echo "Compiling..."
arduino-cli compile --fqbn arduino:avr:mega Firmware

echo "Uploading..."
arduino-cli upload -p /dev/arduino-mega --fqbn arduino:avr:mega Firmware


echo "Serial Monitor..."
serial tty=/dev/arduino-mega
