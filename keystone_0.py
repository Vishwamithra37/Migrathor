import json
from nested_dictionaries import NestedDictionaries as nd
from pprint import pprint as print
import os


def split_take_first(me:str):
    return me.split('@')[0]

# with open('./temp/keypair_list.json','r') as f:
#     source_keypair_list = json.load(f)
# for i in source_keypair_list:
#     os.system("openstack keypair show "+i["Name"]+" -f json> ./temp/key_pairs/"+i["Name"]+".json")
#     os.system("openstack keypair show --public-key "+i["Name"]+" >./temp/key_pair_files/"+i["Name"])

with open('./temp/security_group_list.json','r') as f:
    source_secgr_list = json.load(f)
for i in source_secgr_list:
    os.system("openstack security group show "+i["ID"]+" -f json>"+"./temp/security_groups/"+i["ID"]+".json")
    