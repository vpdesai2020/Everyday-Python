import os 
  
shutdown = input("Would you like to shutdown your computer ? (yes / no): ") 
  
if shutdown == 'no': 
    print("Okay :)")
    exit() 
else: 
    os.system("shutdown /s /t 1")