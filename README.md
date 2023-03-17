# Use **Python** programs to **prevent** your machine from **sleeping**

You *DO NOT* need this in most scenarios, especially on your own laptop/PC. 

**If you could not edit the sleep settings in the machine**

then this might be good for you:

- have your status as `Online` all the time; like `MS Teams`
- keep background activities always on so your process won't break accidentally if the PC went to sleep

# Installation

clone the project

```
cd .../your_cloned_path/fishtouch

pip install -r .\requirements.txt
```

# Guide

To start, run below command in the `fishtouch` directory (check with `pwd` or `chdir`)

it will simulate mouse or keyboard activity. 

```
python turnvolume.py 
```
or 
```
python movemouse.py
```

by using Anaconda Prompt/PowerShell or Mac Terminal

# Notes

*You need to have python installed on your machine first*

after having python installed,

```
which python # MacOS Terminal
where python # Windows Anaconda Prompt
```

```
python --version
```

Mine was `Python 3.8.8` when coding. 