# UltrasonicSensorDemo1

INTRODUCTION
 
- Welcome to the ultrasonic motion detector. This program detects motion utilizing an HC-SRO4 ultrasonic sensor and takes a picture using a raspberry pi with a raspberry pi camera module.


![Wiring_Picture](https://user-images.githubusercontent.com/79159077/145067932-a362e8ce-6471-4fcc-8be4-4f0526612865.jpg)


REQUIREMENTS

- Only one of each component is needed unless otherwise noted in the parenthesis.

Raspberry pi

Raspberry pi camera module

breadboard

jumper wires (10)

HC-SRO4 Ultrasonic sensor

LED lights (3)

resistors (3)

EXECUTION

- This program is executable using python and pressing the run button on most platforms. However, this program was made to be ran on the raspberry pi's boot up. This can be done by accessing the rc.local file by typing the command "sudo nano /etc/rc.local" into the terminal. Then paste: 

- "sudo python /home/pi/"filename".py &" 

- in between the line "fi" and "exit0". To exit the file, press command and "x", type in a capital "Y" when prompted to save, and press enter to finish your save.

MAINTAINERS

Wyomissing Steam Club

Jack Gartner, Mansfield University undergrad
jackgartner7@gmail.com
