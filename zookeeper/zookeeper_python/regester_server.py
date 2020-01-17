# coding=utf-8
from kazoo.client import KazooClient
import time

zk = KazooClient(hosts='192.168.25.128:2181')
zk.start()


def test_ensure():
    zk.ensure_path('/my/favorite')
def test_create():
    # nodename="/kwsy0000000019"
    # zk.create(nodename, '123.56.190.151_{index}'.format(index=1), makepath=True,ephemeral=True, sequence=True)
    # child_node=zk.get_children("/")
    # print child_node
    nodename = '/kwsy/serviceasdf'
    index=0
    while index < 1:
        zk.create(nodename, '123.56.190.151_{index}'.format(index=index),makepath=True, ephemeral=True, sequence=True)
        # time.sleep(10)
        index += 1
    node_li=zk.get_children('/kwsy')
    print node_li
    for i in node_li:
        if i=="zookeeper":
            continue
        # print zk.get("/kwsy/{0}".format(i))
        # zk.delete("/kwsy/{0}".format(i))
    node_li = zk.get_children('/kwsy')
    print node_li
def setData(zk,root,node,data):
    zk.create(node,data,makepath=True,sequence=True,ephemeral=True)
    real_node=zk.get_children(root)

    index=1
    while(index):
        for i in real_node:
            all_node=root+"/"+i
            new_data="{0}_{1}".format(data,index)
            zk.set(all_node,new_data)
            print zk.get(all_node)
        time.sleep(1)
        index+=1

if __name__ == '__main__':
    # zk.delete('/kwsy')
    # test_create()
    setData(zk,"/just","/just/for","use")
    zk.stop()
