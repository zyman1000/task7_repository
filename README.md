### after opening the terminal using CTRL + Alt + t

**command**:`pwd`

**output**: `/home/dell`
this prints the current working directory

**command**: `ls`

**output**: `Arduino  Documents  Fluent-gtk-theme  Pictures  snap       Videos
Desktop  Downloads  kora              OBS    Public    Templates`

note: extra content appears in the list because this is a personal machine not a freshly installed experimental environment

**command**: `cd Desktop`

this changes the current working directory to desktop

**command**: `touch bash_script.sh`

**output**: a file named "bash_script.sh" has been created in the desktop

**command**: `nano bash_script.sh`

**output**: text editor pops up

after writing this to the file:

`#!/bin/bash`

`pwd`

I press CTRL + X then y then enter to exit

**command**: `./bash_script.sh`

**output**: `bash: ./bash_script.sh: Permission denied`

**solution**: adding execution permission to the bash file

**command**: `chmod +x bash_script.sh`

after that: `./bash_script.sh`

**output**: `/home/dell/Desktop`

**command**: `mkdir scripts`

**output**: a folder named "scripts" is created on the desktop

**command**: `cp bash_script.sh scripts`

**output**: the bash script is copied to the scripts folder

**command**: `rm bash_script.sh`

**output**: the bash script is removed from the desktop

**command**: `cat scripts/bash_script.sh`

**output**:

`#!/bin/bash`

`pwd`

**command**: `mv scripts premade_folder`

**output**: moves the folder "scripts" to a folder called "premade_folder"

**command**: `htop`

**output**:

    Command 'htop' not found, but can be installed with:

    sudo snap install htop  # version 3.3.0, or

    sudo apt  install htop  # version 3.0.5-7build2

    See 'snap info htop' for additional versions.'

**solution**: `sudo apt install htop`

now htop is installed

**command**: `htop`

**output**: a simple task manager appears

CTRL + C to exit

**command**: `top`

**output**: a simpler task manager appears

using a new tab in the terminal we take the PID of top which is 18480 in this case

**command**: `kill 18480`

**output**: the process of "top" stopped

**command**: `cd ~`

**output**: now we are in the home directory

### now, we will use SSH

**command**: `ssh bandit0@bandit.labs.overthewire.org -p 2220`

after typing `yes` the output is: 

warning: Permanently added '[bandit.labs.overthewire.org]:2220'
(ED25519 to the list of known hosts.
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit0@bandit.labs.overthewire.org's password: 

after entering the password which was invisible while it was being typed for some reason
**output**: got greeted by overthewire.org

**command**: `whoami`

**output**: `bandit0`

**command**: `exit`

**output**: connection to the site was closed

**command**: `ls | grep Desk`

**output**: `Desktop` where "desk" was red

**bonus**: `neofetch` :)

**output**: ![screenshot](https://drive.google.com/file/d/1PcUA4kGz-lAJ4625Vvzt9o19K_OOS25s/view?usp=sharing)
