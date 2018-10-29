from multiprocessing.connection import Client
from array import array

address = ('localhost', 6000)

with Client(address, authkey=b'go beyond Plus ULTRA!') as conn:
    print(conn.recv())                  # => [2.25, None, 'junk', float]

    print(conn.recv_bytes())            # => 'hello'

    arr = array('i', [0, 0, 0, 0, 0])
    print(conn.recv_bytes_into(arr))    # => 8
    print(arr)                          # => array('i', [42, 1729, 0, 0, 0])

    email = conn.recv_bytes()
    emailChk = ['utkeitaro_gmail.com', 'db_gmail.com', 'minecraft_gmail.com']
    flag = False
    email = email.decode("utf-8")
    for emails in emailChk:
        if emails == email:
            flag = True
            print(str(emails) + ' == ' + email )
            print("Found email, preparing process.")
            break
    print("Email == " + str(email))
    if flag:
        print("Running item.")

    else:

        print("email is non existant")
    conn.close()
