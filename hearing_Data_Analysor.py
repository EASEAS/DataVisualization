# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:25:59 2018

@author: eriks
"""
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('C:/Users/ErikS/Downloads/Sensor_record_2018_3.csv')

sound_levels = list(data['SOUND LEVEL (dB)']  + 30) # addition is in dB for calibration purposes

hearing_budget = 460 # minutes of hearing budget left in the work day
hearing_budget_over_time = [0]*460

n = 86 # length of particular dataset

for x in range(n): 
   """
   if higher than threshold, subtract from hearing budget
   """ 
   if (sound_levels[x] < 85):                      
        exchange = (2**((sound_levels[x] - 85)/3))
        hearing_budget -= exchange
        
   if(hearing_budget < 60 and hearing_budget > 0):
        print("WARNING: Hearing Damage is going to occur")
   elif(hearing_budget < 0):
        print("WARNING: HEARING DAMAGE IS OCCURING")
        break
   if(sound_levels[x] > 140):
        print("WARNING: Impact sound(s) may have damaged hearing!")
        break
   hearing_budget_over_time[x] = hearing_budget
#hearing_budget_over_time[-1] = hearing_budget    
for x in range(n, 460):
    hearing_budget_over_time[x] = hearing_budget_over_time[x-1]






plt.plot(hearing_budget_over_time)
plt.ylabel('Hearing Budget')
plt.xlabel('Time')
plt.show()


plt.plot(sound_levels)
plt.ylabel('Sound Decibels')
plt.xlabel('Time')
plt.show()