"""
DOCSTRING
"""
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
