# -*- coding: utf-8 -*- 
"""
  Thrift服务端示例
"""
import sys, glob
sys.path.append('gen-py')
#sys.path.insert(0, glob.glob('../../lib/py/build/lib.*')[0])
sys.path.insert(0, glob.glob('./lib/py/build/lib*')[0])

from a import  UserServer
from a.ttypes import *


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

SERVER_PORT = 9090

class testHandler:
  def __init__(self):
    self.log = {}

  def getUser(self, userid):
    """
    Parameters:
     - userid
    """
    print("get User")
    # 构造thrift数据结构
    user = User(id=100, name="aa")
    # 返回client
    return  user

handler = testHandler()

# 定义Thrift业务处理逻辑
processor = UserServer.Processor(handler)

transport = TSocket.TServerSocket(port=SERVER_PORT)

# 构造Thrift Factory, 感觉和twisted类似
tfactory = TTransport.TBufferedTransportFactory()

pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print 'Starting the thrift server...'
server.serve()
print 'done.'
