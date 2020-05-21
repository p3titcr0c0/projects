#coding:utf-8
import socket

##############################################
#           #                   #            #
#            #                 #             #
############### By petitcroco ################
#            #                 #             #
#           #                   #            #
##############################################

host, port = ('localhost', 1111)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    print("\nYou are connected !\n\nip: ",host,"\nport: ",port,"\n\n/!\ You just arrived /!\ \n")
    data = input("Send the data: ")
    data = data.encode("utf8")
    socket.sendall(data)

except:
    print("Err: connection impossible")
finally:
    socket.close()