import os
from nested_dictionaries import NestedDictionaries as nd
import json

class keystone_ut:
    def user_id_map():
        with open('./temp/user_list.json','r') as f:
            source_user_list = json.load(f)
            USER_MAP=nd()
        for r in source_user_list:
                USER_MAP[r["Name"]]=r["ID"]
                USER_MAP[r["ID"]]=r["Name"]
        return USER_MAP   
    def project_id_map():
        PROJ_MAP=nd()
        with open('./temp/project_list.json','r') as f:
              source_project_list = json.load(f)
        for r in source_project_list:
              PROJ_MAP[r["Name"]]=r["ID"]
              PROJ_MAP[r["ID"]]=r["Name"]
        return PROJ_MAP      
                