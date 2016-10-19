import socket
import struct
import binascii

pageSize = 128


def getByte(value):
        return chr(value)

def readByte(byte):
        return struct.read(1)

def getInt32(value):
        return struct.pack('I', value)

def readIntArray(address, size):
        array = []
        cycles = size/pageSize + 1

        host = 'localhost'
        port =  5556
        test_socket = socket.socket()
        test_socket.connect((host,port))

        for i in range(cycles):
                lsize = size - (i*pageSize)
                if lsize > pageSize:
                        lsize = pageSize

                """ Python2 equivalents of readBytes, readBool etc..
                can be found here stackoverflow.com/questions/442188/readint-readbyte-readstring-etc-in-python"""
                test_socket.send(getByte(1))
                test_socket.send(getInt32(socket.htonl(address + i * pageSize * 4)))
                test_socket.send(getByte(lsize))

                r = test_socket.recv(1)
                print 'r ='+ binascii.hexlify(r)

                d = test_socket.recv(lsize*4)
                print 'd =' + binascii.hexlify(d)

readIntArray(0x68000200, 1)
