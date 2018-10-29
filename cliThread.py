from multiprocessing.connection import Client
import socket
from array import array

def sendEveryString(messageSent, sock):
    sizeOfMessage = len(messageSent)
    sizeOfMessage = str(sizeOfMessage)
    print(sizeOfMessage)

    for i in range(20):
        if(len(sizeOfMessage) < 20):
            sizeOfMessage = '0' + sizeOfMessage
        else:
            print("Done with item of size 20. Time to send")
            break
    sizeOfMessage = sizeOfMessage.encode('utf-8')
    sock.sendall(sizeOfMessage)
    print(sizeOfMessage)
    messageSent = messageSent.encode('utf-8')
    #Socket send the information.
    sock.sendall(messageSent)

if __name__ == '__main__':
    address = ('localhost', 6001)     # family is deduced to be 'AF_INET'
    choice = 'y'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    while choice != 'n':
        choice = input("Would you like to send a message? (y/n)")
        if choice == 'y':
            messageToSend = input('Type what you want to send.\n')
            sendEveryString(messageToSend, sock)

        elif choice == 'n':
            print('Thank you for using the multiprocessing client tester')
            print('Informing server that you wish to end your connection.')
            messageToSend = 'TM86'
            sendEveryString(messageToSend, sock)
            sock.close()
        else:
            print('Invalid choice.')
    print("the dream is program over...")
