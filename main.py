import numpy as np
import matplotlib.pyplot as mat
import pandas as pd
import os
# dtypes manufacturer,cpuName,singleScore,multiScore,cores,threads,baseClock,turboClock,type
CPU = pd.read_csv("Processadores/CPU_r23_v2.csv")
input("press enter")
print(CPU.dtypes)

filtroCPUXScore = CPU.filter(['manufacturer', 'cpuName', 'threads'])
filtroCarrosNomeAno = CPU.filter(['manufacturer', 'cpuName', 'type'])

print(filtroCPUXScore)
print(filtroCarrosNomeAno)

perThreads = CPU.groupby('threads')

for threads in (perThreads):
    print(threads)

perType = CPU.groupby('type')

for type in (perType):
    print(type)


