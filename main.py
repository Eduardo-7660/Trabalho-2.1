import numpy as np
import matplotlib.pyplot as mat
import pandas as pd
import os
# dtypes manufacturer,cpuName,singleScore,multiScore,cores,threads,baseClock,turboClock,type
# data   AMD,Threadripper 3990X,1262,75671,64,128,2.9,4.5,Desktop

CPU = pd.read_csv("Processadores/CPU_r23_v2.csv")


#matplotlib
fig, axs = mat.subplots(figsize=(12, 4))

#############################
#############################
# Colunas Específicas  filtrada
#############################
#############################
filtroCPUXScore = CPU.filter(['manufacturer', 'cpuName', 'threads'])
filtroCPUXScore.to_csv('CPUxSCORE.csv',index=False)
mat.scatter(filtroCPUXScore['manufacturer'], filtroCPUXScore['threads'], c='k')
mat.xlabel("Manufacturer")
mat.ylabel("Threads")
mat.show()


#############################
#############################
# Colunas Específicas filtrada
#############################
#############################
filtroCarrosNomeAno = CPU.filter(['manufacturer', 'cpuName', 'type'])
filtroCarrosNomeAno.to_csv('CarroNomeAno.csv',index=False)
mat.scatter(filtroCarrosNomeAno['manufacturer'], filtroCarrosNomeAno['type'], c='k')
mat.xlabel("Manufacturer")
mat.ylabel("Type")
mat.show()



#############################
#############################
#operações de filtro;
#############################
#############################
TypeFiltroBaseClock = CPU[CPU['baseClock'] >= 2.8]
TypeBaseClock = TypeFiltroBaseClock[TypeFiltroBaseClock['manufacturer'].str.contains('AMD')]
gpa = TypeBaseClock.groupby('type')
gpa['type'].count().plot()

TypeBaseClock = TypeFiltroBaseClock[TypeFiltroBaseClock['manufacturer'].str.contains('Intel')]
gpa = TypeBaseClock.groupby('type')
gpa['type'].count().plot()

TypeBaseClock = TypeFiltroBaseClock[TypeFiltroBaseClock['manufacturer'].str.contains('Apple')]
gpa = TypeBaseClock.groupby('type')
gpa['type'].count().plot()
mat.legend(['AMD', 'Intel', 'Apple'])
mat.show()


TypeFiltroBaseClock.to_csv("BaseClockMaiorQueMedia.csv",index=False)
print(TypeFiltroBaseClock)



TypeFiltroIntel = CPU[CPU['manufacturer'] == "Intel"]

TypeIntel = TypeFiltroIntel[TypeFiltroIntel['manufacturer'].str.contains('Intel')]
gpa = TypeIntel.groupby('type')
gpa['type'].count().plot()
mat.legend(['Intel'])
mat.show()


TypeFiltroIntel.to_csv("FiltroIntel.csv",index=False)
print(TypeFiltroIntel)



#############################
#############################
#operações de groupby.
#############################
#############################


perThreads = CPU.groupby('threads')
perType = CPU.groupby('type')

for threads in (perThreads):
    print(threads)

for type in (perType):
    print(type)



QtdadeType = CPU[CPU['manufacturer'].str.contains('AMD')]
gpa = QtdadeType.groupby('type')
gpa['singleScore'].count().plot()

QtdadeType = CPU[CPU['manufacturer'].str.contains('Intel')]
gpa = QtdadeType.groupby('type')
gpa['singleScore'].count().plot()

QtdadeType = CPU[CPU['manufacturer'].str.contains('Apple')]
gpa = QtdadeType.groupby('type')
gpa['singleScore'].count().plot()

mat.legend(['AMD', 'Intel', 'Apple'])
mat.show()