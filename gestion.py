import subprocess, sys


color_green,color_cyan,color_red,color_yellow,color_end='\033[32m','\033[36m','\033[31m','\033[33m','\033[0m'
var_help=['--help','-help','--manual','-manual']
setmode='BOARD'
port="None"
etat="None"
error="Pas d'erreurs détectées !"
finish=True


print("","-"*57,"\n|          "+color_green+"GPIO led controller | Raspberry pi 3 A+ "+color_end+"       |\n","-"*57)
print("|       "+color_cyan+"            version:    1.1            "+color_end+"           |\n|     "+color_cyan+"              author:     petitcroco            "+color_end+"    |\n","-"*57)

if ("-pinout" in sys.argv):
	print("*"*26, "pinout", "*"*25)
	print(subprocess.getoutput(""))
	exit()

for arg in var_help:
	if arg in sys.argv:
		print("|             "+color_red+"            Usage :            "+color_end+"             |")
		print("| $ python3 gestion.py [broche] [on/off]                  |")
		print(" "+"-"*(57))
		print("| -pinout: Details de sortie des broches GPIO disponibles |")
		print("| -setmode:BOARD se réferer par le numéro de la broche du |\n|                connecteur [par default]                 |")
		print("| -setmode:BCM se réferer par le numéro 'Broadcom SOC     |\n|              channel' soit les numéro associé au GPIO   |  \n","-"*57)
		exit()

if ("on" in sys.argv):
	etat='on'
if ("off" in sys.argv):
	etat='off'

for i in range(40):
	if str(i+1) in sys.argv:
		port=i+1

if ("-setmode:BOARD" in sys.argv):
	setmode='BOARD'
if ("-setmode:BCM" in sys.argv):
	setmode='BCM'

print("|          "+color_red+"               Execution               "+color_end+"        |\n "+color_yellow+"mode:",setmode,"\n port:",port,"\n état:",etat,""+color_end)

if port=="None":
	error="Le port n'est pas donné ou incorrect !"
	finish=False

if ((etat!="on") and (etat!="off")):
	error="variable [on/off] non déclarée ou incorrecte !"
	finish=False

if ((etat!="on") and (etat!="off")) and port=="None":
	error="Aucun arguments n'est donné !"
	finish=False

if finish==True:
	print("\n  \033[7;40;32mrendering : "+error+color_end+"\n","-"*57)
else:
	print("\n  \033[7;40;31mrendering : "+error+color_end+"\n","-"*57)

print(" "*6+"Try '--help' or '--manual' for more information\n")
