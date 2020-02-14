import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import csv


# exponential function
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def func_linear(x, m, c):
    return m*x+c
p_init = [144.305, -0.0145658, 620.909]
slopesAverage = []

coeff_exp = pd.DataFrame({"a":[], "b":[], "c":[]})

for i in range(1,617):
    filename = str(i)+"_coeff_exp.csv"
    my_csv = pd.read_csv("coeffs/"+filename)
    coeffrow_exp = my_csv.iloc[0,:]
    coeff_exp.loc[len(coeff_exp)] = coeffrow_exp

coeff_exp.to_csv("MASTER_EXP.csv")


#
# for i in range(1,617):
#     filename = str(i)
#     slopesRow = []
#     plt.title(filename)
#     coeff_exp = pd.DataFrame({"a":[], "b":[], "c":[]})
#     coeff_lin = pd.DataFrame({"m":[], "c":[]})
#
#
#     my_csv = pd.read_csv(filename +".csv")
#
#     print(my_csv)
#
#     popt, pcov = curve_fit(func, my_csv.time, my_csv.displacement, maxfev=800, p0=p_init)
#     p_init = popt
#     # for expfit
#     coeffrow_exp = [popt[0], popt[1], popt[2]]
#     coeff_exp.loc[len(coeff_exp)] = coeffrow_exp
#
#     print(popt)
#     print(pcov)
#
#     # axs[n].plot(my_csv.time, my_csv.displacement, 'o', my_csv.time, yfit)
#
#     # second pass
#
#     displacement_linearized = np.log((my_csv.displacement - popt[2]))  # displacmeentln = ln(displacement-C)
#     print(my_csv.displacement)
#     linearizedData = my_csv
#     linearizedData["displacement_linearized"] = displacement_linearized
#
#     linearizedData = linearizedData[~np.isnan(linearizedData).any(axis=1)]
#     popt_linear, pcov_linear = curve_fit(func_linear, linearizedData.time, linearizedData.displacement_linearized,
#                                          maxfev=8000)
#
#     coeffrow_lin = [popt_linear[0], popt_linear[1]]
#
#     slopesRow.append(popt_linear[0])
#
#     coeff_lin.loc[len(coeff_lin)] = coeffrow_lin
#
#     yfit_linear = func_linear(linearizedData.time, *popt_linear)
#     yfit = func(my_csv.time, *popt)
#
#     # axs[n+1].plot(my_csv.time, my_csv.displacement, 'o', my_csv.time, yfit)
#     # axs[n+1].axhline(y=popt[2])
#     plt.axhline(y=np.log(popt[2]))
#
#     plt.plot(linearizedData.time, linearizedData.displacement_linearized, 'o', linearizedData.time, yfit_linear)
#     popt_sim = [-popt[1], np.log(popt[0])]
#     yfit_sim = func_linear(my_csv.time, *popt_sim)
#
#     coeff_exp.to_csv("coeffs/"+str(filename) + "_coeff_exp.csv")
#     coeff_lin.to_csv("coeffs/"+str(filename) + "_coeff_lin.csv")
#     slopesAverage.append(sum(slopesRow)/len(slopesRow))
#     plt.savefig("plots/"+filename+".png")
#     plt.clf()
# print(slopesAverage)
# #plt.plot(SA, slopesAverage)
# #plt.show()
