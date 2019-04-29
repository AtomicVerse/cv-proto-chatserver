from gevent.server import StreamServer
from mprpc import RPCServer
import CVPChatServerProtocolClass

class CVPChatServer:
    def __init__(self):
        self.MessageTable = []
    
    def SendMessage(self, TextMessage):
        self.MessageTable.append(TextMessage)
        print(self.MessageTable[-1])

    if __name__ == '__main__':
        ServerEngine = StreamServer(('127.0.0.1', 20181), CVPChatServerProtocolClass.CVPChatServerProtocol())
        print("Server has been started!")
        ServerEngine.serve_forever()