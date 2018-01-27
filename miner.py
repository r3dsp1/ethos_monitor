#!/usr/bin/python                                                                                                                              


# -*- Python -*-                                                                                                                               
#                                                                   
#                                                                                                                                              
#                                                                                                                                              
# Warning:                                                                                                                                    
# Use all material in this file at your own risk.                                                                                
#                                                                                                                                              



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



# ============================== process arguments ============================                                                                
def ProcessArguments(gotPanelInfo):                                                                                                            
  # arg#0: rig name (required if "/var/run/ethos/stats.file" not available)                                                                    
  # arg#1: json site (required if "/var/run/ethos/url.file" not available)                                                                     
  # "-debug" : (optional) set debug mode                                                                                                       
  global gRigName, gJsonSite, gDebugMode                                                                                                       

  if (gotPanelInfo != 1):                                                                                                                      
    DumpActivity("Taking rig name and panel url from arguments")                                                                               

  argStr = ""                                                                                                                                  

  argIdx = 0                                                                                                                                   
  argProcessed = 0                                                                                                                             
  while (1):                                                                                                                                   
    argIdx += 1                                                                                                                                
    if (argIdx >= len(sys.argv)):                                                                                                              
      break                                                                                                                                    

    arg = sys.argv[argIdx]                                                                                                                                                                                                                                                   

    if (gotPanelInfo == 1):                                                                                                                    
      DumpActivity("Arguments : " + str(arg))                                                                                                  
      continue                                                                                                                                 

    argProcessed += 1                                                                                                                          
    if (argProcessed == 1):                                                                                                                    
      gRigName = arg                                                                                                                           
    elif(argProcessed == 2):                                                                                                                   
      gJsonSite = arg                                                                                                                          
                                                                                                                                               

def GetPanelInfo():                                                                                                                            
  global gRigName, gJsonSite                                                                                                                   

  commandOutput = commands.getstatusoutput('\grep http /var/run/ethos/url.file')                                                               
  if (commandOutput[0] != 0):                                                                                                                  
    DumpActivity("/var/run/ethos/url.file is not availble")                                                                                    
    return 0                                                                                                                                   

  gJsonSite = commandOutput[1]                                                                                                                 
  gJsonSite = gJsonSite+"/?json=yes"                                                                                                           

  commandOutput = commands.getstatusoutput("\grep hostname /var/run/ethos/stats.file")                                                         
  if (commandOutput[0] != 0):                                                                                                                  
    DumpActivity("/var/run/ethos/stats.file is not avaible")                                                                                   
    return 0                                                                                                                                   

  gRigName = commandOutput[1][9:]                                                                                                              

  return 1                                                                                                                                     



# ===================================   run  ================================                                                                  
success = GetPanelInfo()                                                                                                                       
ProcessArguments(success)                                                                                                                      
DumpActivity("Rig Name: " + gRigName + ", Json: " + gJsonSite)                                                                                 
DumpActivity("Monitor Started!")                                                                                                               

while 1:                                                                                                                                       
  # wait for 5 min                                                                                                                             
  time.sleep(300)         
  
  # check for connection  
  response = os.system("ping -c 1 " + hostname)                                                                                              
  if (response == 0):                                                                                                                          
       DumpActivity("Ping 8.8.8.8 successfully ! Network Active")                                                                              
  else:                                                                                                                                        
       DumpActivity("Ping 8.8.8.8 unsuccessfully ! Network Error")                                                                             
       DumpActivity("Rebooting ")                                                                                                              
       os.system("sudo hard-reboot")   

  # read site content                                                                                                                          
  try:                                                                                                                                         
    url = urlopen(gJsonSite).read()                                                                                                            
  except:                                                                                                                                      
    DumpActivity("invalid url")                                                                                                                
                                                                                                                                   

  # convert site content to json                                                                                                               
  try:                                                                                                                                         
    result = json.loads(url)                                                                                                                   
  except:                                                                                                                                      
    DumpActivity("invalid json")                                                                                                               
                                                                                                                                  

  # extract data                                                                                                                               
  try:                                                                                                                                         
    numGpus = result["rigs"][gRigName]["gpus"]                                                                                                 
    numRunningGpus = result["rigs"][gRigName]["miner_instance"]                                                                                
    hashRate =  result["rigs"][gRigName]["miner_hashes"]                                                                                       
    status = result["rigs"][gRigName]["condition"]                                                                                             
  except:                                                                                                                                      
    DumpActivity("invalid rig name")                                                                                                           
                                                                                                                                                              

  if (status == "unreachable"):                                                                                                                
    DumpActivity("[Warning] panel is unreachable")                                                                                            
                                                                                                                                 
  # check if any gpu is down                                                                                                                   
  if (int(numRunningGpus) != int(numGpus)):                                                                                                    
      # reboot                                                                                                                                 
      DumpActivity("One or more GPU(s) might have crashed")                                                                                    
      DumpActivity("Rebooting ")                                                                                                               
      os.system("sudo hard-reboot")                                                                                                            
  else:                                                                                                                                        
    # reset reboot pending counter                                                                                                             
    DumpActivity("GPU(s) is working fine! " + str(hashRate) + " H/s")                                                                          
    gGpuNotHashing = 0                                                                                                                         

