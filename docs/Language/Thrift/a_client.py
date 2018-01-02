# -*- coding: utf-8 -*- 
import sys, glob
sys.path.append('gen-py')
#sys.path.insert(0, glob.glob('../../lib/py/build/lib.*')[0])
sys.path.insert(0, glob.glob('./lib/py/build/lib*')[0])

from a import  UserServer
from a.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


try:

  # Make socket
  transport = TSocket.TSocket('localhost', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = UserServer.Client(protocol)

  # Connect!
  transport.open()

  # 业务逻辑
  #client.getUser("111")
  ret = client.getUser("111")
  print ret
  print("Thrift return: userid is %d, username is %s !") % (ret.id, ret.name)

  # Close!
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)
