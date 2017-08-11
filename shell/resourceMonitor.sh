#!/bin/bash
while true
do
    echo $(date +%FT%H:%M:%S), $(grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}'), $(free -m | awk 'NR==2{printf "%s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }') >> resource.log
    sleep 10
done
