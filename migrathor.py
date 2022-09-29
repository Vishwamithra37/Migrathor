import os
import openstack
from pprint import pprint as print
from nested_dictionaries import NestedDictionaries as nd
import json
conn = openstack.connect(cloud='source_openstack')
project_dictionary=nd()
user_dictionary=nd()
role_dictionary=nd()
# conn2 = openstack.connect(cloud='destination_openstack')
class keystone_migrator():
    def get_projects():
        counter=0
        for user in conn.identity.projects():
           project_dictionary[counter]=user
           counter+=1
        return project_dictionary
    def get_users():
        counter=0
        for user in conn.identity.create_user():
            user_dictionary[counter]=user     
            counter+=1
        print(user_dictionary)    
        return user_dictionary 
    def get_roles():
        counter=0
        for role in conn.identity.roles():
            role_dictionary[counter]=role
            counter+=1
        print(role_dictionary)
        return role_dictionary
    def get_credentials(): 
        counter=0
        for credential in conn.identity.credentials():
         print(credential)    
    def list_role_domain_user_assignments():
      print("List Roles assignments for a user on domain:")
    #   for role in conn.identity.role_project_user_assignments():
        # print(role)  
    #   for role in conn.identity.role_project_group_assignments():
        # print(role)                   
# print(project_dictionary)   
# with open() as a1:
#   b2=json.loads(a1)
#   print(a1)
with open('./temp/project_list.json','r') as f:
    data = json.load(f)
    
print(data)
    
    
    
   
# keystone_migrator.get_projects()
# keystone_migrator.get_users()
# keystone_migrator.get_roles()
# keystone_migrator.get_credentials()
# keystone_migrator.list_role_domain_user_assignments()