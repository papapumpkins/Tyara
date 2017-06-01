''' RFCOMM Mode Bluetooth BT_SOCKETet '''


import bluetooth

BT_ADDR = "7C:B0:C2:8C:5C:02"

port = 0

BT_SOCKET=bluetooth.BluetoothBT_SOCKETet( bluetooth.RFCOMM )
BT_SOCKET.connect((BT_ADDR, port))

BT_SOCKET.send("hello!!")

BT_SOCKET.close()