''' RFCOMM Mode Bluetooth Socket '''


import bluetooth

socket_server=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
socket_server.bind(("", port))
socket_server.listen(1)

(socket_client, address) = socket_server.accept()
print("Connection Request from ",address," - ACCEPTED")

data = socket_client.recv(1024)
print("Incoming :  [%s]" % data)

socket_client.close()
socket_server.close()