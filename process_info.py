import psutil

#Not executed and tested

#Iterate over all running process
for process in psutil.process_iter(['pid', 'name', 'username']):
  try:
    #print process information
    print(f"PID: {process.info['pid']}, Name: {process.info['name']}, Username: {process.info['username']}")
  except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    pass
    
