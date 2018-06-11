#!/usr/bin/python                                                                                                                              


# By Keith.K @ 2018                                                                                                                               



import os                                                                                                                                      
import sys                                                                                                                                     
import time                                                                                                                                    
import datetime                                                                                                                                
import json                                                                                                                                    
import commands                                                                                                                                

from urllib import urlopen                                                                                                                     



gRigName = "-"                                                                                                                                 
gJsonSite = "-"                                                                                                                                
gDebugMode = 0                                                                                                                                 
gGpuNotHashing = 0                                                                                                                             
gLogFile = "/home/ethos/gpu_crash.log"                                                                                                         
hostname = "8.8.8.8"                                                                                                                           



# ================================   functions  =============================                                                                  
def DumpActivity(dumpStr):                                                                                                                     
  print dumpStr                                                                                                                                

  try:                                                                                                                                         
    # writes input string in a file                                                                                                            
    pLogFile = open(gLogFile, "a")                                                                                                             
    pLogFile.write("%s @ %s\n" % (dumpStr, str(datetime.datetime.now())))                                                                      
    pLogFile.close()                                                                                                                           
  except:                                                                                                                                      
    print "File write error in - " + gLogFile                                                                                                  



# ============================== get rig info ============================                                                                
                                                                                                                 
def GetRigInfo():                                                                                                                            
  global miner_Hashes, crashed_Status                                                                                                                   

  miner_Hashes = commands.getoutput("update | grep 'miner_hash' ")   
  crashed_Status = miner_Hashes.find("00.00")

# ===================================   run  ================================                                                                  
                                                                                                                                                                                                      
DumpActivity("Monitor Started!")

while 1:                                                                                                                                       
  # wait for 5 min                                                                                                                             
  time.sleep(300)         
  
  # check for connection  
  response = os.system("ping -c 1 " + hostname)                                                                                              
  if (response == 0):                                                                                                                          
       print ("Ping 8.8.8.8 successfully ! Network Active")                                                                              
  else:                                                                                                                                        
       DumpActivity("Ping 8.8.8.8 unsuccessfully ! Network Error ! Rebooting...")
       print ("Network Error ! Rebooting...")
       os.system("sudo reboot")   
                                                                                                                           
  # check if any gpu is down
  GetRigInfo()
  
  if (crashed_Status != -1):                                                                                                    
      # reboot                                                                                                                                 
      DumpActivity("One or more GPU(s) might have crashed")
      DumpActivity(miner_Hashes)
      DumpActivity("Rebooting...")
      os.system("sudo reboot")                                                                                                            
  else:                                                                                                                                        
    # reset reboot pending counter                                                                                                             
    print ("All GPU(s) is mining ! ")                                                                          
                                                                                                                           

