import socketserver
import subprocess
from sys import platform


class MyTCPHandler(socketserver.StreamRequestHandler):
    '''
    The request handler class for our server.

    It is instantiated once per connection to the server, and must override the handle() method to implement
    communication to the client.
    '''
    def handle(self):
        data = self.request.recv(1048576).strip().decode('utf-8')
        print("{} wrote:".format(self.client_address[0]))
        data_lines = data.split('\n')
        with open("Server/Server_log/" + data_lines[0],"w+") as f:
            for line in data_lines[1:]:
                f.write(line + '\n')

        self.wfile.write(b'Data received')


def get_ip():
    if platform == "win32":
        output = str(subprocess.check_output(['ipconfig']))
        start = output.find('IPv4')
        ip = output[start:].split('\\n')[0][34:-2]
        return ip
    elif platform == "linux":
        output = subprocess.check_output(['hostname','-I']).decode('utf-8')
        return output[:-1]  # omit \n


if __name__ == "__main__":
    HOST = get_ip()
    PORT = 9999
    print("My ip is: ",HOST)
    # Create the server, binding to localhost on port 9999
    try:
        with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server forever until you press Ctrl-C
            server.serve_forever()
    except KeyboardInterrupt:
        print('\nRequest to close the server received.')