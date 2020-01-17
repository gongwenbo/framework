from kazoo.client import KazooClient

def createNode():
    zk = KazooClient(hosts='192.168.25.128:2181')
    zk.start()
    zk.create('/0001ddd/asdf',b'this is my house',makepath=True,sequence=True,ephemeral=True)
    # zk.delete('/0001ddddd', recursive=True)
    # zk.set('xyz30000000014', b"this is safsaf my horse!")
    node = zk.get_children('/')
    print(node)
    zk.stop()
if __name__=="__main__":
    createNode()
