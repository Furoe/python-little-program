# -*- coding: utf-8 -*-
#author Furo Yang

import smtplib
import datetime
import os
import time

def send_email(error_msg):
    server = smtplib.SMTP_SSL('smtp.yeah.net',465)
    my_email = 'furo_yang@yeah.net'
    my_pwd = 'ilcx12345'
    target_email = '17751038730@163.com'

    #send email
    msg = "\r\n".join([
        "From: " + my_email,
        "To: " + target_email,
        "Subject: Mongodb is Down",
        "",
        error_msg
    ])

    server.login(my_email,my_pwd)
    server.sendmail(my_email,target_email,msg)
    server.quit()
    print("Done")

def get_ip():
    sh = 'echo $(curl -s http://txt.go.sohu.com/ip/soip)| grep -P -o -i "(\d+\.\d+.\d+.\d+)"'
    r = os.popen(sh)
    m = r.read()
    r.close()
    return m.strip()

def watch():
    isAlive = "ps -ef | grep mongodb | grep -v grep | wc -l"
    r = os.popen(isAlive)
    m = r.read()
    m = m.strip()
    r.close()
    print m
    if m == '1':
        print "Detected the mongodb is down"
        myaddr = get_ip()
        send_email("mongodb in " + myaddr + " is down")
        print("email has been sent")

if __name__ == "__main__":
    while True:
        watch()
        time.sleep(10*60)