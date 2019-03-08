import threading
import socket
from http.server import HTTPServer, CGIHTTPRequestHandler, BaseHTTPRequestHandler
import socketserver
import threading

#реализация многопоточного сервера CGI на порт 9090

class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):

    pass

web_server = ThreadingHTTPServer(('',9090),CGIHTTPRequestHandler)
thre1=threading.Thread(target = web_server.serve_forever)
thre1.start()