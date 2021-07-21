# Server client
Server and client for transfer files via sockets.
## Server
The command to launch the server is:
```
python3 Server
```
Once it's launched it shows the server IP on terminal and store all files received into Server_log folder. To stop it 
press Ctrl-C.
## Client
The command to launch the client is:
``` 
python3 Client [server_IP] [file_name]
```
Where "server_IP" is the IP of the server and "file_name" is the absolute path name of the file.
