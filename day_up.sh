#!/bin/bash
# This is to compare today's log with yestoday's log
time_y=$(date -d "-6 day" +%F)
time=$(date +%F)
#time_y_test=$(date -d "-2 day" +%F)
#time_test=$(date -d "-1 day" +%F)
str1="./mhn/data/"$time_y""
str2="./mhn/data/"$time""
hp=(_conpot _suricata _cowrie _dionaea _elastichoney _snort _p0f)
for hp_type in ${hp[@]}
do
    echo ${str1}${hp_type}
    echo ${str2}${hp_type}
    grep -F -w -f ${str1}${hp_type} ${str2}${hp_type} -v | wc -l
done
