@echo off
color 01
cd pycode
echo before the program launches, make sure you volume isn't on too loud. there may be a beep.
timeout /t 3 > nul
python pcoptimiser.py