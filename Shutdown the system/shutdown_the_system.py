import os 
import platform
  
   
def shutdown():

    Ask = input("Would you like to shutdown your computer ? (yes / no):   ") 
  
    if Ask == 'no': 
        print("Okay chill :)")
        exit() 
    else: 
        if platform.system()=="Windows":
            os.system("shutdown -s -t 0")
     
        else:
            os.system("shutdown -h now")

shutdown()
