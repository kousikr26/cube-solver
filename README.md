# cube-solver
A Rubik's cube solving bot using computer vision

rubikscube_implementation.py is for finding the cube state after performing algorithms in standard cube notation

Use tile_hsv_value_finder.py to find the color of each tile in a face by placing the cube in the shown square in webcam
Use https://github.com/muodov/kociemba to solve the cube using the kociemba algorithm(under 20 moves)

Integration with the kociemba module and arduino code for stepper motors will hopefully be uploaded soon.
