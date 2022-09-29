openstack user create migrathor --domain default --password migrathor
openstack role add --project services --user migrathor admin
openstack service create --name migrathor \
  --description "OpenStack deployment tool" migrathor
openstack endpoint create --region RegionOne \
  migrathor public http://192.168.56.1:5001
openstack endpoint create --region RegionOne \
  migrathor internal http://192.168.56.1:5001
openstack endpoint create --region RegionOne \
  migrathor admin http://192.168.56.1:5001   

  
