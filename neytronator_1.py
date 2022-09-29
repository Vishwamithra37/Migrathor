import json
from pprint import pprint as print
from nested_dictionaries import NestedDictionaries as nd
import os
import net_ut
import key_ut


net_ignore=[
    "public1"
]
external_gateway_network_name="public1"

def split_take_first(me:str):
    return me.split('@')[0]
PROJ_MAP=key_ut.keystone_ut.project_id_map()
NET_ID_MAP=net_ut.net_ut.net_id_map()
ROUTER_ID_MAP=net_ut.net_ut.router_id_map()
ROUTER_SUBNET_MAP=net_ut.net_ut.router_subnet_map()
counter=1
for r in os.listdir('./temp/'):
    if counter==0:
       pass
    else: 
     if 'network_one' in r:
        with open('./temp/'+r,'r') as f:
                network_data = json.load(f)
        # print(network_data["admin_state_up"]) 
        # print(PROJ_MAP[network_data["project_id"]]) 
        # print(network_data["name"])
        if network_data["name"] not in net_ignore:
            if network_data["shared"]==False:
                shared="no-share"
                # print("jiji")
            else:
                shared="share" 
            if network_data["port_security_enabled"]==True:
                psecurity="enable-port-security"
            else:
                psecurity="disable-port-security"        
            os.system("openstack network create --project "+
            PROJ_MAP[network_data["project_id"]]+" --mtu "+
            str(network_data["mtu"])+" --description migrathor_"+
            network_data["description"]+" --"+shared+" --"+psecurity+" "+
            network_data["name"]+" -f json > ./destination/network_"+network_data["id"]+".json"
            )

for r in os.listdir('./temp/'):
    if counter==0:
        pass
    else:
     if 'subnet_one' in r:
        with open('./temp/'+r,'r') as f:
                subnet_data = json.load(f)

        if subnet_data["enable_dhcp"]==False:
                dhcp="no-dhcp"
        else:
                dhcp="dhcp"        
        os.system("openstack subnet create --project "+
        PROJ_MAP[subnet_data["project_id"]]+" --subnet-range "+
        subnet_data["cidr"]+" --description migrathor_"+
        network_data["description"]+" --"+dhcp+" --gateway "+
        subnet_data["gateway_ip"]+" --network "+
        NET_ID_MAP[subnet_data["network_id"]]+" --allocation-pool start="+
        subnet_data["allocation_pools"][0]["start"]+",end="+
        subnet_data["allocation_pools"][0]["start"]+" "+
        subnet_data["name"]+" -f json > ./destination/subnet_"+subnet_data["id"]+".json"
        )


for r in os.listdir('./temp/'):
    if counter==0:
     pass
    else:
     if 'router_one' in r:
        with open('./temp/'+r,'r') as f:
                router_data = json.load(f)
        print(router_data)
        if router_data["ha"]==False:
                ha="ha"
        else:
                ha="no-ha"  
        if router_data["external_gateway_info"]!=None:            
            if router_data["external_gateway_info"]["enable_snat"]==False:
                    snat="enable-snat"
            else:
                    ha="disable-snat"
            os.system("openstack router create --project "+
        PROJ_MAP[router_data["project_id"]]+" --external-gateway "+
        external_gateway_network_name+" --description migrathor_"+
        router_data["description"]+" "+
        router_data["name"]+" -f json>./destination/router_"+router_data["id"]+".json"
        )          
        else:
            os.system("openstack router create --project "+
        PROJ_MAP[router_data["project_id"]]+" --description migrathor_"+
        router_data["description"]+" "+
        router_data["name"]+" -f json>./destination/router_"+router_data["id"]+".json"
        )
        
        with open('./destination/router_'+router_data["id"]+'.json','r') as f:
                router_data2 = json.load(f)
        print(ROUTER_SUBNET_MAP)        
        for i in ROUTER_SUBNET_MAP: 
            for j in ROUTER_SUBNET_MAP[i]: 
                 print(ROUTER_SUBNET_MAP[i])   
                 os.system("openstack router add subnet "+router_data2["id"]+" "+j
                           )        
 







