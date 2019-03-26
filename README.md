# cube-solver
**A Rubik's cube solving bot using computer vision**

The Rubik’s cube when placed in front of the webcam is captured and cropped.

The average hue, saturation and value of each tile are found and converted to the corresponding colour by matching the values with predefined data.

The colours are stored in a 3D array and processed to a format required by the kociemba algorithm which returns a solution sequence which is further processed to use only 5 stepper motors

The solution string is passed to an Arduino via serial port using pyserial which rotates the corresponding stepper motors

The NEMA-17 stepper motors are controlled by motor drivers on a RAMPS 1.4 board attached to an Arduino MEGA microcontroller board.
## Dependencies and Requirements
- Python 3.7
- Arduino IDE
- OpenCV
- pyserial
- kociemba (https://github.com/muodov/kociemba)
- numpy

## Usage
- Before running calibrate the HSV values in final_cube_solver.py by finding HSV values for each color of your cube in different lighting conditions using cube_state_finder.py in tests folder 
- After correct color is being recognised upload final.ino to the arduino mega attach the RAMPS 1.4 and stepper motors according to datasheet

- Run final_cube_solver.py and scan each face in an orientation as provided in https://github.com/muodov/kociemba
- The program should output around 100 moves after replacing the up face moves
- These moves will automatically be sent to the arduino by pyserial

## Files
- final_cube_solver is the main file including all functions from scanning cube to writing to arduino
- scrambleunscramble.py is for demonstration purposes and just scrambles and reverses it.
- rubikscube_implementation.py is not used anywhere and just applies the transformations corresponding to an algorithm and returns the new cube state
- pyserialtest.py is for testing purposes and directly writes some moves to the arduino and moves the steppers
- tests folder contains various attempts and fails at automatic cube detection 
