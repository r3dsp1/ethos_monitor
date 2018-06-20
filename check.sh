#!/bin/bash


sleep 300


if pgrep -x "miner.py" > /dev/null


then
        echo "monitor is running"

else
        echo "Second called!" >> /home/ethos/gpu_crash.log
        sh /home/ethos/custom.sh

fi
