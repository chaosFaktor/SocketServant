import socket

class Connection:
    def __init__(self, con, addr, server):
        self.con = con
        self.addr = addr
        self.server = server
    def read(self, buffer_size):
        return self.con.recv(buffer_size)
    def write(self, msg):
        self.con.sendall(msg)
    def print(self, msg, end='\n'):
        self.con.sendall(msg.encode('utf-8')+end.encode('utf-8'))
    def get_addr(self):
        return self.addr
    
    

class SocketServer:
    def __init__(self, port, listen_addr='0.0.0.0', queue=0):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = listen_addr
        self.port = port
        self.socket.bind((self.host, self.port))
        
        self.queue = queue
    
    def bind_callback(self, on_open=False, on_close=False):
        self.open_callback = on_open
        self.close_callback= on_close
    
    def wait_for_connection(self):
        with self.socket as sock:
            sock.listen(self.queue)
            con, addr = sock.accept()
            con_obj = Connection(con, addr, self)
            if (self.open_callback):
                self.open_callback(con_obj)
            if (self.close_callback):
                self.close_callback(con=con_obj)
    def wait_for_connections(self):
        with self.socket as sock:
            sock.listen(self.queue)
            while True:
                con, addr = sock.accept()
                con_obj = Connection(con, addr, self)
                if (self.open_callback):
                    self.open_callback(con_obj)
                if (self.close_callback):
                    self.close_callback(con=con_obj)