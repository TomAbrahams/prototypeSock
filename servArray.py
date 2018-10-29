import socket, json, _thread

def sendingArray(myServerAddress, myArray, myEmail):

    socko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socko.connect(serverAddress)
    data = '{"email" :'+ str(myEmail) + '"results" :' + str(myArray) + '}'
    print("Sending", data)
    socko.send(data.encode())
    #Then I should have sent the info to the serverself.
    socko.close()

def getingArray(connection, address):
    print("Connected by ", address)
    print("Beginning Data Retrieval....")
    #Gets the data
    msgSize = connection.recv(20)
    msgSize = int(msgSize)
    data = connection.recv(msgSize)

    connection.close()
    data = data.decode('utf-8')
    print("Data Printing...")
    print(data)
    print("Data Finished...")
    data = json.loads(data)
    myEmail = data.get("email")
    myArray = data.get("results")
    print("Email", myEmail)
    print("Results",myArray)


if __name__ == '__main__':
    IP = 'localhost'
    PORT = 5019
    serverAddress = (IP, PORT)
    A = [1,2,3,2,1]
    email = "mr@socko.com"
    #Server needs to set up the connections.
    serverSocko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocko.bind(serverAddress)
    serverSocko.listen(2)
    while(True):
        conn, addr = serverSocko.accept()
        currentThread = _thread.start_new_thread(getingArray, (conn, addr))
