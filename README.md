# ethos_monitor

Usage
=====
1st optional argument: rig name shown in xxx.ethosdistro.com
              Example: 2e15d2
2nd optional argument: json api in ethosdistro site
              Example: "http://xyz.ethosdistro.com/?json=yes"
These two arguments are required if there is some issue in accessing some files in "/var/run/ethos".

Debugging optional argument: If it is set to "-debug", it dumps running gpu and total gpu number.


sample usage:
   $ ./miner.py
or $ ./miner.py 2e15d2 "http://xyz.ethosdistro.com/?json=yes"

  (if you want to dump debug info)
or $ ./miner.py -debug
or $ ./miner.py -debug 2e15d2 "http://xyz.ethosdistro.com/?json=yes" (required in case of access problem in "/var/run/ethos")


Cronjob setup
=============
Open cronjob using "crontab -e" command.
Add following line at the end -
   @reboot /home/ethos/ethos_monitor/miner.py
or @reboot /home/ethos/ethos_monitor/miner.py 2e15d2 "http://xyz.ethosdistro.com/?json=yes"

Now, restart the system. The script will launch autometically at startup.


log file
========
/home/ethos/gpu_crash.log



If you have any query, please contact me.
Email: hiranmoy.iitkgp@gmail.com


Donations (To transeos)
==================================
Bitcoin: 14BwKCzHYseFX6ae9S3ArVrvZC6A3h7QZx
Ethereum: 0x80ae5B86340d929da6D9868F1175061faE332f4C
Dash: XwXJ2t47zi9HPFxQzfAYxirqS7bcZ3r1Kf
Litecoin: LTek3HbMrgm2p4So69ST8MNPsWbU5vwVKE
Decred: DsWUVKcRhyy7DqhtBk2SoGHPXkffTv79HR8
