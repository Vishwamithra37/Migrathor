import json
from pprint import pprint as print
from nested_dictionaries import NestedDictionaries as nd
import os
import key_ut


image_ignore=[]
def split_take_first(me:str):
    return me.split('@')[0]
PROJ_MAP=key_ut.keystone_ut.project_id_map()   

with open('./temp/image_list.json','r') as f:
    source_image_list = json.load(f)
# print(source_image_list)
for r in os.listdir('./temp/images'):
    with open('./temp/images/'+r,'r') as f:
       image_data = json.load(f)
    # print(image_data["container_format"])   
    # print(image_data["disk_format"])
    # print(image_data["visibility"])
    # print(PROJ_MAP[image_data["owner"]])  
    # print(image_data["name"])    
    os.system('openstack image create \
               --container-format '+image_data["container_format"]+
              ' --disk-format '+image_data["disk_format"]+
              ' --project '+PROJ_MAP[image_data["owner"]]+
              ' --'+image_data["visibility"]+
              ' --file ./temp/image_files/'+image_data["name"]+
            #   Add more properties if required
              ' '+image_data["name"]+" -f json > ./destination/image_one_"+image_data["id"]+".json")
# List the stuff.