# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:18:37 2018
@author: 108700 / Jorge Paz
Install cds api in Windows: https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+Windows
Create filex with .extension : https://gist.github.com/ozh/4131243
Open netCDF pased on http://joehamman.com/2013/10/12/plotting-netCDF-data-with-Python/

Manage environments with the windows console:

# For Windows users# Note: <> denotes changes to be made

#Create a conda environment
conda create --name <environment-name> python=<version:2.7/3.5>

#To create a requirements.txt file:
conda list #Gives you list of packages used for the environment
conda list -e > requirements.txt #Save all the info about packages to your folder

in windows console you can see the content of requirements.txt this way:
more requirements.txt

This will not record the libraries instaled with pip

#To export environment file
activate <environment-name>
conda env export > <environment-name>.yml

#For other person to use the environment
conda env create -f <environment-name>.yml
"""

'''
####################################################
######## STEP 0: introduction to python ############
####################################################

### 1 ### Data structures ############################

## Diccionaries
diccionary01={"Alumno1":"Juan","Alumno2":"Ana"}
print(diccionary01["Alumno1"])
diccionaryOfDiccionaries={'Participant01': {'name': 'Jorge', 'surname': 'Paz'}, 
                          'Participant02': {'name': 'Nieves', 'surname': 'Pena'}}
print(diccionaryOfDiccionaries["Participant01"]['name'])

## Lists 
list01=["Juan","Ana","Pepe"]
print(list01[0])
print(list01[-1])

listOfLists=[[0,0,0,0,0,0],
             [0,0,0,7,0,0],
             [0,1,0,1,0,0]]
print(listOfLists[1][3])


##N-dimensional arrays ########################

import numpy as np
array01 = np.array([[0,0,0,1,1,1],[0,1,1,7,1,0],[0,1,5,1,1,1],[0,1,1,1,1,0],[0,0,1,0,0,0]])
array01 = np.array([[0,0,0,1,1,1],
                    [0,1,1,7,1,0],
                    [0,1,5,1,1,1],
                    [0,1,1,1,1,0],
                    [0,0,1,0,0,0]])

print(array01.dtype)
print(np.shape(array01))

print(array01[1][2:4])

print(array01[(1,2),(3,2)])

print(array01[(1,2),0:6])

print(array01[(1,2),:])

print(np.max(array01))

array3D_1=np.arange(0,18).reshape(2,3,3)
print(array3D_1)
array2D_2=np.arange(10,19).reshape(1,3,3)
print(array2D_2)
array3D_extended=np.concatenate((array3D_1, array2D_2), axis=0)
print(array3D_extended)

### 2 ### Basic structures ##########################

## Loops
for i in range(3):
    print(i)

for i in list01:
    print(i)

## Functions
def FuncionSumarRestar(paramentro1,parametro2,parametro3):
    resultado=paramentro1+parametro2-parametro3
    return (resultado)
print(FuncionSumarRestar(2,3,1))

'''

###############################################################################
######## PASO 1: read and plot a nc file ######################################
###############################################################################

### 1 ### import libreries ####################################################
from netCDF4 import Dataset
import numpy as np


### 2 ### import data from nc to numpy arrays #################################

ruta="C:/Users/..." #change this. include the route the the .nc file
file01 = Dataset(ruta+'era5Spain_201008.nc', mode='r')

print("----")
print("Dimensions:")
print(file01.dimensions)
print("----")
print(file01.dimensions['longitude'])

print("----")
print("Variables:")
print(file01.variables)
print("----")
print(file01.variables['tp'])
print("----")
print(file01.variables['time'])

lons1 = file01.variables['longitude'][:]
lats1 = file01.variables['latitude'][:]
precipt = file01.variables['tp'][:]
preciptUnits = file01.variables['tp'].units
temperat=file01.variables['t2m'][:]
temperatUnits = file01.variables['t2m'].units
presur=file01.variables['msl'][:]
presurUnits = file01.variables['msl'].units
times=file01.variables['time'][:]
timesUnits=file01.variables['time'].units
file01.close() #con esto cerramos el archivo para no dañarlo
print ("File closed. Everything imported in numpy arrays")


### 3 ### plot data ###########################################################

#valuesToPlot=np.mean(precipt,axis=0)
#valuesToPlot=temperat[24*15+12,:,:]-273.15
#valuesUnits=temperatUnits  
valuesToPlot=presur[24*15+12-1,:,:]/100
valuesUnits=presurUnits 

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
#import cartopy 

fig = plt.figure(figsize=(8, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
map=plt.contourf(lons1, lats1, valuesToPlot,60,
                 transform=ccrs.PlateCarree(),cmap='viridis')
ax.coastlines(resolution='10m',color='black')#'100
ax.gridlines(draw_labels=True,
             xlocs=list(range(-10,6,1)),ylocs=list(range(35,45,1)))
fig.colorbar(map,fraction=0.026, pad=0.09,label=valuesUnits)
plt.show()


