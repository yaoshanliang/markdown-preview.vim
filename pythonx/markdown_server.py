#!/usr/bin/python
import socket
import markdown_preview
import threading
import sys
import time

class Server(threading.Thread):

    def Response(self, header, content):
        response = "%s %d\r\n\r\n%s\r\n\r\n" % (header, sys.maxint, content)
        return response

    def isOK(self):
        return self.isOk

    def __init__(self, port):
        try:
            try:
                self.lisfd.close()
            except Exception:
                pass
            self.PORT = port
            self.HOST = "localhost"

            self.lisfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.lisfd.bind((self.HOST, self.PORT))
            self.lisfd.listen(10)
            self.isOk = True
            threading.Thread.__init__(self)
        except Exception as e:
            self.isRun = False
            self.isOk = False
            print e
            print "the previous live preview may not close, only one live be allowed. if not, use killall -9 vim to kill the previous vim process"

    def run(self):
        self.startServer()

    def startServer(self):
        header = "HTTP/1.1 200 OK\r\nContext-Type: text/html\r\nAccess-Control-Allow-Origin: *\r\nServer: Python-slp version 1.0\r\nContext-Length: "
        self.isRun = True
        while self.isRun:
            try:
                confd,addr = self.lisfd.accept()
            except socket.error as e:
                print e
                self.isRun = False

            if self.isRun == False:
                break;

            content = markdown_preview.getBuff()
            confd.send(self.Response(header, content))
            confd.close()

    def endServer(self):
        self.isRun = False
        try:
            try:
                time.sleep(1)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.HOST, self.PORT))
                sock.send('1')
            except Exception as e:
                print e
            self.lisfd.close()
        except Exception as e:
            print e
            print "Markdown Server is Down"
