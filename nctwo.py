#!bin/python
import sys
import os
import time

def bersih():
	os.system("clear")
	
def menu():
	bersih()
	print ("\033[0;32m[\033[0;31m+\033[0;32m]=================\033[0;37m●●●●●\033[0;32m============[\033[0;31m+\033[0;32m]")
	print ("Author : mister cobain.jr")
	print ("Wa : 082353878714")
	print ("Github : https://github.com/pranatarizka")
	print ("Word : be satisfied in the world")
	print ("[\033[0;31m+\033[0;32m]==============================[\033[0;31m+\033[0;32m]")
	print ("\033[0;37m [1] Install Technology Ai")
	print (" [2] Install Pemutus Wifi")
	print (" [3] Keluar/exit")
	print ("______________")

	pil = int(input("\033[0;32mPilih sesuai nomor : "))
	if pil ==1:
		os.system("apt upgrade && apt update -y")
		os.system("apt install git -y")
		os.system("apt install python -y")
		os.system("git clone https://github.com/Mistehcobain/rboowhan")
		print ("[Masukan perintah cd rboowhan,ls,python rboo1.py] -")
		os.system("cd rboowhan")
		os.system("ls")
		os.system("python rboo1.py")
	
	elif pil ==2:
		os.system("apt upgrade && apt update -y")
		os.system("apt install git -y")
		os.system("apt install python -y")
		os.system("git clone https://github.com/Mistehcobain/Leader4")
		print ("[Masukan perintah cd Leader4,ls,python Leader4.py] -")
		os.system("cd Leader4")
		os.system("ls")
		os.system("python Leader4.py")
	
	elif pil ==3:
		os.system("exit")
		os.system("logout")	

	else:
		os.system("clear")
		enter = (input("opsi tidak ada silahkan pilih kembali[Enter];"))
		os.system("python nctwo.py")
		
menu()
