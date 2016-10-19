import socket
import struct
import binascii

pageSize = 128


def getByte(value):
                return chr(value)

def readByte():
        return struct.read(1)

def getInt32(value):
        return struct.pack('I', value)

def writeIntArray(address, array, size):
        cycles = (size/pageSize) + 1
        
        host = 'localhost'
        port =  5556
        test_socket = socket.socket()
        test_socket.connect((host,port))

        for i in range(cycles):
                lsize = size - (i*pageSize)
                if lsize > pageSize:
                        lsize = pageSize

                test_socket.send(getByte(2))
                test_socket.send(getInt32(socket.htonl(address + i * pageSize * 4)))
                test_socket.send(getByte(lsize))

                for k in range(lsize):
                        test_socket.send(getInt32(socket.htonl(array[i*pageSize + k])))
                        
                r = test_socket.recv(1)
                print 'r ='+ binascii.hexlify(r)

writeIntArray(0x6201C000,[0x00FF0000,0x000000FF,0x0000FF00], 1)

