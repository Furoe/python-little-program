# -*- coding:utf-8 -*-
#author: Furo Yang


import pymongo
import os
import datetime
import time

WHITE_IP_LIST = ["127.0.0.1", "112.25.236.85", "123.206.99.44", "34.211.14.93", "34.214.28.151", "34.214.30.48",
                 "34.209.2.17", "47.104.8.198", "47.94.247.93", "47.92.72.165", "120.55.53.182", "101.132.100.121",
                 "47.74.6.59", "120.78.148.171", "47.52.154.193", "47.88.154.132", "47.89.245.93", "47.89.183.228",
                 "47.91.89.167", "47.91.106.162"]

#machine ips
#baidu ips
BAIDU_IP = ["106.12.3.82", "182.61.30.147", "180.76.185.62"]

BAIDU_HP_1 = ["58679a3a-b3dd-11e7-ada5-067923e2685c", "3a917432-baee-11e7-ada5-067923e2685c",
              "0819e302-baf0-11e7-ada5-067923e2685c"]
BAIDU_HP_2 = ["74af8c74-b3de-11e7-ada5-067923e2685c", "0ddaf972-baee-11e7-ada5-067923e2685c",
              "804a1186-baef-11e7-ada5-067923e2685c"]
BAIDU_HP_3 = ["54e0fc3c-b3e0-11e7-ada5-067923e2685c", "095d8946-baee-11e7-ada5-067923e2685c",
              "7a83178e-baef-11e7-ada5-067923e2685c"]

BAIDU_ID = {BAIDU_IP[0]: BAIDU_HP_1, BAIDU_IP[1]: BAIDU_HP_2, BAIDU_IP[2]: BAIDU_HP_3}

#aws ips
AWS_IP = ["34.214.28.151", "34.211.14.93"]

AWS_HP_1 = ["da4e16c6-9922-11e7-ada5-067923e2685c", "8d37af8c-9468-11e7-ada5-067923e2685c",
            "b7029cba-96c4-11e7-ada5-067923e2685c"]
AWS_HP_2 = ["7f708090-99db-11e7-ada5-067923e2685c", "1bac99e2-de49-11e7-ada5-067923e2685c",
            "75710c54-96a2-11e7-ada5-067923e2685c"]

AWS_ID = {AWS_IP[0]: AWS_HP_1, AWS_IP[1]: AWS_HP_2}

#ali huadong
ALI_HD_IP = ["120.55.53.182", "101.132.100.121", "47.100.14.13"]

ALI_HP_1 = ["ef90589e-b549-11e7-ada5-067923e2685c", "2cc9e212-badf-11e7-ada5-067923e2685c"]
ALI_HP_2 = ["34962494-b3e4-11e7-ada5-067923e2685c", "a018664c-bae1-11e7-ada5-067923e2685c",
            "a43f02f0-cf2a-11e7-ada5-067923e2685c"]
ALI_HP_3 = ["40ee7df2-c5ca-11e7-ada5-067923e2685c", "cfd92c28-c823-11e7-ada5-067923e2685c",
            "dfbcb4ea-c5dd-11e7-ada5-067923e2685c", "d2ce1d40-cf2a-11e7-ada5-067923e2685c"]

ALI_HD_ID = {ALI_HD_IP[0]: ALI_HP_1, ALI_HD_IP[1]: ALI_HP_2, ALI_HD_IP[2]: ALI_HP_3}

#ali huanan
ALI_HN_IP = ["120.78.148.171", "120.78.219.180"]

ALI_HP_4 = ["86707d40-b3c7-11e7-ada5-067923e2685c", "eeae56f8-bae2-11e7-ada5-067923e2685c"]
ALI_HP_5 = ["b4028528-c5c9-11e7-ada5-067923e2685c", "7b8ccbc4-c5e5-11e7-ada5-067923e2685c",
            "7c0e6a36-cf2b-11e7-ada5-067923e2685c"]

ALI_HN_ID = {ALI_HN_IP[0]: ALI_HP_4, ALI_HN_IP[1]: ALI_HP_5}

#ali HK
ALI_HK_IP = ["47.52.154.193", "47.89.18.42"]

Ali_HP_6 = ["59b5ec5c-b3c9-11e7-ada5-067923e2685c", "41f5d692-babb-11e7-ada5-067923e2685c",
            "dfd6fc92-bac0-11e7-ada5-067923e2685c", "bbb73f5a-cf2b-11e7-ada5-067923e2685c",
            "6291c32a-de51-11e7-ada5-067923e2685c"]
ALI_HP_7 = ["ea0cc5e4-c5e6-11e7-ada5-067923e2685c", "22ff99aa-c81a-11e7-ada5-067923e2685c",
            "c9beafd2-c81b-11e7-ada5-067923e2685c", "2e13f362-cf2d-11e7-ada5-067923e2685c",
            "56a04fd6-da47-11e7-ada5-067923e2685c"]

ALI_HK_ID = {ALI_HK_IP[0]: Ali_HP_6, ALI_HK_IP[1]: ALI_HP_7}

#ali Singapore
ALI_SG_IP = ["47.88.154.132", "47.88.170.57"]

ALI_HP_8 = ["2c59f4cc-b3cb-11e7-ada5-067923e2685c", "264c0f28-bae4-11e7-ada5-067923e2685c",
            "f6d28e56-bae4-11e7-ada5-067923e2685c", "5b23a802-cf2d-11e7-ada5-067923e2685c"]
ALI_HP_9 = ["7ddb9ace-c5e8-11e7-ada5-067923e2685c", "6b675ef6-c817-11e7-ada5-067923e2685c",
            "2874f8a8-c815-11e7-ada5-067923e2685c", "fb2cce28-cf2d-11e7-ada5-067923e2685c"]

ALI_SG_ID = {ALI_SG_IP[0]: ALI_HP_8, ALI_SG_IP[1]: ALI_HP_9}

#ali Japan
ALI_JP_IP = ["47.74.6.59", "47.74.22.151", "47.74.14.5"]

ALI_HP_10 = ["ad26d826-b796-11e7-ada5-067923e2685c", "2919f77a-cf2e-11e7-ada5-067923e2685c"]
ALI_HP_11 = ["56b6db10-c5e9-11e7-ada5-067923e2685c", "4e156a96-c812-11e7-ada5-067923e2685c",
             "706439fa-c813-11e7-ada5-067923e2685c", "5165760a-cf2e-11e7-ada5-067923e2685c"]
ALI_HP_12 = ["bd8e1758-c5ea-11e7-ada5-067923e2685c", "7570a30c-c5ed-11e7-ada5-067923e2685c",
             "72913580-cf2e-11e7-ada5-067923e2685c"]

ALI_JP_ID = {ALI_JP_IP[0]: ALI_HP_10, ALI_JP_IP[1]: ALI_HP_11, ALI_JP_IP[2]: ALI_HP_12}

#ali north of America
ALI_WA_IP = ["47.89.245.93", "47.89.254.223"]

ALI_HP_13 = ["9f375848-b3cd-11e7-ada5-067923e2685c", "fcc48bd8-bae5-11e7-ada5-067923e2685c",
             "cdb08396-bae6-11e7-ada5-067923e2685c", "c2d254fc-cf2e-11e7-ada5-067923e2685c"]
ALI_HP_14 = ["be6a87f2-c5ee-11e7-ada5-067923e2685c", "d50efcd0-c5ef-11e7-ada5-067923e2685c",
             "a45e92de-c5f0-11e7-ada5-067923e2685c", "38963438-cf2f-11e7-ada5-067923e2685c"]

ALI_WA_ID = {ALI_WA_IP[0]: ALI_HP_13, ALI_WA_IP[1]: ALI_HP_14}

#ali east of America
ALI_EA_IP = ["47.89.183.228", "47.89.176.77"]

ALI_HP_15 = ["1295f0b4-b3cf-11e7-ada5-067923e2685c", "3e4e6e02-bae6-11e7-ada5-067923e2685c",
             "e86e9542-bae6-11e7-ada5-067923e2685c", "f21cc80a-cf2e-11e7-ada5-067923e2685c"]
ALI_HP_16 = ["83375310-c5f1-11e7-ada5-067923e2685c", "71db9dbe-c5f7-11e7-ada5-067923e2685c",
             "48bb37f2-c5fa-11e7-ada5-067923e2685c", "75be5de0-cf2f-11e7-ada5-067923e2685c"]

ALI_EA_ID = {ALI_EA_IP[0]: ALI_HP_15, ALI_EA_IP[1]: ALI_HP_16}

#ali Europe
ALI_EU_IP = ["47.91.89.167", "47.91.88.239"]

ALI_HP_17 = ["1c71776c-b3d3-11e7-ada5-067923e2685c", "0676a8b8-babf-11e7-ada5-067923e2685c",
             "41456e86-d4b2-11e7-ada5-067923e2685c", "b47b243a-bab4-11e7-ada5-067923e2685c"]
ALI_HP_18 = ["622ea50c-c825-11e7-ada5-067923e2685c", "703e7f58-c83b-11e7-ada5-067923e2685c",
             "99585008-c836-11e7-ada5-067923e2685c", "6ddc4748-cf31-11e7-ada5-067923e2685c"]

ALI_EU_ID = {ALI_EU_IP[0]: ALI_HP_17, ALI_EU_IP[1]: ALI_HP_18}

#ali Middle East
ALI_ME_IP = ["47.91.106.162", "47.91.104.232"]

ALI_HP_19 = ["9e1d2af2-b3d5-11e7-ada5-067923e2685c", "5c0daf76-baea-11e7-ada5-067923e2685c",
             "53545242-bae8-11e7-ada5-067923e2685c", "a6844ffa-cf31-11e7-ada5-067923e2685c"]
ALI_HP_20 = ["bd835dba-c5f2-11e7-ada5-067923e2685c", "ed73d754-c5f5-11e7-ada5-067923e2685c",
             "e0a45fdc-c5f3-11e7-ada5-067923e2685c", "d413bbea-cf31-11e7-ada5-067923e2685c"]

ALI_ME_ID = {ALI_ME_IP[0]: ALI_HP_19, ALI_ME_IP[1]: ALI_HP_20}

#ali huabei
ALI_HB_IP_1 = ["47.104.8.198", "47.94.247.93", "47.92.72.165", "39.106.103.19", "47.104.31.23",
             "47.92.167.242"]
ALI_HB_IP = ["47.92.72.165", "47.104.31.23", "47.92.167.242"]
ALI_HP_21 = ["9efa765e-b3ae-11e7-ada5-067923e2685c", "751f183e-bada-11e7-ada5-067923e2685c",
             "e6f1ffb8-cf24-11e7-ada5-067923e2685c"]
ALI_HP_22 = ["959b98f4-b3b3-11e7-ada5-067923e2685c", "fae4d392-bad9-11e7-ada5-067923e2685c",
             "ae0c68da-bac7-11e7-ada5-067923e2685c"]
ALI_HP_23 = ["a991f176-b3b5-11e7-ada5-067923e2685c", "38662fca-badc-11e7-ada5-067923e2685c",
             "e07ab36a-badd-11e7-ada5-067923e2685c", "dab3dcb4-cf27-11e7-ada5-067923e2685c"]
ALI_HP_24 = ["37e3078e-c5be-11e7-ada5-067923e2685c", "89ab7fd8-c83e-11e7-ada5-067923e2685c",
             "d2821aa4-cf29-11e7-ada5-067923e2685c"]
ALI_HP_25 = ["2c26c2c4-c5c2-11e7-ada5-067923e2685c", "b1db36da-c83c-11e7-ada5-067923e2685c",
             "c6445e92-c5c3-11e7-ada5-067923e2685c", "0f02690c-cf2a-11e7-ada5-067923e2685c"]
ALI_HP_26 = ["ebcc891c-c5c5-11e7-ada5-067923e2685c", "54b83d32-c840-11e7-ada5-067923e2685c",
             "5cd82c96-c842-11e7-ada5-067923e2685c", "5e6ad6be-cf2a-11e7-ada5-067923e2685c"]

ALI_HB_ID = {ALI_HB_IP[0]: ALI_HP_23, ALI_HB_IP[1]: ALI_HP_25, ALI_HB_IP[2]: ALI_HP_26}

#Tencent Beijing
TENCENT_BJ_IP = ["58.87.77.160", "118.89.219.238"]

TENCENT_HP_1 = ["e34ec390-babc-11e7-ada5-067923e2685c", "afb9ba48-b53b-11e7-ada5-067923e2685c"]
TENCETN_HP_2 = ["261f1da0-b55e-11e7-ada5-067923e2685c", "77dad4f4-bea5-11e7-ada5-067923e2685c",
                "d754de9c-bea6-11e7-ada5-067923e2685c", "b19060fc-cf34-11e7-ada5-067923e2685c"]

TENCENT_BJ_ID = {TENCENT_BJ_IP[0]: TENCENT_HP_1, TENCENT_BJ_IP[1]: TENCETN_HP_2}

#Tencent Guangzhou
TENCENT_GZ_IP = ["123.207.56.142", "123.207.93.135", "111.230.166.192"]

TENCENT_HP_3 = ["e863c3cc-b557-11e7-ada5-067923e2685c", "c1f4e9de-bafa-11e7-ada5-067923e2685c",
                "120dc634-bafb-11e7-ada5-067923e2685c", "ba505432-cf33-11e7-ada5-067923e2685c"]
TENCENT_HP_4 = ["1f86388e-b559-11e7-ada5-067923e2685c", "42a31f6a-bea2-11e7-ada5-067923e2685c",
                "c209d5b0-bea6-11e7-ada5-067923e2685c", "d28ce830-cf33-11e7-ada5-067923e2685c"]
TENCENT_HP_5 = ["79c76a56-b55a-11e7-ada5-067923e2685c", "d7068c0e-bea3-11e7-ada5-067923e2685c",
                "c4af68ca-bea6-11e7-ada5-067923e2685c", "1beac628-cf34-11e7-ada5-067923e2685c"]

TENCENT_GZ_ID = {TENCENT_GZ_IP[0]: TENCENT_HP_3, TENCENT_GZ_IP[1]: TENCENT_HP_4, TENCENT_GZ_IP[2]: TENCENT_HP_5}

#Tencent Shanghai
TENCENT_SH_IP = ["115.159.24.114", "122.152.209.179"]

TENCENT_HP_6 = ["6c7a7530-b55c-11e7-ada5-067923e2685c", "6e3039ee-bea5-11e7-ada5-067923e2685c",
                "c9311f2e-bea6-11e7-ada5-067923e2685c", "2806eca2-cf34-11e7-ada5-067923e2685c"]
TENCENT_HP_7 = ["00da5fa4-b564-11e7-ada5-067923e2685c", "70df7524-bea5-11e7-ada5-067923e2685c",
                "cefaad58-bea6-11e7-ada5-067923e2685c", "4722d93e-cf34-11e7-ada5-067923e2685c"]

TENCENT_SH_ID = {TENCENT_SH_IP[0]: TENCENT_HP_6, TENCENT_SH_IP[1]: TENCENT_HP_7}

hp_db_conn = pymongo.MongoClient('127.0.0.1', 27017)
hp_db = hp_db_conn.mnemosyne
hp_db_collection = hp_db.session

class coincident():
    def __init__(self):
        pass

    #Analysis 2 machines in the same area
    def get_area2_ips(self, dt_y, dt, Area_ID):
        info = hp_db_collection.find({"timestamp":{"$gte": dt_y, "$lte": dt}})
        dic = {}
        for ma in Area_ID.keys():
            dic[ma] = []
        for item in info:
            hp_id = item.get("identifier")
            for ma in dic.keys():
                if hp_id in Area_ID[ma]:
                    source_ip = item.get("source_ip")
                    if source_ip not in WHITE_IP_LIST:
                        dic[ma].append(source_ip)
        set2 = {}
        for ma in dic.keys():
            set2[ma] = list(set(dic[ma]))
        self.dic2 = set2

    def count_area2_rate(self, Area_IP):
        a1 = self.dic2[Area_IP[0]]
        a2 = self.dic2[Area_IP[1]]
        a3 = []
        for ip in a1:
            if ip in a2:
                a3.append(ip)
        r1 = format(float(len(a3))/(int(len(a1)) + int(len(a2)) - int(len(a3))), '0.6%')

        print r1
        del self.dic2

    #Analysis 3 machine in the same area
    def get_area3_ips(self, dt_y, dt, Area_ID):
        info = hp_db_collection.find({"timestamp": {"$gte": dt_y, "$lte": dt}})
        dic = {}
        for ma in Area_ID.keys():
            dic[ma] = []
        for item in info:
            hp_id = item.get("identifier")
            for ma in dic.keys():
                if hp_id in Area_ID[ma]:
                    source_ip = item.get("source_ip")
                    if source_ip not in WHITE_IP_LIST:
                        dic[ma].append(source_ip)
        set3 = {}
        for ma in dic.keys():
            set3[ma] = list(set(dic[ma]))
        self.dic3 = set3

    def count_area3_rate(self, Area_IP):
        b1 = self.dic3[Area_IP[0]]
        print Area_IP[0]
        b2 = self.dic3[Area_IP[1]]
        print Area_IP[1]
        b3 = self.dic3[Area_IP[2]]
        print Area_IP[2]
        b4 = []
        b5 = []
        for ip in b1:
            if ip in b2:
                b4.append(ip)
        r1 = format(float(len(b4))/(int(len(b1)) + int(len(b2)) - int(len(b4))), '0.6%')
        print r1
        for ip1 in b1 or b2:
            if ip1 not in b4 and ip1 in b3:
                b5.append(ip1)
        r2 = format(float(len(b5))/(int(len(b1)) + int(len(b2)) + int(len(b3)) - 2*int(len(b4)) - int(len(b5))), '0.6%')
        print r2
        del self.dic3


if __name__ == "__main__":
    date = datetime.datetime.utcnow()
    dt = date + datetime.timedelta(hours=-date.hour, minutes=-date.minute, seconds=-date.second,
                                   microseconds=-date.microsecond)
    date_y = dt + datetime.timedelta(days=-1)

    cd = coincident()
    print "AWS"
    cd.get_area2_ips(date_y, dt, AWS_ID)
    cd.count_area2_rate(AWS_IP)
    print "Baidu"
    cd.get_area3_ips(date_y, dt, BAIDU_ID)
    cd.count_area3_rate(BAIDU_IP)
    print "Ali huanan"
    cd.get_area2_ips(date_y, dt, ALI_HN_ID)
    cd.count_area2_rate(ALI_HN_IP)
    print "Ali huabei"
    cd.get_area3_ips(date_y, dt, ALI_HB_ID)
    cd.count_area3_rate(ALI_HB_IP)
    print "Ali Hongkong"
    cd.get_area2_ips(date_y, dt, ALI_HK_ID)
    cd.count_area2_rate(ALI_HK_IP)
    print "Ali Singapore"
    cd.get_area2_ips(date_y, dt, ALI_SG_ID)
    cd.count_area2_rate(ALI_SG_IP)
    print "Ali Japan"
    cd.get_area3_ips(date_y, dt, ALI_JP_ID)
    cd.count_area3_rate(ALI_JP_IP)
    print "Ali West of America"
    cd.get_area2_ips(date_y, dt, ALI_WA_ID)
    cd.count_area2_rate(ALI_WA_IP)
    print "Ali East of America"
    cd.get_area2_ips(date_y, dt, ALI_EA_ID)
    cd.count_area2_rate(ALI_EA_IP)
    print "Ali Europe"
    cd.get_area2_ips(date_y, dt, ALI_EU_ID)
    cd.count_area2_rate(ALI_EU_IP)
    print "Ali Middle East"
    cd.get_area2_ips(date_y, dt, ALI_ME_ID)
    cd.count_area2_rate(ALI_ME_IP)
    print "ALi huadong"
    cd.get_area3_ips(date_y, dt, ALI_HD_ID)
    cd.count_area3_rate(ALI_HD_IP)
    print "Tencent Beijing"
    cd.get_area2_ips(date_y, dt, TENCENT_BJ_ID)
    cd.count_area2_rate(TENCENT_BJ_IP)
    print "Tencent Guangzhou"
    cd.get_area3_ips(date_y, dt, TENCENT_GZ_ID)
    cd.count_area3_rate(TENCENT_GZ_IP)
    print "Tencent Shanghai"
    cd.get_area2_ips(date_y, dt, TENCENT_SH_ID)
    cd.count_area2_rate(TENCENT_SH_IP)
