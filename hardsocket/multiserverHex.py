'''
@author: William
'''
import SocketServer
import threading
import myCrc
from hardsocket.models import Water_param

# use BaseRequestHandler not StreamRequestHandler
class MyTcpRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print 'connected by: %s' % self.client_address[0]
        while True:
#             try:
                data = self.request.recv(1024)
                if not data:
                    print 'no data received'
                    break
                result = myCrc.exp_data(data)
                # self.request.send(result)
                #TODO use thread to save into db
                # result = data
                # water = Water_param(ph=str(result))
                # water.save()
                # self.request.send('ok')
                self.request.send(result)
#             except:
#                 print 'except happend'
#                 #traceback.print_exc()
#                 break
class MyTcpServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

def openSocket():
    host = ''
    port = 21567
    addr = (host, port)
    print 'server is ready'
    # myServer = SocketServer.ThreadingTCPServer(addr, MyStreamRequestHandler)
    # server.serve_forever()
    myServer = MyTcpServer(addr,MyTcpRequestHandler)
    server_thread = threading.Thread(target=myServer.serve_forever)
    server_thread.daemon = True
    server_thread.start()

def closeSocket():
    host = ''
    port = 21567
    addr = (host, port)
    print 'server is closing'
    myServer = MyTcpServer(addr,MyTcpRequestHandler)
    server_thread = threading.Thread(target=myServer.shutdown)
    server_thread.daemon = True
    server_thread.start()
                
# if __name__ == "__main__":
#     openSocket()
