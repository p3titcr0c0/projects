import subprocess, sys, time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

color_green,color_cyan,color_red,color_yellow,color_end='\033[32m','\033[36m','\033[31m','\033[33m','\033[0m'
ports_raspberry_pi_3p=[[2,4],[1,17],[6,9,14,20,25,30,34,39]]
#_______________________5v_____3v___________ground__________

var_help=['--help','-help','help','--manual','-manual']
port="None"
etat="None"

status=["Pas d'erreurs détectées !",True]

var_for=[False,0]


print("","-"*57,"\n|          "+color_green+"GPIO hub controller | Raspberry pi 3 A+ "+color_end+"       |\n","-"*57)
print("|       "+color_cyan+"            version:    1.6            "+color_end+"           |\n|     "+color_cyan+"              author:     petitcroco            "+color_end+"    |\n","-"*57)

if ("-pinout" in sys.argv):
	print("*"*26, "pinout", "*"*25)
	print(subprocess.call(['pinout', '--color']))
	exit()

for arg in var_help:
	if arg in sys.argv:
		print("|             "+color_red+"            Usage :            "+color_end+"             |")
		print("| $ python3 gestion.py [broche] [on/off]                  |")
		print(" "+"-"*(57))
		print("| -pinout: Details de sortie des broches GPIO disponibles |")
		print("| -setmode:BOARD se réferer par le numéro de la broche du |\n|                connecteur [par default]                 |")
		print("| -setmode:BCM se réferer par le numéro 'Broadcom SOC     |\n|              channel' soit les numéro associé au GPIO   |\n")
		print("| -for [seconds]  met dans l'état [on/off] choisi pendant|\n|                 le délai et reviens à l'état initial    |\n","-"*57)
		exit()

if ("on" in sys.argv):
	etat='on'
if ("off" in sys.argv):
	etat='off'

for i in range(40):
	try:
		if (str(i+1)==sys.argv[0]) or (str(i+1)==sys.argv[1]) or (str(i+1)==sys.argv[2]):
			port=i+1
			if (port in ports_raspberry_pi_3p[0]):
			   	status[0]="Le port choisi est une alimentation 5v !"
			   	status[1]=False
			if (port in ports_raspberry_pi_3p[1]):
				status[0]="Le port choisi est une alimentation 3.3v !"
				status[1]=False
			if (port in ports_raspberry_pi_3p[2]):
				status[0]="Le port choisis est la masse !(use -pinout)"
				status[1]=False
	except:
		port="None"

if ("-setmode:BCM" in sys.argv):
	GPIO.setmode(GPIO.BCM)
else:
	GPIO.setmode(GPIO.BOARD)

for i in range (len(sys.argv)):
	if (sys.argv[i]=='-for'):
		var_for[0]=i

try:
	if var_for[0]>=1:
		var_for[1]=sys.argv[var_for[0]+1]
except:
	status[0]="'-for' est utilisé sans attribut !"
	status[1]=False

print("|          "+color_red+"               Execution               "+color_end+"        |"+color_yellow)
if GPIO.getmode()==10:
	print(" mode: BOARD -> 10")
elif GPIO.getmode()==11:
	print(" mode : BCM -> 11")
print(" port:",port,"\n état:",etat,"")

if var_for[0]!=False:
	print(" mode -for activé:")
	print("   pendant",var_for[1],"seconde(s)"+color_end)

if port=="None":
	status[0]="Le port n'est pas donné ou incorrect !"
	status[1]=False

if ((etat!="on") and (etat!="off")):
	status[0]="variable [on/off] non déclarée ou incorrecte !"
	status[1]=False

if ((etat!="on") and (etat!="off")) and port=="None":
	status[0]="Aucun arguments n'est donné !"
	status[1]=False

if status[1]==True:
	print("\n  \033[7;40;32mrendering : "+status[0]+color_end+"\n","-"*57)
	GPIO.setup(port, GPIO.OUT)
	if ("-for" in sys.argv):
		var_for[0]=GPIO.input(port)
		if (var_for[0]==0):
			if etat=="on":
				GPIO.output(port, 1)
		else:
			if etat=="off":
				GPIO.output(port,0)
		time.sleep(int(var_for[1]))
		GPIO.output(port, var_for[0])
	else:
		if etat=="on":
			GPIO.output(port, 1)
		if etat=="off":
			GPIO.output(port,0)

else:
	print("\n  \033[7;40;31mrendering : "+status[0]+color_end+"\n","-"*57)

print(" "*6+"Try '--help' or '--manual' for more information\n\n\n\n")
