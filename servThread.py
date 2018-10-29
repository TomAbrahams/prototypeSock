import _thread
import socket
from array import array



def setupConnection(address, debugFlag):
    #Gets the size of the item with 20 length
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = address
    sock.bind(server_address)
    sock.listen(2)
    conn, client_address = sock.accept()
    flag = True
    while(flag):
        sizeOfData = conn.recv(20)
        sizeOfData = sizeOfData.decode('utf-8')
        print(sizeOfData)
        sizeOfData = int(sizeOfData)
        if(debugFlag):
            print(sizeOfData)

        #Now we know the size of the item
        #Get the Info
        if(sizeOfData > 0):

            print("Entering loop")
            data = conn.recv(sizeOfData)
            #I now I have the data.
            data = data.decode('utf-8')
            if data == 'TM86':
                flag = False
            print(data)
        else:
            flag = False

    print("Closing the connection...")
    conn.close()









if __name__ == '__main__':
    address = ('localhost', 6001)   #Auto determines AF_INET
    choice = 'y'
    numOfThreads = 0
    setupConnection(address, True)
