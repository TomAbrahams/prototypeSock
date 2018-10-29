from multiprocessing.connection import Client
from array import array

address = ('localhost', 6001)     # family is deduced to be 'AF_INET'
choice = 'y'

with Client(address, authkey=b'go beyond Plus ULTRA!') as conn:
    while choice != 'n':
        choice = input("Would you like to send a message? (y/n)")
        if choice == 'y':
            messageToSend = input('Type what you want to send.\n')
            messageToSend = messageToSend.encode('utf-8')
            conn.send_bytes(messageToSend)
        elif choice == 'n':
            print('Thank you for using the multiprocessing client tester')
            print('Informing server that you wish to end your connection.')
            messageToSend = b'TM86'
            conn.send_bytes(messageToSend)
            conn.close()
        else:
            print('Invalid choice.')
print("the dream is program over...")
