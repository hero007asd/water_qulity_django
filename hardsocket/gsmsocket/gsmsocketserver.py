# -*- coding: UTF-8 -*-
'''
@author: William
socket server
sending with ascii
'''
import SocketServer
import threading
import logging
import datahandle

log = logging.getLogger('socket.crc')
# use BaseRequestHandler not StreamRequestHandler
class MyTcpRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        log.info('connected by: %s' % self.client_address[0])
        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                    log.warn('no data received,close client')
                    break
                print data
                result = datahandle.handle_data(data)
                self.request.send(result)
            except Exception,e:
                # log = logging.getLogger('socket.crc')
                log.exception(e)
                # print e
                # break
class MyTcpServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

def openSocket():
    host = ''
    port = 21567
    addr = (host, port)
    log.info('server is ready')
    myServer = MyTcpServer(addr,MyTcpRequestHandler)
    server_thread = threading.Thread(target=myServer.serve_forever)
    server_thread.daemon = True
    server_thread.start()

if __name__=='__main__':
    openSocket()



