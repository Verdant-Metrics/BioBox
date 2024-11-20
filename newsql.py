
import minimalmodbus
import pandas as pd 
#import plotly
#import matplotlib.pyplot as plt
import datetime 
#import numpy as np
#import time
#from dash import Dash, dcc, Input, Output, callback, html
import requests
import json
import os
#from google.cloud.sql.connector import Connector, IPTypes
import pymysql
import time







# initilize soil sensor-----------------------------------------------------
PORT='COM3'

#register numbers based on rs458 protocol
N_reg= 30
P_reg=31
K_reg=32
PH_reg=6
humidity_reg=18
temp_reg=19
cond_reg=21

values=(N_reg,P_reg,K_reg,PH_reg,humidity_reg,temp_reg,cond_reg)

#Set up instrument
instrument = minimalmodbus.Instrument(PORT,1,mode=minimalmodbus.MODE_RTU)

instrument.serial.baudrate = 9600

#Make the settings explicit
instrument.serial.bytesize = 8
instrument.serial.parity   = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.close_port_after_each_call = True
instrument.clear_buffers_before_each_transaction = True

#--------------------------------------------------------------------






#master data frames
masterlist=[]
master_air=[]
Master=pd.DataFrame(masterlist, columns = ["N","P","K","PH","humidity","temp","cond","time"]) 
Master_Air=pd.DataFrame(master_air, columns = ['pm01','pm02','pm10','pm003Count','atmp','rhum','rco2','tvoc','timestamp']) 


def soilsensor(a):
	global Master

	templist=[]
	df = pd.DataFrame(templist, 
                  columns = ["N","P","K","PH","humidity","temp","cond","time"]) 
	

	print("got here")



	templist=[]
	#print("gothere2")
	print(df)

	for i in values:

		value = instrument.read_register(i)
		print(value)
		templist.append(value) #temporary list of all values
		print("templist",templist)

		
 
		# add time and append using loc methods
	time = datetime.datetime.now()
	templist.append(str(time))
	df.loc[len(df)] = templist
	
	
	#Master=pd.concat([Master,df])
	#print('master',Master)

def requestairgradient():
		global Master_Air

		response=requests.get("https://api.airgradient.com/public/api/v1/locations/81542/measures/current?token=2932e6e4-a882-43d9-833c-ec57b87e49a7")
		jsona=response.json()
		dfresponse=pd.json_normalize(jsona) #getting json api response as data frame

		dfresponse=dfresponse[['pm01','pm02','pm10','pm003Count','atmp','rhum','rco2','tvoc','timestamp']] #sub smapling columns of interest

		dfresponse=dfresponse.iloc[0,:] #convert to string so it can be appended to data fram

		Master_Air.loc[len(Master_Air)] = dfresponse #adding last read to master air data frame

		print(Master_Air)





		return fig
		if __name__ == "__main__":
	   		 app2.run_server(debug=True)


["N","P","K","PH","humidity","temp","cond","time"]
#Pushing to sql server-------------------------------
def sqlsoilsensor():


	cursor.execute("CREATE TABLE IF NOT EXISTS soil_sensortest2 (id INT(11) NOT NULL AUTO_INCREMENT, n FLOAT NOT NULL, p FLOAT NOT NULL, k FLOAT NOT NULL, ph FLOAT NOT NULL, humidity FLOAT NOT NULL, temp FLOAT NOT NULL, cond FLOAT NOT NULL, time TIMESTAMP NOT NULL, PRIMARY KEY (id))")

	cursor.execute("SELECT * FROM soil_sensortest4")
	myresult = cursor.fetchall()
	print('printing soil_sensortest2 now')




	for x in myresult:
  			print(x)

		
	sql="INSERT INTO soil_sensor (n,p,k,ph,humidity,temp,cond,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	a = instrument.read_register(N_reg)
	b=instrument.read_register(P_reg)
	c=instrument.read_register(K_reg)
	d=instrument.read_register(PH_reg)
	e=instrument.read_register(humidity_reg)
	f=instrument.read_register(temp_reg)
	g=instrument.read_register(cond_reg)
	h=datetime.datetime.now()
	print('time',h)
	insert=(a,b,c,d,e,f,g,h)
	cursor.execute(sql,insert)
	connection.commit()
		

	cursor.execute("SELECT * FROM soil_sensor")
	myresult = cursor.fetchall()
	print('printing soil_sensortest now')
	for x in myresult:
  			print(x)

user = 'admin'
password = 'biobox2024'
host = 'biobox.cl8ku2sqypva.us-east-2.rds.amazonaws.com'
port = 3306
database = 'bioboxtest'


connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()


# function to return the database connection-----------------------------------------------------





#-------------------------------------------------------------------------

#main loop with keyboard interupt----------------------------------------

#getconn()
try:
    while True:
        sqlsoilsensor()
        time.sleep(10)
except KeyboardInterrupt:
    print('interrupted!')

print("starting")
#takevalues(a)
#pubdata()
#pub2()
#soilsensor()

#requestairgradient()
print("ending")
#---------------------------------------------------------------------------

#how



