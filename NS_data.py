def ness_aws_1_time(df, data):
   import time
   from datetime import datetime
   import calendar
   import numpy as np
   
   DT = []
   ET = []
   DoY = []
   dateformats = ["['%d/%m/%Y %H:%M']", "['%d/%m/%Y %H:%M:%S']", "['%Y-%m-%d %H:%M']", "['%Y-%m-%d %H:%M:%S']"]
   
   header = df.columns
  
   #parse time
   ds = df.loc[:,header[0]:header[0]:1].values #extract date from data frame 
   
   for i in range(0, len(ds)):
      for fmt in dateformats:
         try:   
            tt = time.strptime(str(ds[i]), fmt)
            break
         except ValueError:
            pass
      #DT
      DT.append(tt[0:6])
      #Doy
      DoY.append(float(tt[7]) + ((((float(tt[5])/60) + float(tt[4]))/60) + float(tt[3]))/24) 
      #ET
      ET.append(int(calendar.timegm(tt)))

   data.DT = np.array(DT)
   data.ET = np.array(ET)
   data.DoY = np.array(DoY)
 
   return data
   
def ness_aws_1_QC(df, data):
   import numpy as np  

   # parse ot the data 
   header = df.columns
   
   #Temperature
   X = np.array(df.loc[:,header[1]:header[1]:1])
   TT = (np.float32(X) - 32) * (5/9)
   del X
  
   #Humidity
   X = np.array(df.loc[:,header[4]:header[4]:1])
   RH = np.float32(X)
   del X      
   
   #Wind speed
   X = np.array(df.loc[:,header[6]:header[6]:1])
   WS = np.float32(X) / 2.237
   del X 
   
   #Wind direction
   X = np.array(df.loc[:,header[8]:header[8]:1])
   WD = np.float32(X)
   del X
   
   #Accumulated rain and rain rate
   X = np.array(df.loc[:,header[9]:header[9]:1])
   PA = np.float32(X) * 25.4
   PR = PA * 60/5
   del X

   #Pressure
   X = np.array(df.loc[:,header[10]:header[10]:1])
   PP = np.float32(X) * 33.864
   del X
   
   #Solar
   X = np.array(df.loc[:,header[11]:header[11]:1])
   SL = np.float32(X)
   del X
   
   #UV
   X = np.array(df.loc[:,header[13]:header[13]:1])
   UV = np.float32(X) / 40
   del X
   
   #Soil Temperature 1
   X = np.array(df.loc[:,header[16]:header[16]:1])
   ST1 = (np.float32(X) - 32) * (5/9)
   del X
   
   #Soil Temperature 2
   X = np.array(df.loc[:,header[17]:header[17]:1])
   ST2 = (np.float32(X) - 32) * (5/9)
   del X
   
   #Soil Temperature 3
   X = np.array(df.loc[:,header[18]:header[18]:1])
   ST3 = (np.float32(X) - 32) * (5/9)
   del X
   
   #Soil Temperature 4
   X = np.array(df.loc[:,header[19]:header[19]:1])
   ST4 = (np.float32(X) - 32) * (5/9)
   del X
   
   #Leaf Temperature 1
   X = np.array(df.loc[:,header[20]:header[20]:1])
   LT1 = (np.float32(X) - 32) * (5/9)
   del X
   
   #Leaf Temperature 2
   X = np.array(df.loc[:,header[21]:header[21]:1])
   LT2 = (np.float32(X) - 32) * (5/9)
   del X
   
   #Soil Moisture 1
   X = np.array(df.loc[:,header[22]:header[22]:1])
   SM1 = np.float32(X)
   del X
   
   #Soil Moisture 2
   X = np.array(df.loc[:,header[23]:header[23]:1])
   SM2 = np.float32(X)
   del X
   
   #Soil Moisture 3
   X = np.array(df.loc[:,header[24]:header[24]:1])
   SM3 = np.float32(X)
   del X
   
   #Soil Moisture 4
   X = np.array(df.loc[:,header[25]:header[25]:1])
   SM4 = np.float32(X)
   del X
   
   #Leaf Wetness 1
   X = np.array(df.loc[:,header[26]:header[26]:1])
   LW1 = np.float32(X)
   del X
   
   #Leaf Wetness 2
   X = np.array(df.loc[:,header[27]:header[27]:1])
   LW2 = np.float32(X)
   del X
   
   # QC data
   # remove nans
   for n in range(len(data.DoY)):
      if np.isnan(TT[n]) == True:
         TT[n] = -1e20
      if np.isnan(RH[n]) == True:
         RH[n] = -1e20  
      if np.isnan(WS[n]) == True:
         WS[n] = -1e20
      if np.isnan(WD[n]) == True:
         WD[n] = -1e20 
      if np.isnan(PP[n]) == True:
         PP[n] = -1e20
      if np.isnan(PA[n]) == True:
         PA[n] = -1e20  
      if np.isnan(PR[n]) == True:
         PR[n] = -1e20
      if np.isnan(SL[n]) == True:
         SL[n] = -1e20 
      if np.isnan(UV[n]) == True:
         UV[n] = -1e20     
      if np.isnan(ST1[n]) == True:
         ST1[n] = -1e20  
      if np.isnan(ST2[n]) == True:
         ST2[n] = -1e20
      if np.isnan(ST3[n]) == True:
         ST3[n] = -1e20          
      if np.isnan(ST4[n]) == True:
         ST4[n] = -1e20 
      if np.isnan(LT1[n]) == True:
         LT1[n] = -1e20  
      if np.isnan(LT2[n]) == True:
         LT2[n] = -1e20
      if np.isnan(SM1[n]) == True:
         SM1[n] = -1e20  
      if np.isnan(SM2[n]) == True:
         SM2[n] = -1e20
      if np.isnan(SM3[n]) == True:
         SM3[n] = -1e20          
      if np.isnan(SM4[n]) == True:
         SM4[n] = -1e20  
      if np.isnan(LW1[n]) == True:
         LW1[n] = -1e20  
      if np.isnan(LW2[n]) == True:
         LW2[n] = -1e20         
   
   #combine multi soil and leaf sensors into one array
   ST = np.empty(shape=(len(ST1),4))
   SM = np.empty(shape=(len(SM1),4))
   LT = np.empty(shape=(len(LT1),2))
   LW = np.empty(shape=(len(LW1),2))
   
   for n in range(len(data.ET)):
      #soil temperature
      ST[n,0] = ST1[n]
      ST[n,1] = ST2[n]
      ST[n,2] = ST3[n]
      ST[n,3] = ST4[n]  
      #soil moisture
      SM[n,0] = SM1[n]
      SM[n,1] = SM2[n]
      SM[n,2] = SM3[n]
      SM[n,3] = SM4[n]   
      #leaf temperature      
      LT[n,0] = LT1[n]
      LT[n,1] = LT2[n]
      #leaf wettness      
      LW[n,0] = LW1[n]
      LW[n,1] = LW2[n]
    
   # create flags
   # Temperature
   qc_flag_temperature = np.ones_like(TT)
   #T>30 2b
   ix = np.where(TT > 30)
   try:
      qc_flag_temperature[ix] = 2
   except:
      pass
   
   #T>40 3b
   ix = np.where(TT > 40)
   try:
      qc_flag_temperature[ix] = 3
   except:
      pass
      
   #T<-10 4b
   ix = np.where((TT > -1e20) & (TT < -10))
   try:
      qc_flag_temperature[ix] = 4
   except:
      pass
   
   #T<-20 5b
   ix = np.where((TT > -1e20) & (TT < -20))
   try:
      qc_flag_temperature[ix] = 5
   except:
      pass
      
   #Missing 6b
   ix = np.where(TT == -1e20)
   try:
      qc_flag_temperature[ix] = 6
   except:
      pass
      
   #Humidity
   qc_flag_relative_humidity = np.ones_like(RH)
   #RH>100 2b
   ix = np.where(RH > 100)
   try:
      qc_flag_relative_humidity[ix] = 2
   except:
      pass
   
   #RH == 100 3b
   ix = np.where(RH == 100)
   try:
      qc_flag_relative_humidity[ix] = 3
   except:
      pass
      
   #RH<40 4b
   ix = np.where(RH < 40)
   try:
      qc_flag_relative_humidity[ix] = 4
   except:
      pass
   
   #RH<0 5b
   ix = np.where(RH < 0)
   try:
      qc_flag_relative_humidity[ix] = 5
   except:
      pass
   
   #Missing 6b
   ix = np.where(RH == -1e20)
   try:
      qc_flag_relative_humidity[ix] = 6
   except:
      pass
   
   # Presure
   qc_flag_pressure = np.ones_like(PP)
   #PP>1000 2b
   ix = np.where(PP > 1050)
   try:
      qc_flag_pressure[ix] = 2
   except:
      pass
      
   #PP>1100 3b
   ix = np.where(PP > 1100)
   try:
      qc_flag_pressure[ix] = 3
   except:
      pass
      
   #PP<950 4b
   ix = np.where(PP < 950)
   try:
      qc_flag_pressure[ix] = 4
   except:
      pass
   
   #PP<0 5b
   ix = np.where(PP < 540)
   try:
      qc_flag_pressure[ix] = 5
   except:
      pass
   
   #Missing 6b
   ix = np.where(PP == -1e20)
   try:
      qc_flag_pressure[ix] = 6
   except:
      pass
      
   #wind speed   
   qc_flag_wind_speed = np.ones_like(WS)
   #WS>30 2b
   ix = np.where(WS > 30)
   try:
      qc_flag_wind_speed[ix] = 2
   except:
      pass
  
   #WS=0 3b
   ix = np.where(WS == 0)
   try:
      qc_flag_wind_speed[ix] = 3
   except:
      pass
  
   #WS<0 4b
   ix = np.where(WS < 0)
   try:
      qc_flag_wind_speed[ix] = 4
   except:
      pass
  
   #Missing 5b
   ix = np.where(WS == -1e20)
   try:
      qc_flag_wind_speed[ix] = 5
   except:
      pass
   
   #wind direction
   qc_flag_wind_from_direction = np.ones_like(WD)
   #WD>360 2b
   ix = np.where(WD > 360)
   try:
      qc_flag_wind_from_direction[ix] = 2
   except:
      pass
      
   #WD<0 3b
   ix = np.where(WD < 0)
   try:
      qc_flag_wind_from_direction[ix] = 3
   except:
      pass
   
   #WS == 0 4b
   ix = np.where(WS == 0)
   try:
      qc_flag_wind_from_direction[ix] = 4
   except:
      pass
      
   #Missing 5b
   ix = np.where(WD == -1e20)
   try:
      qc_flag_wind_from_direction[ix] = 5
   except:
      pass
   
   #radiation
   qc_flag_radiation = np.ones_like(UV)
   #UV>2000 2b
   ix = np.where(UV > 1800)
   try:
      qc_flag_radiation[ix] = 2
   except:
      pass
      
   #UV<0 3b
   ix = np.where(UV < 0)
   try:
      qc_flag_radiation[ix] = 3
   except:
      pass
      
   #Missing UV 4b
   ix = np.where(UV == -1e20)
   try:
      qc_flag_radiation[ix] = 4
   except:
      pass
   
   #SL>2000 5b
   ix = np.where(SL > 1800)
   try:
      qc_flag_radiation[ix] = 5
   except:
      pass
      
   #SL<0 6b
   ix = np.where(SL < 0)
   try:
      qc_flag_radiation[ix] = 6
   except:
      pass
      
   #Missing SL 7b
   ix = np.where(SL == -1e20)
   try:
      qc_flag_radiation[ix] = 7
   except:
      pass
   
   #precipitation
   qc_flag_precipitation = np.ones_like(PA)
   #PA>25 2b  300 *(5/60)
   ix = np.where(PA > 25)
   try:
      qc_flag_precipitation[ix] = 2
   except:
      pass
      
   #PA<0 3b
   ix = np.where(PA < 0)
   try:
      qc_flag_precipitation[ix] = 3
   except:
      pass
   
   #Missing PA 4b
   ix = np.where(PA == -1e20)
   try:
      qc_flag_precipitation[ix] = 4
   except:
      pass
   
   #PR>300 5b
   ix = np.where(PR > 300)
   try:
      qc_flag_precipitation[ix] = 5
   except:
      pass
      
   #PR<0 6b
   ix = np.where(PR < 0)
   try:
      qc_flag_precipitation[ix] = 6
   except:
      pass
   
   #Missing PR 7b
   ix = np.where(PR == -1e20)
   try:
      qc_flag_precipitation[ix] = 7
   except:
      pass
   
   #soil temperature   
   qc_flag_soil_temperature = np.ones_like(ST)  
   #ST > 30 2b
   ix = np.where(ST > 30)
   try:
      qc_flag_soil_temperature[ix] = 2
   except:
      pass
   
   #ST 20 - 30 3b
   ix = np.where((ST > 20) & (ST < 30))
   try:
      qc_flag_soil_temperature[ix] = 3
   except:
      pass   
   
   #ST 0 - 5 4b
   ix = np.where((ST > 0) & (ST < 5))
   try:
      qc_flag_soil_temperature[ix] = 4
   except:
      pass 
   
   #ST -5 - 0 5b
   ix = np.where((ST > -5) & (ST < 0))
   try:
      qc_flag_soil_temperature[ix] = 5
   except:
      pass 
   
   #ST < -10 6b
   ix = np.where(ST < -10)
   try:
      qc_flag_soil_temperature[ix] = 6
   except:
      pass 
   
   #Missing ST 7b
   ix = np.where(ST == -1e20)
   try:
      qc_flag_soil_temperature[ix] = 7
   except:
      pass

   #soil moisture   
   qc_flag_soil_moisture = np.ones_like(SM)  
   #SM >15 2b
   ix = np.where(SM > 15)
   try:
      qc_flag_soil_moisture[ix] = 2
   except:
      pass
      
   #SM 10 - 15 3b
   ix = np.where((SM > 10) & (SM < 15))
   try:
      qc_flag_soil_moisture[ix] = 3
   except:
      pass
      
   #SM 0 - 5 4b
   ix = np.where((SM > 0) & (SM < 5))
   try:
      qc_flag_soil_moisture[ix] = 4
   except:
      pass   
   
   #Missing SM 5b
   ix = np.where(SM == -1e20)
   try:
      qc_flag_soil_moisture[ix] = 5
   except:
      pass

   #leaf temperature   
   qc_flag_leaf_temperature = np.ones_like(LT) 
   # LT > 30 2b
   ix = np.where(LT > 30)
   try:
      qc_flag_leaf_temperature[ix] = 2
   except:
      pass
   
   #LT 20 - 30 3b
   ix = np.where((LT > 20) & (LT < 30))
   try:
      qc_flag_leaf_temperature[ix] = 3
   except:
      pass   
   
   #LT 0 - 5 4b
   ix = np.where((LT > 0) & (LT < 5))
   try:
      qc_flag_leaf_temperature[ix] = 4
   except:
      pass 
   
   #LT -5 - 0 5b
   ix = np.where((LT > -5) & (LT < 0))
   try:
      qc_flag_leaf_temperature[ix] = 5
   except:
      pass 
   
   #LT < -10 6b
   ix = np.where(LT < -10)
   try:
      qc_flag_leaf_temperature[ix] = 6
   except:
      pass 
   
   #Missing LT 7b
   ix = np.where(LT == -1e20)
   try:
      qc_flag_leaf_temperature[ix] = 7
   except:
      pass

   #leaf wetness   
   qc_flag_leaf_wetness = np.ones_like(LW)  
   # LW >15 2b
   ix = np.where(LW > 15)
   try:
      qc_flag_leaf_wetness[ix] = 2
   except:
      pass
      
   #LW 10 - 15 3b
   ix = np.where((LW > 10) & (LW < 15))
   try:
      qc_flag_leaf_wetness[ix] = 3
   except:
      pass
      
   #LW 0 - 5 4b
   ix = np.where((LW > 0) & (LW < 5))
   try:
      qc_flag_leaf_wetness[ix] = 4
   except:
      pass 
      
   #Missing LW 5b
   ix = np.where(LW == -1e20)
   try:
      qc_flag_leaf_wetness[ix] = 5
   except:
      pass   
   
   # min and max
   ix = np.where(qc_flag_temperature < 3 )
   try: 
      TT_min = np.min(TT[ix])
   except:
      TT_min = -1e20
   try:
      TT_max = np.max(TT[ix])
   except:
      TT_max = -1e20
   
   ix = np.where(qc_flag_relative_humidity == 1)
   try:
      RH_min = np.min(RH[ix])
   except:
      RH_min = -1e20
   try:
      RH_max = np.max(RH[ix])
   except:
      RH_max = -1e20
   
   ix = np.where(qc_flag_wind_speed == 1)
   try:
      WS_min = np.min(WS[ix])
   except:
      WS_min = -1e20
   try:
      WS_max = np.max(WS[ix])
   except:
      WS_max = -1e20
   
   ix = np.where(qc_flag_wind_from_direction == 1)
   try:
      WD_min = np.min(WD[ix])
   except:
      WD_min = -1e20
   try:
      WD_max = np.max(WD[ix])
   except:
      WD_max = -1e20
   
   ix = np.where(qc_flag_pressure < 4)
   try:
      PP_min = np.min(PP[ix])
   except:
      PP_min = -1e20
   try:
      PP_max = np.max(PP[ix])
   except:
      PP_max = -1e20
   
   ix = np.where(qc_flag_precipitation == 1)
   try:
      PA_min = np.min(PA[ix])
   except:
      PA_min = -1e20
   try:
      PA_max = np.max(PA[ix])
   except:
      PA_max = -1e20
      
   ix = np.where(qc_flag_precipitation == 1)
   try:
      PR_min = np.min(PR[ix])
   except:
      PR_min = -1e20
   try:
      PR_max = np.max(PR[ix])
   except:
      PR_max = -1e20
      
   ix = np.where(qc_flag_radiation == 1)
   try:
      SL_min = np.min(SL[ix])
   except:
      SL_min = -1e20
   try:
      SL_max = np.max(SL[ix])
   except:
      SL_max = -1e20
      
   ix = np.where(qc_flag_radiation == 1)
   try:
      UV_min = np.min(UV[ix])
   except:
      UV_min = -1e20
   try:
      UV_max = np.max(UV[ix])
   except:
      UV_max = -1e20
   
   ix = np.where(qc_flag_soil_temperature == 1)
   try:
      ST_min = np.min(ST[ix])
   except:
      ST_min = -1e20
   try:
      ST_max = np.max(ST[ix])
   except: 
      ST_max = -1e20
   
   ix = np.where(qc_flag_soil_moisture == 1)
   try:
      SM_min = np.min(SM[ix])
   except:
      SM_min = -1e20
   try:
      SM_max = np.max(SM[ix])
   except:
      SM_max = -1e20
   
   ix = np.where(qc_flag_leaf_temperature == 1)
   try:
      LT_min = np.min(LT[ix])
   except:
      LT_min = -1e20
   try:
      LT_max = np.max(LT[ix])
   except:
      LT_max = -1e20
      
   ix = np.where(qc_flag_leaf_wetness == 1)
   try:
      LW_min = np.min(LW[ix])
   except:
      LW_min = -1e20
   try:
      LW_max = np.max(LW[ix])
   except: 
      LW_max = -1e20
   
   #convert temperature to kelvin
   #air temperature
   ix = np.where(TT > -1e20)
   try:
      TT[ix] = TT[ix] + 273.15
   except:
      pass
   if TT_min > -1e20:
      TT_min = TT_min + 273.15
   if TT_max > -1e20:
      TT_max = TT_max + 273.15
   
   #soil temperature
   ix = np.where(ST > -1e20)
   try:
      ST[ix] = ST[ix] + 273.15
   except:
      pass
   if ST_min > -1e20:
      ST_min = ST_min + 273.15
   if ST_max > -1e20:
      ST_max = TT_max + 273.15
   
   #leaf temperature
   ix = np.where(LT > -1e20)
   try:
      LT[ix] = LT[ix] + 273.15
   except:
      pass
   if LT_min > -1e20:
      LT_min = LT_min + 273.15
   if LT_max > -1e20:
      LT_max = LT_max + 273.15
   
   data.TT = TT
   data.TT_min = TT_min
   data.TT_max = TT_max
   data.RH = RH
   data.RH_min = RH_min
   data.RH_max = RH_max
   data.WS = WS
   data.WS_min = WS_min
   data.WS_max = WS_max
   data.WD = WD
   data.WD_min = WD_min
   data.WD_max = WD_max
   data.PP = PP
   data.PP_min = PP_min
   data.PP_max = PP_max
   data.PA = PA
   data.PA_min = PA_min
   data.PA_max = PA_max
   data.PR = PR
   data.PR_min = PR_min
   data.PR_max = PR_max
   data.SL = SL
   data.SL_min = SL_min
   data.SL_max = SL_max
   data.UV = UV
   data.UV_min = UV_min
   data.UV_max = UV_max
   data.ST = ST
   data.ST_min = ST_min
   data.ST_max = ST_max
   data.SM = SM
   data.SM_min = SM_min
   data.SM_max = SM_max
   data.LT = LT
   data.LT_min = LT_min
   data.LT_max = LT_max
   data.LW = LW
   data.LW_min = LW_min
   data.LW_max = LW_max
   data.qc_flag_temperature = qc_flag_temperature
   data.qc_flag_relative_humidity = qc_flag_relative_humidity
   data.qc_flag_pressure = qc_flag_pressure
   data.qc_flag_wind_speed = qc_flag_wind_speed
   data.qc_flag_wind_from_direction = qc_flag_wind_from_direction
   data.qc_flag_radiation = qc_flag_radiation
   data.qc_flag_precipitation = qc_flag_precipitation
   data.qc_flag_soil_temperature = qc_flag_soil_temperature
   data.qc_flag_soil_moisture = qc_flag_soil_moisture
   data.qc_flag_leaf_temperature = qc_flag_leaf_temperature
   data.qc_flag_leaf_wetness = qc_flag_leaf_wetness
   
   return data  

def ness_aws_1(fn_in, data, logfile): 
   import pandas as pd  
   from datetime import datetime
  
   try:
      df = pd.read_csv(fn_in)
   except:
      # exit if problem encountered
      print("Unable to open data file: ", fn_in, ". This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Unable to open data file: ' + fn_in + 'Program will terminate.\n')
      g.close()
      exit()
   
   #parse time
   data = ness_aws_1_time(df, data)
   
   #parse_data
   data = ness_aws_1_QC(df, data)
   
   return data 
   
def ness_aws_2_time(df, data):
   import time
   from datetime import datetime
   import calendar
   import numpy as np
   
   DT = []
   ET = []
   DoY = []
   dateformats = ["['%Y%m%d %H:%M']", "['%Y%m%d %H:%M:%S']", "['%d/%m/%Y %H:%M']", "['%d/%m/%Y %H:%M:%S']", "['%Y-%m-%d %H:%M']", "['%Y-%m-%d %H:%M:%S']"]
   
   header = df.columns
  
   #parse time
   ds = df.loc[:,header[0]:header[0]:1].values #extract date from data frame 
   
   for i in range(1, len(ds)):
      for fmt in dateformats:
         try:   
            tt = time.strptime(str(ds[i]), fmt)
            break
         except ValueError:
            pass    
      
      #DT
      DT.append(tt[0:6])
      #Doy
      DoY.append(float(tt[7]) + ((((float(tt[5])/60) + float(tt[4]))/60) + float(tt[3]))/24) 
      #ET
      ET.append(int(calendar.timegm(tt)))

   data.DT = np.array(DT)
   data.ET = np.array(ET)
   data.DoY = np.array(DoY)
   
   return data
   
def ness_aws_2_QC(df, data):
   import numpy as np  

   # parse ot the data 
   header = df.columns
   #Temperature
   X = np.array(df.loc[1:len(df),header[1]:header[1]:1])
   TT = np.float32(X)
   del X
  
   #Humidity
   X = np.array(df.loc[1:len(df),header[4]:header[4]:1])
   RH = np.float32(X)
   del X      
   
   #Wind speed
   X = np.array(df.loc[1:len(df),header[6]:header[6]:1])
   WS = np.float32(X)
   del X 
   
   #Wind direction
   X = np.array(df.loc[1:len(df),header[8]:header[8]:1])
   WD = np.float32(X)
   del X
   
   #Accumulated rain and rain rate
   X = np.array(df.loc[1:len(df),header[9]:header[9]:1])
   PA = np.float32(X)
   PR = PA * 60/5
   del X

   #Pressure
   X = np.array(df.loc[1:len(df),header[10]:header[10]:1])
   PP = np.float32(X)
   del X
   
   #Solar
   X = np.array(df.loc[1:len(df),header[11]:header[11]:1])
   SL = np.float32(X)
   del X
   
   #UV
   X = np.array(df.loc[1:len(df),header[13]:header[13]:1])
   UV = np.float32(X) / 40
   del X
   
   # QC data
   # remove nans
   for n in range(len(data.DoY)):
      if np.isnan(TT[n]) == True:
         TT[n] = -1e20
      if np.isnan(RH[n]) == True:
         RH[n] = -1e20  
      if np.isnan(WS[n]) == True:
         WS[n] = -1e20
      if np.isnan(WD[n]) == True:
         WD[n] = -1e20 
      if np.isnan(PP[n]) == True:
         PP[n] = -1e20
      if np.isnan(PA[n]) == True:
         PA[n] = -1e20  
      if np.isnan(PR[n]) == True:
         PR[n] = -1e20
      if np.isnan(SL[n]) == True:
         SL[n] = -1e20 
      if np.isnan(UV[n]) == True:
         UV[n] = -1e20             
   
   #combine multi soil and leaf sensors into one array
   ST = np.ones(shape=(len(TT),4)) * -1e20
   SM = np.ones(shape=(len(TT),4)) * -1e20
   LT = np.ones(shape=(len(TT),2)) * -1e20
   LW = np.ones(shape=(len(TT),2)) * -1e20
    
   # create flags
   # Temperature
   qc_flag_temperature = np.ones_like(TT)
   #T>30 2b
   ix = np.where(TT > 30)
   try:
      qc_flag_temperature[ix] = 2
   except:
      pass
   
   #T>40 3b
   ix = np.where(TT > 40)
   try:
      qc_flag_temperature[ix] = 3
   except:
      pass
      
   #T<-10 4b
   ix = np.where((TT > -1e20) & (TT < -10))
   try:
      qc_flag_temperature[ix] = 4
   except:
      pass
   
   #T<-20 5b
   ix = np.where((TT > -1e20) & (TT < -20))
   try:
      qc_flag_temperature[ix] = 5
   except:
      pass
      
   #Missing 6b
   ix = np.where(TT == -1e20)
   try:
      qc_flag_temperature[ix] = 6
   except:
      pass
      
   #Humidity
   qc_flag_relative_humidity = np.ones_like(RH)
   #RH>100 2b
   ix = np.where(RH > 100)
   try:
      qc_flag_relative_humidity[ix] = 2
   except:
      pass
   
   #RH == 100 3b
   ix = np.where(RH == 100)
   try:
      qc_flag_relative_humidity[ix] = 3
   except:
      pass
      
   #RH<40 4b
   ix = np.where(RH < 40)
   try:
      qc_flag_relative_humidity[ix] = 4
   except:
      pass
   
   #RH<0 5b
   ix = np.where(RH < 0)
   try:
      qc_flag_relative_humidity[ix] = 5
   except:
      pass
   
   #Missing 6b
   ix = np.where(RH == -1e20)
   try:
      qc_flag_relative_humidity[ix] = 6
   except:
      pass
   
   # Presure
   qc_flag_pressure = np.ones_like(PP)
   #PP>1000 2b
   ix = np.where(PP > 1050)
   try:
      qc_flag_pressure[ix] = 2
   except:
      pass
      
   #PP>1100 3b
   ix = np.where(PP > 1100)
   try:
      qc_flag_pressure[ix] = 3
   except:
      pass
      
   #PP<950 4b
   ix = np.where(PP < 950)
   try:
      qc_flag_pressure[ix] = 4
   except:
      pass
   
   #PP<0 5b
   ix = np.where(PP < 540)
   try:
      qc_flag_pressure[ix] = 5
   except:
      pass
   
   #Missing 6b
   ix = np.where(PP == -1e20)
   try:
      qc_flag_pressure[ix] = 6
   except:
      pass
      
   #wind speed   
   qc_flag_wind_speed = np.ones_like(WS)
   #WS>30 2b
   ix = np.where(WS > 30)
   try:
      qc_flag_wind_speed[ix] = 2
   except:
      pass
  
   #WS=0 3b
   ix = np.where(WS == 0)
   try:
      qc_flag_wind_speed[ix] = 3
   except:
      pass
  
   #WS<0 4b
   ix = np.where(WS < 0)
   try:
      qc_flag_wind_speed[ix] = 4
   except:
      pass
  
   #Missing 5b
   ix = np.where(WS == -1e20)
   try:
      qc_flag_wind_speed[ix] = 5
   except:
      pass
   
   #wind direction
   qc_flag_wind_from_direction = np.ones_like(WD)
   #WD>360 2b
   ix = np.where(WD > 360)
   try:
      qc_flag_wind_from_direction[ix] = 2
   except:
      pass
      
   #WD<0 3b
   ix = np.where(WD < 0)
   try:
      qc_flag_wind_from_direction[ix] = 3
   except:
      pass
   
   #WS == 0 4b
   ix = np.where(WS == 0)
   try:
      qc_flag_wind_from_direction[ix] = 4
   except:
      pass
      
   #Missing 5b
   ix = np.where(WD == -1e20)
   try:
      qc_flag_wind_from_direction[ix] = 5
   except:
      pass
   
   #radiation
   qc_flag_radiation = np.ones_like(UV)
   #UV>2000 2b
   ix = np.where(UV > 1800)
   try:
      qc_flag_radiation[ix] = 2
   except:
      pass
      
   #UV<0 3b
   ix = np.where(UV < 0)
   try:
      qc_flag_radiation[ix] = 3
   except:
      pass
      
   #Missing UV 4b
   ix = np.where(UV == -1e20)
   try:
      qc_flag_radiation[ix] = 4
   except:
      pass
   
   #SL>2000 5b
   ix = np.where(SL > 1800)
   try:
      qc_flag_radiation[ix] = 5
   except:
      pass
      
   #SL<0 6b
   ix = np.where(SL < 0)
   try:
      qc_flag_radiation[ix] = 6
   except:
      pass
      
   #Missing SL 7b
   ix = np.where(SL == -1e20)
   try:
      qc_flag_radiation[ix] = 7
   except:
      pass
   
   #precipitation
   qc_flag_precipitation = np.ones_like(PA)
   #PA>25 2b  300 *(5/60)
   ix = np.where(PA > 25)
   try:
      qc_flag_precipitation[ix] = 2
   except:
      pass
      
   #PA<0 3b
   ix = np.where(PA < 0)
   try:
      qc_flag_precipitation[ix] = 3
   except:
      pass
   
   #Missing PA 4b
   ix = np.where(PA == -1e20)
   try:
      qc_flag_precipitation[ix] = 4
   except:
      pass
   
   #PR>300 5b
   ix = np.where(PR > 300)
   try:
      qc_flag_precipitation[ix] = 5
   except:
      pass
      
   #PR<0 6b
   ix = np.where(PR < 0)
   try:
      qc_flag_precipitation[ix] = 6
   except:
      pass
   
   #Missing PR 7b
   ix = np.where(PR == -1e20)
   try:
      qc_flag_precipitation[ix] = 7
   except:
      pass
   
   #soil temperature   
   qc_flag_soil_temperature = np.ones_like(ST)  
   #ST > 30 2b
   ix = np.where(ST > 30)
   try:
      qc_flag_soil_temperature[ix] = 2
   except:
      pass
   
   #ST 20 - 30 3b
   ix = np.where((ST > 20) & (ST < 30))
   try:
      qc_flag_soil_temperature[ix] = 3
   except:
      pass   
   
   #ST 0 - 5 4b
   ix = np.where((ST > 0) & (ST < 5))
   try:
      qc_flag_soil_temperature[ix] = 4
   except:
      pass 
   
   #ST -5 - 0 5b
   ix = np.where((ST > -5) & (ST < 0))
   try:
      qc_flag_soil_temperature[ix] = 5
   except:
      pass 
   
   #ST < -10 6b
   ix = np.where(ST < -10)
   try:
      qc_flag_soil_temperature[ix] = 6
   except:
      pass 
   
   #Missing ST 7b
   ix = np.where(ST == -1e20)
   try:
      qc_flag_soil_temperature[ix] = 7
   except:
      pass

   #soil moisture   
   qc_flag_soil_moisture = np.ones_like(SM)  
   #SM >15 2b
   ix = np.where(SM > 200)
   try:
      qc_flag_soil_moisture[ix] = 2
   except:
      pass
      
   #SM 0 - 10 3b soil very wet
   ix = np.where((SM > 0) & (SM < 10))
   try:
      qc_flag_soil_moisture[ix] = 3
   except:
      pass
      
   #SM 100 - 150 4b soil very dry
   ix = np.where((SM > 100) & (SM < 150))
   try:
      qc_flag_soil_moisture[ix] = 4
   except:
      pass   
     
   #SM <0 5b
   ix = np.where(SM < 0)
   try:
      qc_flag_soil_moisture[ix] = 5
   except:
      pass      
   
   #Missing SM 6b
   ix = np.where(SM == -1e20)
   try:
      qc_flag_soil_moisture[ix] = 6
   except:
      pass

   #leaf temperature   
   qc_flag_leaf_temperature = np.ones_like(LT) 
   # LT > 30 2b
   ix = np.where(LT > 30)
   try:
      qc_flag_leaf_temperature[ix] = 2
   except:
      pass
   
   #LT 20 - 30 3b
   ix = np.where((LT > 20) & (LT < 30))
   try:
      qc_flag_leaf_temperature[ix] = 3
   except:
      pass   
   
   #LT 0 - 5 4b
   ix = np.where((LT > 0) & (LT < 5))
   try:
      qc_flag_leaf_temperature[ix] = 4
   except:
      pass 
   
   #LT -5 - 0 5b
   ix = np.where((LT > -5) & (LT < 0))
   try:
      qc_flag_leaf_temperature[ix] = 5
   except:
      pass 
   
   #LT < -10 6b
   ix = np.where(LT < -10)
   try:
      qc_flag_leaf_temperature[ix] = 6
   except:
      pass 
   
   #Missing LT 7b
   ix = np.where(LT == -1e20)
   try:
      qc_flag_leaf_temperature[ix] = 7
   except:
      pass

   #leaf wetness   
   qc_flag_leaf_wetness = np.ones_like(LW)  
   # LW >15 2b
   ix = np.where(LW > 15)
   try:
      qc_flag_leaf_wetness[ix] = 2
   except:
      pass
      
   #LW 10 - 15 3b
   ix = np.where((LW > 10) & (LW < 15))
   try:
      qc_flag_leaf_wetness[ix] = 3
   except:
      pass
      
   #LW 0 - 5 4b
   ix = np.where((LW > 0) & (LW < 5))
   try:
      qc_flag_leaf_wetness[ix] = 4
   except:
      pass 
      
   #LW <0 5b
   ix = np.where(LW < 0)
   try:
      qc_flag_leaf_wetness[ix] = 5
   except:
      pass   
      
   #Missing LW 6b
   ix = np.where(LW == -1e20)
   try:
      qc_flag_leaf_wetness[ix] = 6
   except:
      pass   
   
   # min and max
   ix = np.where(qc_flag_temperature < 3 )
   try: 
      TT_min = np.min(TT[ix])
   except:
      TT_min = -1e20
   try:
      TT_max = np.max(TT[ix])
   except:
      TT_max = -1e20
   
   ix = np.where(qc_flag_relative_humidity == 1)
   try:
      RH_min = np.min(RH[ix])
   except:
      RH_min = -1e20
   try:
      RH_max = np.max(RH[ix])
   except:
      RH_max = -1e20
   
   ix = np.where(qc_flag_wind_speed == 1)
   try:
      WS_min = np.min(WS[ix])
   except:
      WS_min = -1e20
   try:
      WS_max = np.max(WS[ix])
   except:
      WS_max = -1e20
   
   ix = np.where(qc_flag_wind_from_direction == 1)
   try:
      WD_min = np.min(WD[ix])
   except:
      WD_min = -1e20
   try:
      WD_max = np.max(WD[ix])
   except:
      WD_max = -1e20
   
   ix = np.where(qc_flag_pressure < 4)
   try:
      PP_min = np.min(PP[ix])
   except:
      PP_min = -1e20
   try:
      PP_max = np.max(PP[ix])
   except:
      PP_max = -1e20
   
   ix = np.where(qc_flag_precipitation == 1)
   try:
      PA_min = np.min(PA[ix])
   except:
      PA_min = -1e20
   try:
      PA_max = np.max(PA[ix])
   except:
      PA_max = -1e20
      
   ix = np.where(qc_flag_precipitation == 1)
   try:
      PR_min = np.min(PR[ix])
   except:
      PR_min = -1e20
   try:
      PR_max = np.max(PR[ix])
   except:
      PR_max = -1e20
      
   ix = np.where(qc_flag_radiation == 1)
   try:
      SL_min = np.min(SL[ix])
   except:
      SL_min = -1e20
   try:
      SL_max = np.max(SL[ix])
   except:
      SL_max = -1e20
      
   ix = np.where(qc_flag_radiation == 1)
   try:
      UV_min = np.min(UV[ix])
   except:
      UV_min = -1e20
   try:
      UV_max = np.max(UV[ix])
   except:
      UV_max = -1e20
   
   ix = np.where(qc_flag_soil_temperature == 1)
   try:
      ST_min = np.min(ST[ix])
   except:
      ST_min = -1e20
   try:
      ST_max = np.max(ST[ix])
   except: 
      ST_max = -1e20
   
   ix = np.where(qc_flag_soil_moisture == 1)
   try:
      SM_min = np.min(SM[ix])
   except:
      SM_min = -1e20
   try:
      SM_max = np.max(SM[ix])
   except:
      SM_max = -1e20
   
   ix = np.where(qc_flag_leaf_temperature == 1)
   try:
      LT_min = np.min(LT[ix])
   except:
      LT_min = -1e20
   try:
      LT_max = np.max(LT[ix])
   except:
      LT_max = -1e20
      
   ix = np.where(qc_flag_leaf_wetness == 1)
   try:
      LW_min = np.min(LW[ix])
   except:
      LW_min = -1e20
   try:
      LW_max = np.max(LW[ix])
   except: 
      LW_max = -1e20
   
   #convert temperature to kelvin
   #air temperature
   ix = np.where(TT > -1e20)
   try:
      TT[ix] = TT[ix] + 273.15
   except:
      pass
   if TT_min > -1e20:
      TT_min = TT_min + 273.15
   if TT_max > -1e20:
      TT_max = TT_max + 273.15
   
   #soil temperature
   ix = np.where(ST > -1e20)
   try:
      ST[ix] = ST[ix] + 273.15
   except:
      pass
   if ST_min > -1e20:
      ST_min = ST_min + 273.15
   if ST_max > -1e20:
      ST_max = TT_max + 273.15
   
   #leaf temperature
   ix = np.where(LT > -1e20)
   try:
      LT[ix] = LT[ix] + 273.15
   except:
      pass
   if LT_min > -1e20:
      LT_min = LT_min + 273.15
   if LT_max > -1e20:
      LT_max = LT_max + 273.15
   
   data.TT = TT
   data.TT_min = TT_min
   data.TT_max = TT_max
   data.RH = RH
   data.RH_min = RH_min
   data.RH_max = RH_max
   data.WS = WS
   data.WS_min = WS_min
   data.WS_max = WS_max
   data.WD = WD
   data.WD_min = WD_min
   data.WD_max = WD_max
   data.PP = PP
   data.PP_min = PP_min
   data.PP_max = PP_max
   data.PA = PA
   data.PA_min = PA_min
   data.PA_max = PA_max
   data.PR = PR
   data.PR_min = PR_min
   data.PR_max = PR_max
   data.SL = SL
   data.SL_min = SL_min
   data.SL_max = SL_max
   data.UV = UV
   data.UV_min = UV_min
   data.UV_max = UV_max
   data.ST = ST
   data.ST_min = ST_min
   data.ST_max = ST_max
   data.SM = SM
   data.SM_min = SM_min
   data.SM_max = SM_max
   data.LT = LT
   data.LT_min = LT_min
   data.LT_max = LT_max
   data.LW = LW
   data.LW_min = LW_min
   data.LW_max = LW_max
   data.qc_flag_temperature = qc_flag_temperature
   data.qc_flag_relative_humidity = qc_flag_relative_humidity
   data.qc_flag_pressure = qc_flag_pressure
   data.qc_flag_wind_speed = qc_flag_wind_speed
   data.qc_flag_wind_from_direction = qc_flag_wind_from_direction
   data.qc_flag_radiation = qc_flag_radiation
   data.qc_flag_precipitation = qc_flag_precipitation
   data.qc_flag_soil_temperature = qc_flag_soil_temperature
   data.qc_flag_soil_moisture = qc_flag_soil_moisture
   data.qc_flag_leaf_temperature = qc_flag_leaf_temperature
   data.qc_flag_leaf_wetness = qc_flag_leaf_wetness
   
   return data    

def ness_aws_2(fn_in, data, logfile): 
   import pandas as pd  
   from datetime import datetime
  
   try:
      df = pd.read_table(fn_in)
   except:
      # exit if problem encountered
      print("Unable to open data file: ", fn_in, ". This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Unable to open data file: ' + fn_in + 'Program will terminate.\n')
      g.close()
      exit()
   
   #parse time
   data = ness_aws_2_time(df, data)
   
   #parse_data
   data = ness_aws_2_QC(df, data)
   
   return data  