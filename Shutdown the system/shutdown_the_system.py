import os 
import platform
  
Ask = input("Would you like to shutdown your computer ? (yes / no): ") 
  
if Ask == 'no': 
    print("Okay :)")
    exit() 
else: 
    shutdown()
    
    
def shutdown():
    import os
    import platform
 
    if platform.system()=="Windows":
        os.system("shutdown -s -t 0")
 
    else:
        os.system("shutdown -h now")
