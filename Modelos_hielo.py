#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:41:44 2023

@author: nico
"""
import math
import numpy as np
import matplotlib.pyplot as plt

#%% Funciones

# t es el tiempo
t  = np.arange(0, 100*60*60, 1) # calculo de 0 a 100 horas en pasos de 1 segundo

# #%% Elige el modelo a correr
# Imai    = 0 #Growth rate of glace from ICING AND SNOW ACCRETION. D.Kuroiwa -> no estoy seguro de sus unidades, no di con el paper original
# Goodwin = 1 # Goodwin et al. model 1983 -> revisado las unidades en paper 
# #

# def imai_model(V,T,t):
#     '''
#     Growth rate of glace from ICING AND SNOW ACCRETION. D.Kuroiwa
#     Parameters
#     ----------
#     V : float
#         Velocidad del viento.
#     T : float
#         Temperatura.
#     t : array of init 64
#         tiempo en segundos.

#     Returns
#     -------
#     R : Array of float64
#         Radio de la accreción de hielo.

#     '''
#     C1 = 2.3e-6
#     R = (C1*math.sqrt(V)*(-T)*t)**(2/3)
#     return R
    

#%% Un modelo mejor

def Goodwin_model(PP,V,Vd):
    # Goodwin et al. model 1983, assumes that all the drops collected freeze on the cable. In other words, the growth mode is dry. 
    # Goodwin et al. model is conceptually correct, good predictions at moderate conditions and fair predictions in extreme conditions. More in Makkonen, Lasse (1998) Modeling power line icing in freezing precipitation
    rho_w =  997 #kg/m3
    rho_i =  917 #kg/m3
    DR = ((rho_w*PP)/(np.pi*rho_i))*np.sqrt(1+(V/Vd)) # Unidades de mm
    return DR

def Calc_Vd(PP_intensidad):
    # Calculo radio promedio del tamaño de gota r_0 detalles en Sheng 2023, "Estimating and Mapping Extreme Ice Accretion Hazard and Load Due to Freezing Rain at Canadian Sites" 
    r_0 = 1.835/(4.1*PP_intensidad**(-0.21))# -> Marshall-Palmer drop size distribution (Atlas et al. 1973)
    print(f"El radio promedio de la distribución es de: {r_0} [mm]")
    if r_0 < 0.6:
        print("r_0 < 0.6")
        Vd = 8*r_0
    elif r_0 > 0.6 and r_0 < 2.0:
        print("r_0 > 0.6 and r_0 < 2.0")
        Vd = 201*(r_0/1000)**0.5
    print(f"El valor de la velocidad de caida de gota es Vd = {Vd} [m/s]") 
    return Vd, r_0    


caso ='Tololo 1'
V = 4 # viento m/s
PP_intensidad = 10 #mm
Vd, r_0 = Calc_Vd(PP_intensidad)
DR1 = Goodwin_model(PP_intensidad, V, Vd)
print(caso)
print(f"El espesor de hielo es de {round(DR1,1)} mm ")

caso ='Calama 1'
V = 4 # viento m/s
PP_intensidad = 5 #mm
Vd, r_0 = Calc_Vd(PP_intensidad)
DR1 = Goodwin_model(PP_intensidad, V, Vd)
print(caso)
print(f"El espesor de hielo es de {round(DR1,1)} mm ")

caso ='Calama 2'
V = 10 # viento m/s
PP_intensidad = 3 #mm
Vd, r_0 = Calc_Vd(PP_intensidad)
DR1 = Goodwin_model(PP_intensidad, V, Vd)
print(caso)
print(f"El espesor de hielo es de {round(DR1,1)} mm ")


caso ='10 mm'
V = 10/2 # viento m/s
PP_intensidad = 17.5 #mm
Vd, r_0 = Calc_Vd(PP_intensidad)
DR1 = Goodwin_model(PP_intensidad, V, Vd)
print(caso)
print(f"El espesor de hielo es de {round(DR1,1)} mm ")
