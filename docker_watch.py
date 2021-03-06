# -*- coding: utf-8 -*-
# Furo Yang

import smtplib
import datetime
import os
import time

def send_email(error_msg):
    server = smtplib.SMTP_SSL('smtp.yeah.net',465)
    my_email = 'furo_yang@yeah.net'
    my_password = 'ilcx12345'
    target_email = '17751038730@163.com'

    # send mail
    msg = "\r\n".join([
        "From: " + my_email,
        "To: " + target_email,
        "Subject:  DOCKER DOWN",
        "",
        error_msg
    ])

    server.login(my_email,my_password)
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
    isAlive = "ps -ef | grep docker | grep -v grep | wc -l"
    r = os.popen(isAlive)
    m = r.read()
    m = m.strip()
    r.close()
    if m == '2':
        print "Detected the docker is down"
        myaddr = get_ip()
        send_email("docker in " +  myaddr + " is down")
        print "email hs been sent"

if __name__ == "__main__":
    while True:
        watch()
        time.sleep(10*60)
