import json
from pprint import pprint as print
from nested_dictionaries import NestedDictionaries as nd
import os
proj_ignore=[
    "service","admin"
]
user_ignore=[
    "admin","glance","neutron","placement","nova","heat","zun","heat_domain_admin","kuryr"
]
def split_take_first(me:str):
    return me.split('@')[0]

with open('./temp/project_list.json','r') as f:
    source_project_list = json.load(f)
ID_PROJECT_LIST=[]
for r in source_project_list:
         if r["Name"] in proj_ignore:
            pass
         else:
            ID_PROJECT_LIST.append(r["Name"])
for r in ID_PROJECT_LIST:      
            # os.system() Enter the line to change to destination      
            os.system('openstack project create '+r)            

with open('./temp/role_assignment_list.json','r') as f:
    source_role_assignment_list = json.load(f)
ROLE_ASSIGNMENT_MAP=nd()
for r in source_role_assignment_list:
         ROLE_ASSIGNMENT_MAP[split_take_first(r["User"])][split_take_first(r["Project"])]=[]
for r in source_role_assignment_list:         
         ROLE_ASSIGNMENT_MAP[split_take_first(r["User"])][split_take_first(r["Project"])].append(r["Role"])

for r in ROLE_ASSIGNMENT_MAP:
    if r not in user_ignore:
        os.system('openstack user create '+r+' --password ubuntu')
        for r2 in ROLE_ASSIGNMENT_MAP[r]:
             for r3 in ROLE_ASSIGNMENT_MAP[r][r2]:
                    print(r3)
                    os.system('openstack role add --project '+r2+' --user '+r+' '+r3 )

# os.system('openstack user create a2 --password ubuntu')
# os.system('openstack role add member --project a1_project --user a2')


     

# with open('./temp/role_list.json','r') as f:
#     source_role_list = json.load(f)
# ROLE_ID_MAP=nd()
# for r in source_role_list:
#          ROLE_ID_MAP[r["Name"]]=r["ID"]
#          ROLE_ID_MAP[r["ID"]]=r["Name"]

# with open('./temp/user_list.json','r') as f:
#     source_user_list = json.load(f)
# USER_MAP=nd()
# for r in source_user_list:
#             USER_MAP[r["Name"]]=r["ID"]
#             USER_MAP[r["ID"]]=r["Name"]


# print(ROLE_ID_MAP)
# print(ID_PROJECT_MAP)
# openstack role assignment list --help