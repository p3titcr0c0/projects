#coding:utf-8
import socket

##############################################
#           #                   #            #
#            #                 #             #
############### By petitcroco ################
#            #                 #             #
#           #                   #            #
##############################################

host, port = ('', 1111)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("\nServer started !\n\nip:",host,"\nport: " + str(port)+"\n")

socket.listen(5)
connection, address = socket.accept()
print("/!\ Anyone is here /!\ \n")

data = connection.recv(1024)
print("data: "+data.decode("utf8"))

connection.close()
socket.close()