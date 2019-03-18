# cube-solver
A Rubik's cube solving bot using computer vision

The Rubik’s cube when placed in front of the webcam is captured and cropped.

The average hue, saturation and value of each tile are found and converted to the corresponding colour by matching the values with predefined data.

The colours are stored in a 3D array and processed to a format required by the kociemba algorithm which returns a solution sequence which is further processed to use only 5 stepper motors

The solution string is passed to an Arduino via serial port using pyserial which rotates the corresponding stepper motors

The NEMA-17 stepper motors are controlled by motor drivers on a RAMPS 1.4 board attached to an Arduino MEGA microcontroller board.
