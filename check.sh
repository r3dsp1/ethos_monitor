#!/bin/bash


sleep 300


if pgrep -x "miner.py" > /dev/null


then
        echo "monitor is running"

else

        sh /home/ethos/custom.sh

fi
