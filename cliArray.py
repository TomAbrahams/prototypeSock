import socket, json

def sendingArray(myArray, myEmail):
    IP = 'localhost'
    PORT = 5019
    socko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddress = (IP, PORT)
    socko.connect(serverAddress)
    data = json.dumps({"email" : myEmail, "results" : myArray})
    print("Preparing to send data", data)
    print(len(data))
    #Set up the size of the data.
    sizeOfData = len(data)
    sizeOfData = str(sizeOfData)
    for i in range(20):
        sizeOfData = '0' + sizeOfData
        if len(sizeOfData) == 20:
            break
    #Sending size of 20
    socko.sendall(sizeOfData.encode('utf-8'))
    print("Send json...")
    socko.sendall(data.encode('utf-8'))
    #Then I should have sent the info to the serverself.
    socko.close()

if __name__ == '__main__':
    A = [1,2,3,2,590000]
    email = "cookies123@fake.com"
    sendingArray(A, email)
