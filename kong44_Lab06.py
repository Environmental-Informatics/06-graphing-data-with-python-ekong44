#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 01:13:01 2020
@author: kong44

Program description: 
This program accepts text files and generates summary figures of the data. 
Text files have been provided by the instructor, it is data from bodies of water. 
"""

# importing modules
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams

# part 3 of the assignment, command line prompt to determine input file 
prompt = input("\t>Type '1' for Tippecanoe data.\n\t>Type '2' for Wildcat data." +
               "\n\t>Type '3' if you want to manually enter the input file name." +
               "\n\t>Enter your numeric response here: ")
prompt = int(prompt)

if prompt == 1:
    input_data = "Tippecanoe_River_at_Ora.Annual_Metrics.txt"
    
elif prompt == 2:
    input_data = "Wildcat_Creek_at_Lafayette.Annual_Metrics.txt"
    
elif prompt == 3 :
    print('\nPlease enter the file name, including the extension.')
    print('This will only work if the file is within the directory!')
    input_data = input('>')
    
else:
    print("\nSorry, there are only three available options. Please try again.")
    
# using genfromtxt to open file and generate arrays with corresponding header name
data2plot = np.genfromtxt(input_data, skip_header=1) # skip header so the first line is not read

# subplot 1
plt.subplot(311)
plt.plot(data2plot[:,0], data2plot[:,1], 'k', label='Mean')
plt.plot(data2plot[:,0], data2plot[:,2], 'r', label='Max')
plt.plot(data2plot[:,0], data2plot[:,3], 'b', label='Min')
# axis labels
plt.xlabel('Year')
plt.ylabel('Streamflow (cfs)') # Stated in README
# Place a legend above this subplot
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3), shadow=True, ncol=3)

# subplot 2
plt.subplot(312)
plt.plot(data2plot[:,0], data2plot[:,5]*100, 'bo')
# axis labels
plt.xlabel('Year')
plt.ylabel('Tqmean (%)') # Stated in README

# subplot 3
plt.subplot(313)
plt.bar(data2plot[:,0], data2plot[:,6])
# axis labels
plt.xlabel('Year')
plt.ylabel('R-B Index (ratio)') # Stated in README

rcParams['figure.figsize'] = 8.5, 11 # figure size in inches (width, height)

# saving plot as PDF file
print("\nWhat would you like the output file name to be?")
output_name = input(">")
plt.savefig(output_name + ".pdf")