import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import csv


# exponential function
def func(x, a, b, c):
    return a * np.exp(-b * x) + c


for i in range(1,2):
    filename = "peaks/"+str(i)+".csv"

    my_csv = pd.read_csv(filename)

    print(my_csv)
    
    popt, pcov = curve_fit(func, my_csv.time, my_csv.displacement, maxfev=8000, p0=(390.538,-0.172436, 550.77))
    print(popt)
    print(pcov)
    yfit = func(my_csv.time, *popt)
    plt.plot(my_csv.time, my_csv.displacement, 'o', my_csv.time, yfit)
    plt.title(str(i))
    plt.savefig("fitplots/"+str(i)+".png")
    plt.clf()

    #axs[n].set_xlim([0, 100])
    #axs[n].plot(time,displacement)
    #axs[n].plot(peaks[peaks.columns[0]],peaks[peaks.columns[1]], 'g*')
    
    #peaks.to_csv("peaks/"+filename)
    
    plt.show(block=False)
    #plt.savefig("plots/"+filename+".png")
