# This is a simple email client that sends email to a recipient.
# The client connects to a mail server, then dialogues (handshakes) with the mail server
# using the SMTP protocol and send an email message to the mail server.


from socket import *


# In order to terminate the program


# Defining the smtp client
def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n I can do it!"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # external_mailserver = 'smtp.gmail.com'

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Handshaking between the SMTP client and the server begins

    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    helo_command = 'HELO Alice\r\n'
    clientSocket.send(helo_command.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    sender_email = "MAIL FROM: <sender@senderdomain.com>\r\n"
    clientSocket.send(sender_email.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    # if recv2[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    recvr_email = "RCPT TO: <recvr@recvrdomain.com>\r\n"
    clientSocket.send(recvr_email.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    # if recv3[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    clientSocket.send("DATA\r\n".encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    # if recv4[:3] != '354':
    #    print('354 From and To information not received.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg)
    recv5 = clientSocket.recv(1024).decode()
    # print(recv5)
    # if recv5 != '250':
    # print('250 reply not received from the server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    recv6 = clientSocket.recv(1024).decode()
    # Fill in end

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
