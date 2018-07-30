#!/bin/bash

sudo update-miner claymore
sudo update-miner ethminer

cd

rm -f -R ethos_monitor

git clone https://github.com/r3dsp1/ethos_monitor

chmod -R 775 ethos_monitor/

rm -f custom.sh

cp ~/ethos_monitor/custom.sh ~/custom.sh

chmod -R 755 custom.sh

echo "1" > /opt/ethos/etc/autorebooted.file

sudo timedatectl set-timezone Asia/Hong_Kong

echo "0 * * * * sh /home/ethos/ethos_monitor/check.sh" > cron

crontab cron

crontab -l

rm cron

rm gpu_crash.log

sudo reboot
