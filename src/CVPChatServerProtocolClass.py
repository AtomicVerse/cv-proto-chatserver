from mprpc import RPCServer
from CVPChatServerClass import CVPChatServer

CVPChatServer = CVPChatServer()
ChatLog = [""]

class CVPChatServerProtocol(RPCServer):
    
    def SendMessage(self, TextMessage):
        CVPChatServer.SendMessage(TextMessage)
        return True
    
    def GetRecentMessage(self):
        return str(CVPChatServer.MessageTable[-1])
        #return True