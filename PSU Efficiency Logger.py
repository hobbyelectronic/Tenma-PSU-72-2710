#Efficiency logger for switchmode power supplies using Kunkin KP184 and Tenma 72-2710
#Needs TenmaPSU72-2710 and  KP184 command line interface in the same directory
#!/usr/bin/python3
import click
import serial
import time
import os
import re
import subprocess
from array import *
from tabulate import tabulate
import csv 

#SET COM PORTS for Electronic Load and PSU
EL="com5"
PSU="COM4"
Start = 100
End=1000 #End of current range in mA
Step=100 #Step size in mA
PSUstart=30
PSUstop=32
count=0 
filename='LM2576v2.csv'

Results = []
Resultstable = []
ResultsPSU =[]

for y in range(PSUstart, PSUstop):
	
	cmd = "python TenmaPSU72-2710.py setvolt " + str(PSU) +" " + str(y)
	os.system(cmd) 
	time.sleep(5)
	for x in range(Start, End, Step):
		count=count +1
		cmd = "kp184 port " + str(EL) +";baud 9600;address 1;current " + str(x)
		os.system(cmd)
		time.sleep(1)
	
		cmd = "kp184 port " +str(EL)+ ";baud 9600;address 1;get_current"
		result = subprocess.check_output(cmd, shell=True)
		result = str(result)
		IOUT = re.findall('[0-9]+', result)
		IOUT = int(IOUT[4])
		#print(IOUT)
		time.sleep(1)
	
	
		cmd = "kp184 port " +str(EL)+ ";baud 9600;address 1;get_voltage"
		result = subprocess.check_output(cmd, shell=True)
		result = str(result)
		VOUT = re.findall('[0-9]+', result)
		VOUT = int(VOUT[4])
		#print(VOUT)
		
		cmd = "python TenmaPSU72-2710.py getcurrent " + str(PSU)
		result = subprocess.check_output(cmd, shell=True)
		result = str(result)
		IIN=re.findall('[0-9]+', result)
		#print(IIN)
		#print(IIN[2])
		cmd = "python TenmaPSU72-2710.py getvoltage " + str(PSU)
		result = subprocess.check_output(cmd, shell=True)
		result = str(result)
		VIN=re.findall('[0-9]+', result)
		VINR= VIN[1]+VIN[2]
		VINR= (float(VINR)*10)/1000
		IINR=float(IIN[1]) + (float(IIN[2])/1000)
		VOUTR= float(VOUT)/1000
		IOUTR= float(IOUT)/1000
		#print(VINR)
		Efficiency = (IOUTR*VOUTR)/(VINR*IINR)
		EFFR= float("{:.3f}".format(Efficiency))
		#print(EFFR)
		Results.append(VINR)
		Results.append(IINR)
		Results.append(VOUTR)
		Results.append(IOUTR)
		Results.append(EFFR)
		Resultstable.append([VINR,IINR,VOUTR,IOUTR,EFFR])
		time.sleep(10)
		print(".")

print(tabulate(Resultstable,headers=["VIN","IIN", "VOUT","IOUT","EFF"]))
file = open(filename, 'w', newline ='') 	
with file: 
	# identifying header 
	header = ['VIN(V)', 'IIN(A)','VOUT(V)',"IIOUT(A)", 'EFFICIENCY'] 
	writer = csv.DictWriter(file, fieldnames = header) 
	
	# writing data row-wise into the csv file 
	writer.writeheader()
	loopcount = 0
	for x in range (0,count):
		writer.writerow({'VIN(V)' : Results[loopcount], 
						'IIN(A)': Results[loopcount+1],
						'VOUT(V)': Results[loopcount+2],
						'IIOUT(A)': Results[loopcount+3],
						'EFFICIENCY': Results[loopcount+4]}) 
		loopcount=loopcount+5
