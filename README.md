a simple HMI with basler camera

# Prerequisites
1. install python37
2. plug pylon camera 
3. install wiringPi
> sudo apt install python python3 python-pip python3-pip
Python 2: sudo python -m pip install odroid-wiringpi
Python 3: sudo python3 -m pip install odroid-wiringpi

 
# Installation
$pip install -r requirements.txt
$download code

# How to use it
option 1. launch program manually 
>$python main.py

option 2. launch program automatically when OS startup

>append "python CODE_PATH/main.py" to bash.rc
