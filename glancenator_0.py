import json
from pprint import pprint as print
from nested_dictionaries import NestedDictionaries as nd
import os
import key_ut

image_ignore=[]
def split_take_first(me:str):
    return me.split('@')[0]
USER_MAP=key_ut.keystone_ut.user_id_map()    

with open('./temp/image_list.json','r') as f:
    source_image_list = json.load(f)
# print(source_image_list)
os.system("mkdir ./temp/images")
os.system("mkdir ./temp/image_files")
for r in source_image_list:
    print(r["Name"])
    os.system("openstack image show "+r["Name"]+" -f json > ./temp/images/"+r["Name"]+".json")
    os.system("openstack image save --file ./temp/image_files/"+r["Name"]+" "+r["Name"])
