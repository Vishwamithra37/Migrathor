. $1 #source Openstack
# . $2 #destination Openstack
rm -rf ./temp/
rm -rf ./destination/ 
mkdir -p ./temp/
mkdir -p ./destination/
mkdir -p ./temp/key_pairs/
mkdir -p ./temp/key_pair_files/
mkdir -p ./temp/security_groups/

openstack project list -f json > ./temp/project_list.json
openstack user list -f json > ./temp/user_list.json
openstack role list -f json > ./temp/role_list.json
openstack role assignment list --names -f json > ./temp/role_assignment_list.json
openstack keypair list -f json > ./temp/keypair_list
openstack security group list -f json>./temp/security_group_list.json
python3 keystone_0.py
# . $2 Change to second source at this point and run the python3 keystoner.py
#  python3 keystoner.py
# . $1  Changing back to original source

openstack image list -f json > ./temp/image_list.json
python3 glancenator_0.py
# openstack user list -f json

# . $2 Change to second source at this point and run the python3 glancenator.py
#  python3 glancenator.py
# . $1Changing back to original source

openstack network list -f json > ./temp/network_list.json
openstack router list -f json > ./temp/router_list.json
python3 neutronator_0.py
# 