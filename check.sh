#!/bin/bash


sleep 300


if pgrep -x "miner.py" > /dev/null


then
        echo "monitor is running"

else
        echo "Second called!" >> /home/ethos/gpu_crash.log
        python /home/ethos/ethos_monitor/miner.py

fi
