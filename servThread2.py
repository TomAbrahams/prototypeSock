import _thread
from multiprocessing.pool import ThreadPool
from multiprocessing.connection import Listener
from array import array



def setupConnection(address, debugFlag):
    #Gets the size of the item with 20 length
    print("Always Be coding")
    choice = 'y'
    while choice == 'y':
        with Listener(address, authkey=b'go beyond Plus ULTRA!') as listener:
            with listener.accept() as conn:
                print('connection accepted from', listener.last_accepted)
                while True:
                    try:
                        print("Attempting the thread.")
                        message = conn.recv_bytes()
                        email = message.decode("utf-8")
                        #print(email)
                        emailChk = ['utkeitaro_gmail.com', 'db_gmail.com', 'minecraft_gmail.com']
                        flag = False
                        for emails in emailChk:
                            if emails == email:
                                flag = True
                                print(str(emails) + ' == ' + email )
                                print("Found email, preparing process.")
                                break
                        #print("Email == " + str(email))
                        if flag:
                            print("Running item.")
                        elif(email == 'TM86'):
                            print('closing the connection.')
                            conn.close()
                            choice = 'n'
                            #return choice
                        else:
                            print(email)
                            print("email is non existant")
                    except KeyboardInterrupt:
                        conn.close()
                        print("Terminating server...")
                        choice == 'n'
                        #return choice
                        break

if __name__ == '__main__':
    address = ('localhost', 6001)   #Auto determines AF_INET
    choice = 'y'
    numOfThreads = 0

    while choice == 'y':
        print("This begins")
        pool = ThreadPool(processes = 2)
        asyncResult = pool.apply_async(setupConnection, (address, True))
        choice = asyncResult
        print("This ends ", choice)
