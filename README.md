## (p)iPod
I really enjoy listening to things while I drive, be it music or podcasts, but I don't like usage of 
data it often requires. I could definitely put more music onto my phone, but to be honest not all smart
phones even have that much memory anymore for music (I think companies would rather you pay for the data
and use their streaming services. I mean why else stop producing 120GB MP3 players?). 

*This project is actively under development in my spare time*

### Installation Setup 
Clone the repository on the Desktop of your raspberry pi. 
```
pi@raspberry:~/Desktop/$ git clone https://github.com/scott-robbins/piPod
pi@raspberry:~/Desktop/$ cd piPod/code
pi@raspberry:~/Desktop/$ sudo python setup.py
```
To run this script on start it needs to be added to /etc/rc.local this will be done during the `-setup` option if it hasn't been done already. Additionally, setup will check that you have music folder setup for creating playlists and customizing playback for modes other than a random shuffle. 

After running setup successfully, just put the RaspberryPi in your car, connect it's power to an available USB port in your car, and connect the AUX cable from the Raspberry Pi into the vehicle. When the car starts 
the RaspberryPi will power-up, and boot into the piPod script now that it's in the /etc/rc.local file. 

### Usage
Initial [prototype](https://youtu.be/6VVyyCdHMFI)
** Using separate power source (small portable battery) eliminates the noisy interference. Will post updated video soon. 


### Features
____________________________________________________________________________________
### *Last Modified August 2020*
