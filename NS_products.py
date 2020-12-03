def create_NC_file(nm, dp, ver, opt1, opt2, opt3, start_date, logfile):
   from netCDF4 import Dataset
   from datetime import datetime
   
   try:
      # create nc file
      from netCDF4 import Dataset
      dout = 'Data\\'
      f1 = nm # instrument name
      f2 = 'ness-gardens'
      if nm == 'ness-hand-obs':
         f3 = datetime.fromtimestamp(int(start_date)).strftime('%Y%m') # monthly files 
      else:
         f3 = datetime.fromtimestamp(int(start_date)).strftime('%Y%m%d') # daily files
      f4 = dp # data product
      f5 = 'v' + ver # version number
      f6 = '.nc'
      
      if ((len(opt1)<1) and (len(opt2)<1) and (len(opt3)<1)):
         fn = dout+f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+f5+f6         
      if ((len(opt1)>1) and (len(opt2)<1) and (len(opt3)<1)):
         fn = dout+f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+f5+f6
      if ((len(opt1)>1) and (len(opt2)>1) and (len(opt3)<1)):
         fn = dout+f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+opt2+chr(95)+f5+f6
      if ((len(opt1)>1) and (len(opt2)>1) and (len(opt3)>1)):
         fn = dout+f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+opt2+chr(95)+opt3+chr(95)+f5+f6
      
      nc = Dataset(fn, "w",  format = "NETCDF4_CLASSIC") 
   except:
      # exit if problem encountered
      print('Unable to create: ',fn,'. This program will terminate')
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat()+' Unable to create: '+fn+'. This program will terminate\n')
      g.close()
      exit()
      
      del Dataset, datetime

   return nc

def surface_met(meta, data, nc):
   import NS_common as com
   import numpy as np
   
   # write common global attrib 
   com.global_attributes(nc, meta, data.ET)
      
   # write common dimensions
   com.dimensions(nc, data.ET)
   
   # write common variables
   com.variables(nc, data) 
   
   # write specific variables
   v = nc.createVariable('air_pressure', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'hPa'
   v.standard_name = 'air_pressure'
   v.long_name = 'Air Pressure'
   v.valid_min = np.float32(data.PP_min)
   v.valid_max = np.float32(data.PP_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.PP) 
   
   v = nc.createVariable('air_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'air_temperature'
   v.long_name = 'Air Temperature'
   v.valid_min = np.float32(data.TT_min)
   v.valid_max = np.float32(data.TT_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.TT)
   
   v = nc.createVariable('relative_humidity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '%'
   v.standard_name = 'relative_humidity'
   v.long_name = 'Relative Humidity'
   v.valid_min = np.float32(data.RH_min)
   v.valid_max = np.float32(data.RH_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.RH)
   
   v = nc.createVariable('wind_speed', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'wind_speed'
   v.long_name = 'Wind Speed'
   v.valid_min = np.float32(data.WS_min)
   v.valid_max = np.float32(data.WS_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.WS)
   
   v = nc.createVariable('wind_from_direction', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.standard_name = 'wind_from_direction'
   v.long_name = 'Wind From Direction'
   v.valid_min = np.float32(data.WD_min)
   v.valid_max = np.float32(data.WD_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.WD)
   
   v = nc.createVariable('thickness_of_rainfall_amount', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm'
   v.standard_name = 'thickness_of_rainfall_amount'
   v.long_name = 'Rain Accumulated in Averaging Period'
   v.valid_min = np.float32(data.PA_min)
   v.valid_max = np.float32(data.PA_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.PA)
   
   v = nc.createVariable('rainfall_rate', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm hr-1'
   v.standard_name = 'rainfall_rate'
   v.long_name = 'Rainfall Rate'
   v.valid_min = np.float32(data.PR_min)
   v.valid_max = np.float32(data.PR_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.PR)
   
   v = nc.createVariable('downwelling_cie_weighted_uv_flux_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.long_name = 'Downwelling CIE Weighted UV Radiative Flux'
   v.valid_min = np.float32(data.UV_min)
   v.valid_max = np.float32(data.UV_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.UV)
   
   v = nc.createVariable('downwelling_total_irradiance', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.long_name = 'Downwelling Total Radiative Flux'
   v.valid_min = np.float32(data.SL_min)
   v.valid_max = np.float32(data.SL_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data.SL)
   
   v = nc.createVariable('soil_temperature', np.float32, ('time','s_index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'soil_temperature'
   v.long_name = 'Soil Temperature'
   v.valid_min = np.float32(data.ST_min)
   v.valid_max = np.float32(data.ST_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data.ST)
   
   v = nc.createVariable('soil_moisture', np.float32, ('time','s_index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'cbar'
   v.long_name = 'Soil Moisture'
   v.valid_min = np.float32(data.SM_min)
   v.valid_max = np.float32(data.SM_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data.SM)
   
   v = nc.createVariable('leaf_temperature', np.float32, ('time','l_index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Soil Moisture'
   v.valid_min = np.float32(data.LT_min)
   v.valid_max = np.float32(data.LT_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data.LT)
   
   v = nc.createVariable('leaf_wetness', np.float32, ('time','l_index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Soil Wetness'
   v.valid_min = np.float32(data.LW_min)
   v.valid_max = np.float32(data.LW_max)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data.LW)
   
   v = nc.createVariable('qc_flag_temperature', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Temperature'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:suspect_data:_air_temperature>30C' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:suspect_data:_air_temperatrue>40C' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:suspect_data:_air_temperature<-10C' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:suspect_data:_air_temperature<-20C' + '\n'
   v.flag_meanings = v.flag_meanings + '6b:bad_data:_missing_data' 
   #write data
   v[:] = np.int8(data.qc_flag_temperature)  
   
   v = nc.createVariable('qc_flag_relative_humidity', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Relative Humidity'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:bad_data:_relative_humidity>100%' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:suspect_data:_relative_himidity=100%' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:suspect_data:_relative_himidity<40%' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:bad_data:_relative_himidity<0%' + '\n'
   v.flag_meanings = v.flag_meanings + '6b:bad_data:_missing_data' 
   #write data
   v[:] = np.int8(data.qc_flag_relative_humidity)
   
   v = nc.createVariable('qc_flag_pressure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Pressure'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:good_data:_pressure>1050hPa' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:suspect_data:_pressure=1100hPa' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:suspect_data:_pressure<950hPa' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:bad_data:_pressure<540hPa' + '\n'
   v.flag_meanings = v.flag_meanings + '6b:bad_data:_missing_data'
   #write data
   v[:] = np.int8(data.qc_flag_pressure)
   
   v = nc.createVariable('qc_flag_wind_speed', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Wind Speed'
   v.flag_values = '0b,1b,2b,3b,4b,5b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:suspect_data:_wind_speed>30ms-1' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:suspect_data:_wind_speed=0ms-1' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:bad_data:_wind_speed<0ms-1' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:bad_data:_missing_data' 
   #write data
   v[:] = np.int8(data.qc_flag_wind_speed)
   
   v = nc.createVariable('qc_flag_wind_from_direction', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Wind From Direction'
   v.flag_values = '0b,1b,2b,3b,4b,5b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:bad_data:_wind_direction>360degrees' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:bad_data:_wind_direction<0degrees' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:suspect_data:_wind_speed=0ms-1' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:bad_data:_missing_data' 
   #write data
   v[:] = np.int8(data.qc_flag_wind_from_direction)
   
   v = nc.createVariable('qc_flag_radiation', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Radiation'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b,7b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:suspect_data:UV>1800Wm-2' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:bad_data:UV<0Wm-2' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:bad_data:UV_missing_data' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:suspect_data:_total_irradiance(Solar)>1800ms-1' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:bad_data:_total_irradiance(Solar)<0ms-1' + '\n'
   v.flag_meanings = v.flag_meanings + '7b:bad_data:_total_irradiance_missing_data' 
   #write data
   v[:] = np.int8(data.qc_flag_radiation)
   
   v = nc.createVariable('qc_flag_precipitation', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Precipitation'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b,7b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:suspect_data:_accumulated_rain>25mm' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:bad_data:_accumulated_rain<0mm' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:bad_data:_accumulated_rain_missing_data' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:suspect_data:_rainfall_rate>300mmhr-1' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:bad_data:_rainfall_rate<0mmhr-1' + '\n'
   v.flag_meanings = v.flag_meanings + '7b:bad_data:_rainfall_rate_missing_data'  
   #write data
   v[:] = np.int8(data.qc_flag_precipitation)
   
   v = nc.createVariable('qc_flag_soil_temperature', np.int8, ('time', 's_index',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Soil Temperature'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b,7b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:suspect_data:_soil_temperature>30C' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:suspect_data:_soil_temperatrue_in_band_20C_to_30C' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:suspect_data:_soil_temperature_in_band_0C_to_5C' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:suspect_data:_soil_temperature_in_band_-5C_to_0C' + '\n'
   v.flag_meanings = v.flag_meanings + '6b:suspect_data:_soil_temperature_in_band<-10C' + '\n'
   v.flag_meanings = v.flag_meanings + '7b:bad_data:_missing_data' 
   #write data
   v[:,:] = np.int8(data.qc_flag_soil_temperature)
   
   v = nc.createVariable('qc_flag_soil_moisture', np.int8, ('time', 's_index',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Soil Moisture'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:suspect_data:_soil_moisture>200' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:good_data:_soil_moisture_in_band_0_to_10_soil_very_wet' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:good_data:_soil_moisture_in_band_100C_to_150_soil_very_dry' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:suspect_data:_soil_moisture<0' + '\n'
   v.flag_meanings = v.flag_meanings + '6b:bad_data:_missing_data' 
   #write data
   v[:,:] = np.int8(data.qc_flag_soil_moisture)
   
   v = nc.createVariable('qc_flag_leaf_temperature', np.int8, ('time', 'l_index',))
   #variable attribute
   v.units = 'K'
   v.long_name = 'Data Quality Flag: Leaf Temperature'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:suspect_data:_leaf_temperature>30C' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:suspect_data:_leaf_temperatrue>40C' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:suspect_data:_leaf_temperature<-10C' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:suspect_data:_leaf_temperature<-20C' + '\n'
   v.flag_meanings = v.flag_meanings + '6b:bad_data:_missing_data' 
   #write data
   v[:,:] = np.int8(data.qc_flag_leaf_temperature) 
   
   v = nc.createVariable('qc_flag_leaf_wetness', np.int8, ('time', 'l_index',))
   #variable attribute
   v.units = 'K'
   v.long_name = 'Data Quality Flag: Leaf Wetness'
   v.flag_values = '0b,1b,2b,3b,4b,5b,6b'
   v.flag_meanings = '0b:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1b:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2b:suspect_data:_leaf_wetness>15' + '\n'
   v.flag_meanings = v.flag_meanings + '3b:good_data:_leaf_wetness_in_band_10_to_15' + '\n'
   v.flag_meanings = v.flag_meanings + '4b:good_data:_leaf_wetness_in_band_0_to_5' + '\n'
   v.flag_meanings = v.flag_meanings + '5b:suspect_data:_leaf_wetness<0' + '\n'
   v.flag_meanings = v.flag_meanings + '6b:bad_data:_missing_data' 
   #write data
   v[:,:] = np.int8(data.qc_flag_leaf_wetness)