import socket
import sys

if __name__ == "__main__":
    HOST, PORT = sys.argv[1], 9999

    # Create a socket (SOCK_STREAM means a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        with open(sys.argv[2], 'r') as f:
            data = f.read()
            name_pos = sys.argv[2].rfind('/') + 1  # omit '/'
            final_data = sys.argv[2][name_pos:] + '\n' + data
            sock.sendall(bytes(final_data, "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))