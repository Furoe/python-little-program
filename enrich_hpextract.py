import pymongo
import os
import time
import datetime

WHITE_IP_LIST = ["127.0.0.1","112.25.236.85","123.206.99.44","34.211.14.93","34.214.28.151","34.214.30.48","34.209.2.17"]
save_path = './mhn/temp/'

hp_db_conn = pymongo.MongoClient('127.0.0.1',27017)
hp_db = hp_db_conn.mnemosyne
hp_db_collection = hp_db.session
#hp_ip_enrich = hp_db_collection.ip

class enrich():
    def __init__(self):
        pass

    # read from mongo
    def get_hp_info(self,utc_date_y,utc_date):

        # get one day
        find = hp_db_collection.find({"timestamp":{"$gte":utc_date_y,"$lte":utc_date}})

        hp_dic = {}
        for item in find:
            hp = item.get("honeypot")
            if hp_dic.get(hp) is None:
                hp_dic[hp] = []
            source_ip = item.get("source_ip")
            # add ip not in while ip list
            if source_ip not in WHITE_IP_LIST:
                hp_dic[hp].append(source_ip)
            hp_set = {}
        for hp_type in hp_dic.keys():
            hp_set[hp_type] = list(set(hp_dic[hp_type]))
        self.hp_dic = hp_set
        return hp_set

    # count ips in one day caught by all kinds of hp
    def hp_ip_count(self,date):
        logtime = date.strftime('%Y-%m-%d')
        filename = save_path + logtime
        for x in self.hp_dic.keys():
            hp_ip_num = len(self.hp_dic.get(x))
            with open(filename,'a') as f:
                f.writelines(x + ':' + str(hp_ip_num) + '\n')
        f.close()

    # get one week
    def get_hp_week_info(self,utc_date_w,utc_date):

        # get one week
        week_find = hp_db_collection.find({"timestamp": {"$gte": utc_date_w, "$lte": utc_date}})

        week_hp_dic = {}
        for item in week_find:
            hp = item.get("honeypot")
            if week_hp_dic.get(hp) is None:
                week_hp_dic[hp] = []
            source_ip = item.get("source_ip")
            # add ip not in while ip list
            if source_ip not in WHITE_IP_LIST:
                week_hp_dic[hp].append(source_ip)
            week_hp_set = {}
        for hp_type in week_hp_dic.keys():
            week_hp_set[hp_type] = list(set(week_hp_dic[hp_type]))
        self.week_hp_dic = week_hp_set
        return week_hp_set



    # count enrich ips
    def count_enrich(self,date):
        hp_enrich_dic = {}
        logtime = date.strftime('%Y-%m-%d')
        filename = save_path + 'week_' + logtime
        for x in self.hp_dic.keys():
            hp_enrich_dic[x] = []
            for ip in self.hp_dic[x]:
                if x in self.week_hp_dic.keys():
                    if ip not in self.week_hp_dic[x]:
                        hp_enrich_dic[x].append(ip)
            with open(filename,'a') as d:
                d.writelines(x + ':' + str(len(hp_enrich_dic[x])) + '\n')
        d.close()

    # get amount
    def get_ip_amount(self, utc_date):

        # get all
        amount_find = hp_db_collection.find({"timestamp": {"$lte": utc_date}})

        amount_hp_dic = {}
        for item in amount_find:
            hp = item.get("honeypot")
            if amount_hp_dic.get(hp) is None:
                amount_hp_dic[hp] = []
            source_ip = item.get("source_ip")
            # add ip not in while ip list
            if source_ip not in WHITE_IP_LIST:
                amount_hp_dic[hp].append(source_ip)
        amount_hp_set = {}
        for hp_type in amount_hp_dic.keys():
            amount_hp_set[hp_type] = list(set(amount_hp_dic[hp_type]))
            if cmp(hp_type.lower(), "p0f") == 0:
                p0fips = amount_hp_set[hp_type]
                amount_hp_set[hp_type] = []
                for ip in p0fips:
                    if amount_hp_dic[hp_type].count(ip) >= 20:
                        amount_hp_set[hp_type].append(ip)
        self.amount_hp_dic = amount_hp_set
        return amount_hp_set

    # count amount
    def count_amount(self):
        sum = 0
        for x in self.amount_hp_dic.keys():
            print x
            print len(self.amount_hp_dic[x])

if __name__ == "__main__":
    date = datetime.datetime.utcnow() + datetime.timedelta(days=-9)
    dt = date + datetime.timedelta(hours=-date.hour,minutes=-date.minute,seconds=-date.second,microseconds=-date.microsecond)
    date_y = dt + datetime.timedelta(days=-1)
    date_w = dt + datetime.timedelta(days=-8)

    print date
    print dt
    print 'I\'m running'
    enrich_case = enrich()
    #hp = enrich_case.get_hp_info(date_y,dt)
    #week_hp = enrich_case.get_hp_week_info(date_w,date_y)
    #enrich_case.hp_ip_count(dt)
    #enrich_case.count_enrich(dt)
    amount = enrich_case.get_ip_amount(dt)
    enrich_case.count_amount()
    print 'data count is over'
