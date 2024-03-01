from .services.SocketServer import SocketServer
import config

from threading import Thread



#######     GLOBALS     ######
server = SocketServer(config.server_cfg["port"])


#######     CALLBACKS   ######
def on_open(con):
    con.print("200")
    while True:
        print(con.read(1024))
        con.print("200")

def on_close(con):
    print("Connection terminated.")
    

def run():
    server.bind_callback(on_open=on_open, on_close=on_close)
    server.wait_for_connections()