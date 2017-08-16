#!/bin/bash
echo "timestamp, cpu(%), memory(%)"
while true
do
    echo $(date +%FT%H:%M:%S), $(grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'), $(free -m | awk 'NR==2{printf "%.2f\n", $3*100/$2 }')
    sleep 60
done
