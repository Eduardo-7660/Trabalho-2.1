import numpy as np
import matplotlib.pyplot as mat
import pandas as pd
import os
# dtypes manufacturer,cpuName,singleScore,multiScore,cores,threads,baseClock,turboClock,type
CPU = pd.read_csv("Carros/CPU_r23_v2.csv")
input("press enter")
print(CPU.dtypes)

filtroCPUXScore = CPU.filter(['manufacturer', 'cpuName', 'threads'])
filtroCarrosNomeAno = CPU.filter(['manufacturer', 'cpuName', 'type'])

print(filtroCPUXScore)
print(filtroCarrosNomeAno)

perName = CPU.groupby('cpuName')
perThread = CPU.groupby('threads')

print(perName)
print(perThread)