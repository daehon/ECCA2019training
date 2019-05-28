#!/usr/bin/env python

#1# Define the working directory ##############################################
import os
print("Current Working Directory " , os.getcwd())
os.chdir("C:/Users/1...") #Include here the path to the folder where files will be downloaded

#2# Example of loop and functions #############################################

def AddAndDelete(a,b,c):
    return a+b-c

print(AddAndDelete(3,4,1))

for i in range (5):
    print(i)

for i in range (5):
    print(AddAndDelete(3,4,i))

#3# interesting part of the script ############################################
import cdsapi

c = cdsapi.Client()

years=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
months=['01','02','03','04','05','06','07','08','09','10','11','12']
days=['01','02','03','04','05','06','07','08','09','10','11','12',
      '13','14','15','16','17','18','19','20','21','22','23','24',
      '25','26','27','28','29','30','31']
times=['00:00','01:00','02:00','03:00','04:00','05:00','06:00',
       '07:00','08:00','09:00','10:00','11:00','12:00','13:00',
       '14:00','15:00','16:00','17:00','18:00','19:00','20:00',
       '21:00','22:00','23:00']

#data are stored in monthly tapes
#I create a function that recovers all the data that I need from a tape.

def DownloadBassicParamentersEra5SpainNc(year,month): 
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type':'reanalysis',
            'format':'netcdf',
            'variable':['10m_u_component_of_wind','10m_v_component_of_wind','2m_temperature',
                        'mean_sea_level_pressure','surface_pressure','total_precipitation'],
            'year':year,
            'month':month,
            'day':days,
            'time':times,
            'area': [35,-10,44,5],
        },
        'era5Spain_'+year+month+'.nc')

for y in years:
    for m in months:
        print('Downloading'+y+m+'---------------------------')
        DownloadBassicParamentersEra5SpainNc(y,m)



        
