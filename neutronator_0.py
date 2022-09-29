import json
from pprint import pprint as print
from nested_dictionaries import NestedDictionaries as nd
import os
import key_ut

net_ignore=[
    "public"
]

def split_take_first(me:str):
    return me.split('@')[0]

with open('./temp/network_list.json','r') as f:
    source_network_list = json.load(f)
NET_ID_MAP=nd()
SUBNET_NETWORK_MAP=nd()
ROUTER_ID_MAP=nd()
counter=0
for r in source_network_list:
    NET_ID_MAP[r["Name"]]=r["ID"]
    NET_ID_MAP[r["ID"]]=r["Name"]
    os.system("openstack network show "+r["ID"]+" -f json > ./temp/network_one_"+r["ID"]+".json")
    for i in r["Subnets"]:
        SUBNET_NETWORK_MAP[i]=NET_ID_MAP[r["Name"]]
        # os.system("openstack subnet show "+i+" -f json > ./temp/subnet_one_"+r["ID"]+".json")
        os.system("openstack subnet show "+i+" -f json > ./temp/subnet_one_"+i+".json")

with open('./temp/router_list.json','r') as f:
    source_router_list = json.load(f)
PROJ_MAP=key_ut.keystone_ut.project_id_map()    
for r in source_router_list:
    ROUTER_ID_MAP[r["ID"]]=r["Name"]
    ROUTER_ID_MAP[r["Name"]]=r["ID"]
    os.system("openstack router show "+r["ID"]+" -f json > ./temp/router_one_"+r["ID"]+".json")
# print(NET_ID_MAP) 
# print(SUBNET_NETWORK_MAP) 