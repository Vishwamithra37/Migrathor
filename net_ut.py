import os
from nested_dictionaries import NestedDictionaries as nd
import json

class net_ut:
    def net_id_map():
        with open('./temp/network_list.json','r') as f:
            source_network_list = json.load(f)
        NET_ID_MAP=nd()
        SUBNET_NETWORK_MAP=nd()
        for r in source_network_list:
            NET_ID_MAP[r["Name"]]=r["ID"]
            NET_ID_MAP[r["ID"]]=r["Name"]
        return NET_ID_MAP    
    def subnet_net_map():
        with open('./temp/network_list.json','r') as f:
             source_network_list = json.load(f)
        NET_ID_MAP=nd()
        SUBNET_NETWORK_MAP=nd()
        for r in source_network_list:
            NET_ID_MAP[r["Name"]]=r["ID"]
            NET_ID_MAP[r["ID"]]=r["Name"]
            for i in r["Subnets"]:
                SUBNET_NETWORK_MAP[i]=NET_ID_MAP[r["Name"]]
        return SUBNET_NETWORK_MAP  
    def router_id_map():
        ROUTER_ID_MAP=nd()
        with open('./temp/router_list.json','r') as f:
            source_router_list = json.load(f) 
        for r in source_router_list:
            ROUTER_ID_MAP[r["ID"]]=r["Name"]
            ROUTER_ID_MAP[r["Name"]]=r["ID"]    
        return ROUTER_ID_MAP    
    def router_subnet_map():
        ROUTER_SUBNET_MAP=nd()
        for r in os.listdir('./temp/'):
            if 'router_one' in r:
                with open('./temp/'+r,'r') as f:
                    router_data = json.load(f)
                ROUTER_SUBNET_MAP[router_data["id"]]=[]                    
                if router_data["interfaces_info"]!=[]:
                    for j in router_data["interfaces_info"]:    
                       ROUTER_SUBNET_MAP[router_data["id"]]=[j["subnet_id"]]+ROUTER_SUBNET_MAP[router_data["id"]]                             
      
        return ROUTER_SUBNET_MAP  
    def destination_source_subnet_map():
        e1=net_ut.router_subnet_map()
        des_source_map=nd()
        for r in os.listdir('./destination/'):
            if 'subnet_' in r:
                # print(r)
                for i in e1:
                    for j in e1[i]:          
                        with open('./destination/subnet_'+j+".json",'r') as f:
                              router_data = json.load(f)
                        print(j)      
                        des_source_map[i]=router_data["id"]   
                          
        return des_source_map                 




