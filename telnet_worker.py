import socket
import select
from PyQt6.QtCore import QThread, pyqtSignal

class TelnetWorker(QThread):
    data_received = pyqtSignal(str)
    connection_closed = pyqtSignal()
    connection_error = pyqtSignal(str)
    
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.sock = None
        self.running = False

    def run(self):
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5.0)  # connection timeout
        
        try:
            self.sock.connect((self.host, self.port))
            self.data_received.emit(f"Connected to {self.host}:{self.port}\n")
        except Exception as e:
            self.connection_error.emit(f"Failed to connect: {str(e)}")
            self.running = False
            return
            
        self.sock.settimeout(0.5) # small timeout for select loop
        
        while self.running:
            try:
                # Use select to wait for data without blocking indefinitely
                ready_to_read, _, _ = select.select([self.sock], [], [], 0.5)
                if ready_to_read:
                    data = self.sock.recv(4096)
                    if not data:
                        # connection closed by server
                        break
                    
                    # Try to decode, handle errors
                    try:
                        decoded_data = data.decode('utf-8', errors='replace')
                        self.data_received.emit(decoded_data)
                    except Exception as e:
                        print(f"Decode error: {e}")
                        
            except socket.timeout:
                continue
            except Exception as e:
                if self.running:
                    self.connection_error.emit(f"Connection error: {str(e)}")
                break
                
        self.cleanup()
        
    def send_command(self, cmd):
        if self.sock and self.running:
            try:
                self.sock.sendall((cmd + '\r\n').encode('utf-8'))
            except Exception as e:
                self.connection_error.emit(f"Send error: {str(e)}")
                self.cleanup()
                
    def cleanup(self):
        self.running = False
        if self.sock:
            try:
                self.sock.close()
            except:
                pass
            self.sock = None
        self.connection_closed.emit()

    def stop(self):
        self.running = False
        self.wait()
