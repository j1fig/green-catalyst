#!/bin/bash

#wget http://downloads.raspberrypi.org/raspbian_latest -O raspbian.zip
#mkdir tmp
#cd tmp
#unzip ../raspbian.zip
#cd ..

# insert SD card here...

echo "Unmounting SD card partitions..."
umount /dev/mmcblk0p1
umount /dev/mmcblk0p2

echo "Writing image to SD card..."
dd bs=1M if=tmp/2014-09-09-wheezy-raspbian.img of=/dev/mmcblk0
sync
