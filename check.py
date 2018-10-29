messageSent = "ThisOnTWO?"
sizeOfMessage = len(messageSent)
sizeOfMessage  = str(sizeOfMessage)
for i in range(20):
    if(len(sizeOfMessage) < 20):
        sizeOfMessage = '0' + sizeOfMessage
    else:
        print("Done with item of size 20. Time to send")
        break
print(sizeOfMessage)
print(len(sizeOfMessage))
