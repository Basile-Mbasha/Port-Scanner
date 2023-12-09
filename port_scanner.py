import socket
import threading
from queue import Queue
import pyfiglet
import time

# Create an ASCII art banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

def port_scan(port):
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(0.5)
 try:
     con = s.connect((target, port))
     print('Port :', port, "is open.")
     con.close()
 except:
     pass

def scan_thread():
 while True:
     worker = q.get()
     port_scan(worker)
     q.task_done()

target = input("Enter the host: ")
q = Queue()
for x in range(1, 100):
 q.put(x)

# Record the start time
start_time = time.time()

for t in range(200):
 t = threading.Thread(target=scan_thread)
 t.daemon = True
 t.start()

q.join()

# Record the end time
end_time = time.time()

# Calculate the duration of the scan
duration = end_time - start_time
print(f"Scan completed in {duration:.2f} seconds.")
