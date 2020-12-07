def create_CSV_file(nm, dp, ver, opt1, opt2, opt3, start_date):
   from datetime import datetime
   
   try:
      # create csv file_name
      dout = 'Data\\'
      f1 = nm # instrument name
      f2 = 'ness-gardens'
      f3 = datetime.fromtimestamp(int(start_date)).strftime('%Y%m%d') # daily files
      f4 = dp # data product
      f5 = 'v' + ver # version number
      f6 = '.csv'
      if ((len(opt1)<1) and (len(opt2)<1) and (len(opt3)<1)):
         fn = dout+f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+f5+f6         
      if ((len(opt1)>1) and (len(opt2)<1) and (len(opt3)<1)):
         fn = dout+f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+f5+f6
      if ((len(opt1)>1) and (len(opt2)>1) and (len(opt3)<1)):
         fn = dout+f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+opt2+chr(95)+f5+f6
      if ((len(opt1)>1) and (len(opt2)>1) and (len(opt3)>1)):
         fn = dout+f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+opt2+chr(95)+opt3+chr(95)+f5+f6
   except:
      print('error')
   
   return fn
   
def write_file_atts(meta, ET, f):
   from datetime import datetime
  
   for x in range(0,len(meta[:,0])):
      row = meta[x,0] + ',' + meta[x,1] + '\n'
      if 'last_revised_date' in meta[x,0]:
         row = meta[x,0] + ',G,' + datetime.utcnow().strftime('%Y-%m-%d') + '\n'# isoformat() + '\n'
      if 'date_valid' in meta[x,0]:
         row = meta[x,0] + ',G,' + datetime.fromtimestamp(int(ET[0])).strftime('%Y-%m-%d') + '\n'
      
      f.write("{}".format(row))
    
   del datetime
   
def write_var_atts(f, data):
   import numpy as np
   
   #1. time
   row = 'type,1,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,1,time' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,1,time,seconds since 1970-01-01 00:00:00,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,1,Time,seconds since 1970-01-01 00:00:00' + '\n'
   f.write("{}".format(row))
   row = 'axis,1,T,CF' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,1,' + str(np.float64(min(data.ET))) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,1,' + str(np.float64(max(data.ET))) + '\n'
   f.write("{}".format(row))
   row = 'calendar,1,standard' + '\n'
   f.write("{}".format(row))		

   #2. day_of_year
   row = 'type,2,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,2,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,2,Day of Year,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,2,' + str(np.int32(min(data.DoY))) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,2,' + str(np.int32(max(data.DoY))) + '\n'
   f.write("{}".format(row))
   
   #3. year
   row = 'type,3,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,3,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,3,Year,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,3,' + str(np.int32(min(data.DT[:,0]))) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,3,' + str(np.int32(max(data.DT[:,0]))) + '\n'
   f.write("{}".format(row))
   
   #4. month
   row = 'type,4,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,4,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,4,Month,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,4,' + str(np.int32(min(data.DT[:,1]))) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,4,' + str(np.int32(max(data.DT[:,1]))) + '\n'
   f.write("{}".format(row))
   
   #5. day
   row = 'type,5,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,5,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,5,Day,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,5,' + str(np.int32(min(data.DT[:,2]))) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,5,' + str(np.int32(max(data.DT[:,2]))) + '\n'
   f.write("{}".format(row))
   
   #6. hour
   row = 'type,6,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,6,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,6,Hour,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,6,' + str(np.int32(min(data.DT[:,3]))) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,6,' + str(np.int32(max(data.DT[:,3]))) + '\n'
   f.write("{}".format(row))
   
   #7. minute
   row = 'type,7,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,7,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,7,Minute,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,7,' + str(np.int32(min(data.DT[:,4]))) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,7,' + str(np.int32(max(data.DT[:,4]))) + '\n'
   f.write("{}".format(row))
   
   #8. second
   row = 'type,8,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,8,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,8,Second,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,8,' + str(np.float32(min(data.DT[:,5]))) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,8,' + str(np.float32(max(data.DT[:,5]))) + '\n'
   f.write("{}".format(row))
   
   #9. latitude
   row = 'type,9,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,9,latitude' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,9,latitude,degrees_north,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,9,Latitude,degrees_north' + '\n'
   f.write("{}".format(row))
   
   #10. longitude
   row = 'type,10,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,10,longitude' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,10,longitude,degrees_east,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,10,Longitude,degrees_east' + '\n'
   f.write("{}".format(row))
   
   #11. air_pressure
   row = 'type,11,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,11,time' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,11,air_pressure,hPa,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,11,Air Pressure,hPa' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,11,' + str(np.float32(data.PP_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,11,' + str(np.float32(data.PP_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,11,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,11,latitude longitude' + '\n'
   f.write("{}".format(row))	
   
   #12. air_temperature
   row = 'type,12,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,12,time' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,12,air_temperature,K,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,12,Air Temperature,K' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,12,' + str(np.float32(data.TT_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,12,' + str(np.float32(data.TT_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,12,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,12,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #13. relative_humidity
   row = 'type,13,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,13,time' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,13,relative_humidity,%,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,13,Relative Humidity,%' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,13,' + str(np.float32(data.RH_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,13,' + str(np.float32(data.RH_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,13,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,13,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #14. wind_speed
   row = 'type,14,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,14,time' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,14,wind_speed,m s-1,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,14,Wind Speed,m s-1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,14,' + str(np.float32(data.WS_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,14,' + str(np.float32(data.WS_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,14,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,14,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #15. wind_from_direction
   row = 'type,15,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,15,time' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,15,wind_from_direction,degree,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,15,Wind From Direction,degree' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,15,' + str(np.float32(data.WD_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,15,' + str(np.float32(data.WD_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,15,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,15,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #16. thickness_of_rainfall_amount
   row = 'type,16,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,16,time' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,16,thickness_of_rainfall_amount,mm,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,16,Rain Accumulated in Averaging Period,mm' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,16,' + str(np.float32(data.PA_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,16,' + str(np.float32(data.PA_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,16,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,16,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #17. rainfall_rate
   row = 'type,17,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,17,time' + '\n'
   f.write("{}".format(row))
   row = 'standard_name,17,rainfall_rate,mm hr-1,CF' + '\n'
   f.write("{}".format(row))
   row = 'long_name,17,Rainfall Rate,mm hr-1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,17,' + str(np.float32(data.PR_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,17,' + str(np.float32(data.PR_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,17,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,17,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #18. downwelling_cie_weighted_uv_flux_in_air
   row = 'type,18,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,18,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,18,Downwelling CIE Weighted UV Radiative Flux,W m-2' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,18,' + str(np.float32(data.UV_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,18,' + str(np.float32(data.UV_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,18,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,18,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #19. downwelling_total_irradiance
   row = 'type,19,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,19,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,19,Downwelling Total Radiative Flux,W m-2' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,19,' + str(np.float32(data.SL_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,19,' + str(np.float32(data.SL_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,19,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,19,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #20. soil_temperature_bare_concrete
   row = 'type,20,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,20,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,20,Soil Temperature Bare Concrete,K' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,20,' + str(np.float32(data.ST_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,20,' + str(np.float32(data.ST_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,20,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,20,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #21. soil_temperature_grass
   row = 'type,21,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,21,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,21,Soil Temperature Grass,K' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,21,' + str(np.float32(data.ST_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,21,' + str(np.float32(data.ST_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,21,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,21,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #22. soil_temperature_bare_soil
   row = 'type,22,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,22,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,22,Soil Temperature Bare Soil,K' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,22,' + str(np.float32(data.ST_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,22,' + str(np.float32(data.ST_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,22,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,22,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #23. soil_temperature_10cm_below_grass_surface
   row = 'type,23,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,23,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,23,Soil Temperature 10cm Below Grass Surface,K' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,23,' + str(np.float32(data.ST_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,23,' + str(np.float32(data.ST_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,23,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,23,latitude longitud' + '\n'
   f.write("{}".format(row))
   
   #24. soil_moisture_10cm_below_grass_surface
   row = 'type,24,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,24,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,24,Soil Moisture 10cm Below Grass Surface,cbar' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,24,' + str(np.float32(data.SM_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,24,' + str(np.float32(data.SM_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,24,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,24,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #25. soil_moisture_20cm_below_grass_surface
   row = 'type,25,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,25,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,25,Soil Moisture 20cm Below Grass Surface,cbar' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,25,' + str(np.float32(data.SM_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,25,' + str(np.float32(data.SM_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,25,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,25,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #26. soil_moisture_30cm_below_grass_surface
   row = 'type,26,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,26,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,26,Soil Moisture 30cm Below Grass Surface,cbar' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,26,' + str(np.float32(data.SM_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,26,' + str(np.float32(data.SM_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,26,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,26,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #27. soil_moisture_50cm_below_grass_surface
   row = 'type,27,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,27,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,27,Soil Moisture 50cm Below Grass Surface,cbar' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,27,' + str(np.float32(data.SM_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,27,' + str(np.float32(data.SM_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,27,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,27,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #28. leaf_temperature_50cm
   row = 'type,28,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,28,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,28,Leaf Temperature at 50cm,K' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,28,' + str(np.float32(data.LT_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,28,' + str(np.float32(data.LT_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,28,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,28,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #29. leaf_temperature_2m
   row = 'type,29,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,29,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,29,Leaf Temperature at 2m,K' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,29,' + str(np.float32(data.LT_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,29,' + str(np.float32(data.LT_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,29,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,29,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #30. leaf_wetness_50cm
   row = 'type,30,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,30,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,30,Leaf Wetness at 50cm,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,30,' + str(np.float32(data.LW_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,30,' + str(np.float32(data.LW_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,30,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,30,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #31. leaf_wetness_2m
   row = 'type,31,float' + '\n'
   f.write("{}".format(row))
   row = 'dimension,31,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,31,Leaf Wetness at 2m,1' + '\n'
   f.write("{}".format(row))
   row = 'valid_min,31,' + str(np.float32(data.LW_min)) + '\n'
   f.write("{}".format(row))
   row = 'valid_max,31,' + str(np.float32(data.LW_max)) + '\n'
   f.write("{}".format(row))
   row = 'cell_methods,31,time: mean' + '\n' 
   f.write("{}".format(row))
   row = 'coordinates,31,latitude longitude' + '\n'
   f.write("{}".format(row))
   
   #32. qc_flag_temperature
   row = 'type,32,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,32,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,32,Data Quality Flag: Temperature,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,32,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,32,not_used,good_data,suspect_data:_air_temperature>30C,suspect_data:_air_temperatrue>40C,suspect_data:_air_temperature<-10C,suspect_data:_air_temperature<-20C,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #33. qc_flag_relative_humidity
   row = 'type,33,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,33,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,33,Data Quality Flag: Relative Humidity,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,33,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,33,not_used,good_data,bad_data:_relative_humidity>100%,suspect_data:_relative_humidity=100%,suspect_data:_relative_himidity<40%,bad_data:_relative_himidity<0%,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #34. qc_flag_pressure
   row = 'type,34,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,34,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,34,Data Quality Flag: Pressure,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,34,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,34,not_used,good_data,good_data:_pressure>1050hPa,suspect_data:_pressure=1100hPa,suspect_data:_pressure<950hPa,bad_data:_pressure<540hPa,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #35. qc_flag_wind_speed
   row = 'type,35,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,35,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,35,Data Quality Flag: Wind Speed,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,35,0,1,2,3,4,5' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,35,not_used,good_data,suspect_data:_wind_speed>30ms-1,suspect_data:_wind_speed=0ms-1,bad_data:_wind_speed<0ms-1,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #36. qc_flag_wind_from_direction
   row = 'type,36,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,36,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,36,Data Quality Flag: Wind Direction,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,36,0,1,2,3,4,5' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,36,not_used,good_data,bad_data:_wind_direction>360degrees,bad_data:_wind_direction<0degrees,suspect_data:_wind_speed=0ms-1,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #37. qc_flag_radiation
   row = 'type,37,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,37,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,37,Data Quality Flag: Radiation,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,37,0,1,2,3,4,5,6,7' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,37,not_used,good_data,suspect_data:UV>1800Wm-2,bad_data:UV<0Wm-2,bad_data:UV_missing_data,suspect_data:_total_irradiance(Solar)>1800ms-1,bad_data:_total_irradiance(Solar)<0ms-1,bad_data:_total_irradiance_missing_data' + '\n'
   f.write("{}".format(row))
   
   #38. qc_flag_precipitation
   row = 'type,38,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,38,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,38,Data Quality Flag: Precipitation,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,38,0,1,2,3,4,5,6,7' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,38,not_used,good_data,suspect_data:_accumulated_rain>25mm,bad_data:_accumulated_rain<0mm,bad_data:_accumulated_rain_missing_data,suspect_data:_rainfall_rate>300mmhr-1,bad_data:_rainfall_rate<0mmhr-1,bad_data:_rainfall_rate_missing_data' + '\n'
   f.write("{}".format(row))
   
   #39. qc_flag_soil_temperature_bare_concrete
   row = 'type,39,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,39,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,39,Data Quality Flag: Bare Contrete Temperature,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,39,0,1,2,3,4,5,6,7' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,39,not_used,good_data,suspect_data:_soil_temperature>30C,suspect_data:_soil_temperatrue_in_band_20C_to_30C,suspect_data:_soil_temperature_in_band_0C_to_5C,suspect_data:_soil_temperature_in_band_-5C_to_0C,suspect_data:_soil_temperature_in_band<-10C,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #40. qc_flag_soil_temperature_grass
   row = 'type,40,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,40,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,40,Data Quality Flag: Grass Temperature,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,40,0,1,2,3,4,5,6,7' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,40,not_used,good_data,suspect_data:_soil_temperature>30C,suspect_data:_soil_temperatrue_in_band_20C_to_30C,suspect_data:_soil_temperature_in_band_0C_to_5C,suspect_data:_soil_temperature_in_band_-5C_to_0C,suspect_data:_soil_temperature_in_band<-10C,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #41. qc_flag_soil_temperature_bare_soil
   row = 'type,41,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,41,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,41,Data Quality Flag: Bare Soil Temperature,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,41,0,1,2,3,4,5,6,7' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,41,not_used,good_data,suspect_data:_soil_temperature>30C,suspect_data:_soil_temperatrue_in_band_20C_to_30C,suspect_data:_soil_temperature_in_band_0C_to_5C,suspect_data:_soil_temperature_in_band_-5C_to_0C,suspect_data:_soil_temperature_in_band<-10C,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #42. qc_flag_soil_temperature_10cm_below_grass_surface
   row = 'type,42,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,42,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,42,Data Quality Flag: Soil Temperature 10cm Below Grass Gurface,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,42,0,1,2,3,4,5,6,7' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,42,not_used,good_data,suspect_data:_soil_temperature>30C,suspect_data:_soil_temperatrue_in_band_20C_to_30C,suspect_data:_soil_temperature_in_band_0C_to_5C,suspect_data:_soil_temperature_in_band_-5C_to_0C,suspect_data:_soil_temperature_in_band<-10C,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #43. qc_flag_soil_moisture_10cm_below_grass_surface
   row = 'type,43,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,43,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,43,Data Quality Flag: Soil Moisture 10cm Below Grass Surface,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,43,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,43,not_used,good_data,suspect_data:_soil_moisture>200,good_data:_soil_moisture_in_band_0_to_10_soil_very_wet,good_data:_soil_moisture_in_band_100C_to_150_soil_very_dry,suspect_data:_soil_moisture<0,6b:bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #44. qc_flag_soil_moisture_20cm_below_grass_surface
   row = 'type,44,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,44,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,44,Data Quality Flag: Soil Moisture 20cm Below Grass Surface,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,44,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,44,not_used,good_data,suspect_data:_soil_moisture>200,good_data:_soil_moisture_in_band_0_to_10_soil_very_wet,good_data:_soil_moisture_in_band_100C_to_150_soil_very_dry,suspect_data:_soil_moisture<0,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #45. qc_flag_soil_moisture_30cm_below_grass_surface
   row = 'type,45,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,45,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,45,Data Quality Flag: Soil Moisture 30cm Below Grass Surface,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,45,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,45,not_used,good_data,suspect_data:_soil_moisture>200,good_data:_soil_moisture_in_band_0_to_10_soil_very_wet,good_data:_soil_moisture_in_band_100C_to_150_soil_very_dry,suspect_data:_soil_moisture<0,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #46. qc_flag_soil_moisture_50cm_below_grass_surface
   row = 'type,46,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,46,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,46,Data Quality Flag: Soil Moisture 50cm Below Grass Surface,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,46,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,46,not_used,good_data,suspect_data:_soil_moisture>200,good_data:_soil_moisture_in_band_0_to_10_soil_very_wet,good_data:_soil_moisture_in_band_100C_to_150_soil_very_dry,suspect_data:_soil_moisture<0,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #47. qc_flag_leaf_temperature_50cm
   row = 'type,47,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,47,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,47,Data Quality Flag: Leaf Temperature at 50cm,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,47,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,47,not_used,good_data,suspect_data:_leaf_temperature>30C,suspect_data:_leaf_temperatrue>40C,suspect_data:_leaf_temperature<-10C,suspect_data:_leaf_temperature<-20C,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #48. qc_flag_leaf_temperature_2m
   row = 'type,48,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,48,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,48,Data Quality Flag: Leaf Temperature at 2m,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,48,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,48,not_used,good_data,suspect_data:_leaf_temperature>30C,suspect_data:_leaf_temperatrue>40C,suspect_data:_leaf_temperature<-10C,suspect_data:_leaf_temperature<-20C,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #49. qc_flag_leaf_wetness_50cm
   row = 'type,49,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,49,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,49,Data Quality Flag: Leaf Wetness at 50cm,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,49,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,49,not_used,good_data,suspect_data:_leaf_wetness>15,good_data:_leaf_wetness_in_band_10_to_15,good_data:_leaf_wetness_in_band_0_to_5,suspect_data:_leaf_wetness<0,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))
   
   #50. qc_flag_leaf_wetness_2m
   row = 'type,50,int' + '\n'
   f.write("{}".format(row))
   row = 'dimension,50,time' + '\n'
   f.write("{}".format(row))
   row = 'long_name,50,Data Quality Flag: Leaf Wetness at 2m,1' + '\n'
   f.write("{}".format(row))
   row = 'flag_values,50,0,1,2,3,4,5,6' + '\n'
   f.write("{}".format(row))
   row = 'flag_meanings,50,not_used,good_data,suspect_data:_leaf_wetness>15,good_data:_leaf_wetness_in_band_10_to_15,good_data:_leaf_wetness_in_band_0_to_5,suspect_data:_leaf_wetness<0,bad_data:_missing_data' + '\n'
   f.write("{}".format(row))

def write_data(f, data):
   import numpy as np
   
   # start of data block indicator
   row = 'data' + '\n'
   f.write("{}".format(row))
   # column header
   row = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50' + '\n'
   f.write("{}".format(row))
   # data
   for n in range(len(data.ET)):
      row = (
            str(np.float64(data.ET[n]))   + ',' + str(np.float32(data.DoY[n]))  + ',' + 
            str(np.int32(data.DT[n,0]))   + ',' + str(np.int32(data.DT[n,1]))   + ',' +
            str(np.int32(data.DT[n,2]))   + ',' + str(np.int32(data.DT[n,3]))   + ',' + 
            str(np.int32(data.DT[n,4]))   + ',' + str(np.float32(data.DT[n,5])) + ',' +
            str(np.float32(data.lat))     + ',' + str(np.float32(data.lon))     + ',' + 
            str(np.float32(data.PP[n,0]))   + ',' + str(np.float32(data.TT[n,0]))   + ',' +
            str(np.float32(data.RH[n,0]))   + ',' +
            str(np.float32(data.WS[n,0]))   + ',' + str(np.float32(data.WD[n,0]))   + ',' + 
            str(np.float32(data.PA[n,0]))   + ',' + str(np.float32(data.PR[n,0]))   + ',' +
            str(np.float32(data.UV[n,0]))   + ',' + str(np.float32(data.SL[n,0]))   + ',' + 
            str(np.float32(data.ST[n,0])) + ',' + str(np.float32(data.ST[n,1])) + ',' + 
            str(np.float32(data.ST[n,2])) + ',' + str(np.float32(data.ST[n,3])) + ',' +
            str(np.float32(data.SM[n,0])) + ',' + str(np.float32(data.SM[n,1])) + ',' + 
            str(np.float32(data.SM[n,2])) + ',' + str(np.float32(data.SM[n,3])) + ',' +
            str(np.float32(data.LT[n,0])) + ',' + str(np.float32(data.LT[n,1])) + ',' +
            str(np.float32(data.LW[n,0])) + ',' + str(np.float32(data.LW[n,1])) + ',' +
            str(np.int8(data.qc_flag_temperature[n,0]))        + ',' + str(np.int8(data.qc_flag_relative_humidity[n,0]))   + ',' +
            str(np.int8(data.qc_flag_pressure[n,0]))           + ',' +
            str(np.int8(data.qc_flag_wind_speed[n,0]))         + ',' + str(np.int8(data.qc_flag_wind_from_direction[n,0])) + ',' +
            str(np.int8(data.qc_flag_radiation[n,0]))          + ',' + str(np.int8(data.qc_flag_precipitation[n,0]))       + ',' +
            str(np.int8(data.qc_flag_soil_temperature[n,0])) + ',' + str(np.int8(data.qc_flag_soil_temperature[n,1]))  + ',' +
            str(np.int8(data.qc_flag_soil_temperature[n,2])) + ',' + str(np.int8(data.qc_flag_soil_temperature[n,3]))  + ',' +
            str(np.int8(data.qc_flag_soil_moisture[n,0]))    + ',' + str(np.int8(data.qc_flag_soil_moisture[n,1]))     + ',' +
            str(np.int8(data.qc_flag_soil_moisture[n,2]))    + ',' + str(np.int8(data.qc_flag_soil_moisture[n,3]))     + ',' +
            str(np.int8(data.qc_flag_leaf_temperature[n,0])) + ',' + str(np.int8(data.qc_flag_leaf_temperature[n,1]))  + ',' +
            str(np.int8(data.qc_flag_leaf_wetness[n,0]))     + ',' + str(np.int8(data.qc_flag_leaf_wetness[n,1]))      + '\n'
            )    
      f.write("{}".format(row))
   # end of data block indicator
   row = 'end data'
   f.write("{}".format(row))
   
def write_csv(meta, data, fn):
   
   f = open(fn,'w')
   write_file_atts(meta, data.ET, f)
   write_var_atts(f, data)
   write_data(f, data)
   f.close()
      
   exit()   