# coding=utf-8
from kazoo.client import KazooClient
import time

zk = KazooClient(hosts='192.168.25.128:2181')
zk.start()
service_lst = []


@zk.ChildrenWatch('/just')
def my_func(children):
    global service_lst
    service_lst = children
    print "my_func"


children = zk.get_children('/just', watch=my_func)
for child in children:
    service_lst.append(child)

while True:
    # print service_lst
    time.sleep(1)

zk.stop()
