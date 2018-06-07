#!/bin/bash
# /home/ethos/custom.sh

# update monitor on boot
rm -f -R ethos_monitor
git clone https://github.com/r3dsp1/ethos_monitor
chmod -R 775 ethos_monitor/

# config file
echo "1" > /opt/ethos/etc/autorebooted.file      

# start monitor
./ethos_monitor/miner.py

exit 0
