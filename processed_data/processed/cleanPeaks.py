import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import style

plt.figure(figsize=(6.5, 4), dpi = 800)

import numpy as np
import csv
filenames_x = ["shortpend_0.00126_3_data.csv",'shortpend_0.01057_2_data.csv' , '0.10582_data (4).csv', '0.21164_data (4).csv', '0.31746_data (4).csv', '0.42328_data (4).csv', '0.5291_data (3).csv', '0.63491_data (4).csv']
filenames_small = ["shortpend_0.00126_1_data.csv", "shortpend_0.00126_2_data.csv", "shortpend_0.00126_3_data.csv"]
filenames_0 = ['0_data.csv', 'shortpend_01057_1_data.csv','shortpend_0.01057_2_data.csv']
filenames_1 = ['0.10582_data (1).csv', '0.10582_data (2).csv', '0.10582_data (3).csv', '0.10582_data (4).csv']
filenames_2 = ['0.21164_data (1).csv', '0.21164_data (2).csv', '0.21164_data (3).csv', '0.21164_data (4).csv']
filenames_3 = ['0.31746_data (1).csv', '0.31746_data (2).csv', '0.31746_data (3).csv', '0.31746_data (4).csv']
filenames_4 = ['0.42328_data (1).csv', '0.42328_data (2).csv', '0.42328_data (3).csv', '0.42328_data (4).csv']
filenames_5 = ['0.5291_data (1).csv', '0.5291_data (2).csv', '0.5291_data (3).csv'] #'0.5291_data (4).csv']
filenames_6 = ['0.63491_data (1).csv', '0.63491_data (2).csv', '0.63491_data (3).csv', '0.63491_data (4).csv']

SA = [0.00126, 0.0106, 0.107, 0.215, 0.326,0.430, 0.545, 0.653]

# averaged equilibrium values
equil_small = 16.82030769
equil_0 = 39.87033333
equil_1 = 35.86672199
equil_2 = 36.90771242
equil_3 = 36.90771242
equil_4 = 33.6508881
equil_5 = 34.02425
equil_6 = 34.00403

equil_new = [[16.79382472549817],
[16.79361870639260],
[16.84912603930461],
[36.85829254727475],
[39.87023201403782],
[39.22227684346701],
[35.02191691691691],
[35.17950064020487],
[35.24996497844827],
[35.22689245395128],
[34.88386816555953],
[34.81244685118331],
[35.05087699944843],
[35.05924914675768],
[32.92662324649299],
[32.95391719745223],
[33.02740149625935],
[32.43573770491804],
[34.00237238979118],
[34.27046736502819],
[34.2051747311828],
[34.21969040247678],
[34.00515584415584],
[34.05803365810452],
[34.01662739322533],
[33.715004048583],
[32.98521293800539],
[33.17085197524987],
[33.43988461538462],
[33.46377329192547]]

filesets = [filenames_small, filenames_0, filenames_1, filenames_2, filenames_3, filenames_4, filenames_5, filenames_6]
equils = [equil_small, equil_0, equil_1, equil_2, equil_3, equil_4, equil_5, equil_6]

marker_order = ["o","s","^","x"]
point_color = ["#287db7","#ff8922", "#6ebe6e", "#e47475"]


# exponential function
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def func_linear(x, m, c):
    return m*x+c
slopesAll = []
slopesAverage = []
minAverage = []
maxAverage = []
diffAverage = []
filesetnum = 0
num = 0
equilsNew_i = 0
for fileset in filesets:



    #fig, axs = plt.subplots(len(fileset))
    n = 0 # for subplots
    j = 1 # for label subplots
    coeff_exp = pd.DataFrame({"name":[], "a":[], "b":[], "c":[], "r2":[]})
    coeff_lin = pd.DataFrame({"name":[], "m":[], "c":[], "minslope":[], "maxslope":[], "diff":[], "r2":[]})
    slopesRow = []
    minRow = []
    maxRow = []
    diffRow = []
    for filename in fileset:

        #fig.suptitle(filename)

        my_csv = pd.read_csv(filename)


        my_csv = my_csv[my_csv['displacement'] > equil_new[equilsNew_i]] # filter peaks that are below the equilibrium point
        # make exception for 0.01057
        # if filename == 'shortpend_01057_1_data.csv':
        #     popt, pcov = curve_fit(func, my_csv.time, my_csv.displacement, maxfev =800, p0 = [25.8846, 0.00439018, 46.4443])
        # elif filename == 'shortpend_0.01057_2_data.csv':
        #     popt, pcov = curve_fit(func, my_csv.time, my_csv.displacement, maxfev =800, p0 = [25.8846, 0.00439018, 46.4443])
        # else:
        #     popt, pcov = curve_fit(func, my_csv.time, my_csv.displacement, maxfev =800)
        # yfit = func(my_csv.time, *popt)
        # coeffrow_exp = [filename, popt[0], popt[1], popt[2], r2]
        # coeff_exp.loc[len(coeff_exp)] = coeffrow_exp

        # for expfit
        # ss_res = np.sum((my_csv.displacement - yfit) ** 2)
        # ss_tot = np.sum((my_csv.displacement - np.mean(my_csv.displacement)) ** 2)
        # r2 = 1 - (ss_res / ss_tot)




        # axs[n].plot(my_csv.time, my_csv.displacement, 'o', my_csv.time, yfit)

        # second pass
        #my_csv = my_csv[my_csv['displacement'] > popt[2]] # filter peaks that are below the equilibrium point
        if fileset == filenames_0:
            my_csv = my_csv[my_csv['time'] < 60] # filter peaks beyond 20s
        else:
            my_csv = my_csv[my_csv['time'] < 15] # filter peaks beyond 20s

        displacement_linearized = np.log((my_csv.displacement-equil_new[equilsNew_i])) # displacmeentln = ln(displacement-C)
        linearizedData = my_csv
        linearizedData["displacement_linearized"] = displacement_linearized

        linearizedData = linearizedData[~np.isnan(linearizedData).any(axis=1)]
        popt_linear, pcov_linear = curve_fit(func_linear, linearizedData.time, linearizedData.displacement_linearized, maxfev =8000)
        linearizedData.max_or_min = [filename]*linearizedData.shape[0]
        linearizedData.to_csv("linearizedcsvs/"+ filename)


        yfit_linear = func_linear(linearizedData.time, *popt_linear)

        # axs[n+1].plot(my_csv.time, my_csv.displacement, 'o', my_csv.time, yfit)
        # axs[n+1].axhline(y=popt[2])
        linearizedData["uncertainty_displacement"] = 0.3


        #popt_sim = [-popt[1], np.log(popt[0])]
        #yfit_sim = func_linear(my_csv.time, *popt_sim)     # Plot exponential curve fit

        #plt.plot(linearizedData.time, yfit_sim)            # Plot exponential curve fit

        maxX = linearizedData.iloc[0]
        minX = linearizedData.iloc[-1]


        # myX = np.linspace(0, 15, 100)
        maxY = linearizedData.loc[linearizedData['displacement_linearized'].idxmax()]
        minY = linearizedData.loc[linearizedData['displacement_linearized'].idxmin()]


        # plot max min slopes
        plt.plot([maxX.time, minX.time], [maxY.displacement_linearized+maxY.uncertainty_displacement/maxY.displacement_linearized, minY.displacement_linearized-minY.uncertainty_displacement/minY.displacement_linearized], c=point_color[n], linestyle=":", marker='', label='_nolegend_')
        plt.plot([maxX.time, minX.time], [maxY.displacement_linearized-maxY.uncertainty_displacement/maxY.displacement_linearized, minY.displacement_linearized+minY.uncertainty_displacement/minY.displacement_linearized], c=point_color[n], linestyle=":", marker='', label='_nolegend_')

        maxSlope= ((minY.displacement_linearized+minY.uncertainty_displacement/minY.displacement_linearized)-(maxY.displacement_linearized-maxY.uncertainty_displacement/(maxY.displacement_linearized)))/((maxX.time+0.003)-(minX.time-0.003))
        minSlope= ((minY.displacement_linearized-minY.uncertainty_displacement/minY.displacement_linearized)-(maxY.displacement_linearized+maxY.uncertainty_displacement/(maxY.displacement_linearized)))/((maxX.time-0.003)-(minX.time+0.003))
        diff = (maxSlope - minSlope)/2
        # calculate R^2
        ss_res = np.sum((linearizedData.displacement_linearized - yfit_linear) ** 2)
        ss_tot = np.sum((linearizedData.displacement_linearized - np.mean(linearizedData.displacement_linearized)) ** 2)
        r2 = 1 - (ss_res / ss_tot)


        plt.plot(linearizedData.time, yfit_linear, c=point_color[n], label='') # Plot trendline
        plt.errorbar(linearizedData.time, linearizedData.displacement_linearized, yerr = linearizedData.uncertainty_displacement/linearizedData.displacement_linearized, xerr=[0.03]*linearizedData.shape[0] , marker=marker_order[n], linestyle='None', c=point_color[n], label="Trial "+str(j) + " ["+'y='+str(round(popt_linear[0],3))+"x+"+str(round(popt_linear[1],3))+" ($R^2$="+str(round(r2,3))+")"+"]")

        if fileset == filesets[7]:
            print(filename)
            print("Max", maxSlope)
            print("Min", minSlope)
            print("XMax", maxX.time)
            print("XMin", minX.time)
            print("YMin", minY.displacement_linearized)
            print("YMax", maxY.displacement_linearized)
            print("YMin_uncert", minY.uncertainty_displacement/minY.displacement_linearized)
            print("YMax_uncert", maxY.uncertainty_displacement/maxY.displacement_linearized)
            print("Diff", diff)
            print("Slope", popt_linear[0])

        coeffrow_lin = [filename, popt_linear[0], popt_linear[1], minSlope, maxSlope, diff, r2]
        slopesRow.append(popt_linear[0])
        maxRow.append(maxSlope)
        minRow.append(minSlope)
        diffRow.append(diff)
        coeff_lin.loc[len(coeff_lin)] = coeffrow_lin



        plt.title(filename)

        #axs[n].set_xlim([0, 100])
        #axs[n].plot(time,displacement)
        #axs[n].plot(peaks[peaks.columns[0]],peaks[peaks.columns[1]], 'g*')

        # #peaks.to_csv("peaks/"+filename)
        n+=1
        j+=1
        equilsNew_i += 1
    # coeff_exp.to_csv("coeffs/"+str(filename) + "_coeff_exp.csv")
    coeff_lin.to_csv("coeffs/"+str(filename) + "_coeff_lin.csv")
    print("sloepsrow" ,slopesRow)
    slopesAverage.append(np.average(slopesRow))
    slopesAll.append(slopesRow)

    maxAverage.append(sum(maxRow)/len(maxRow))
    minAverage.append(sum(minRow)/len(minRow))
    diffAverage.append(sum(diffRow)/len(diffRow))

    plt.xlabel('Time (s)')
    plt.ylabel('ln(x) from equilibrium (cm)')
    # plt.xlabel('Surface Area (m²)')
    # plt.ylabel('Damping Coefficient')
    # handles, labels = plt.gca().get_legend_handles_labels()
    # if len(fileset) == 3:
    #
    #     order = [3,0,4,1,5,2]
    # else:
    #     order = [4,0,5,1,6,2,7,3]

    # plt.legend([handles[idx] for idx in order], [labels[idx] for idx in order], loc="upper right", prop={'size': 8})
    plt.legend(loc="upper right", prop={'size': 7})
    plt.title("Linearized Peaks vs Time ("+str(SA[num])+"m²)")
    plt.show(block=False)
    num += 1

    print(SA[filesetnum])
    plt.savefig("plots/"+filename+".png")


    plt.clf()
print("slopes", slopesAverage)
print("sloeps7",slopesAverage[7])
print(slopesAll)
#plt.plot(SA, slopesAverage)
#plt.show()
from itertools import chain

filenames = list(chain.from_iterable(filesets))
combined_csv = pd.concat( [ pd.read_csv("linearizedcsvs/"+f) for f in filenames ] )
combined_csv.to_csv("BIGCSV_oct20.csv")

combined_csv_coeff = pd.concat( [ pd.read_csv("coeffs/"+g+"_coeff_lin.csv") for g in filenames_x ] )
combined_csv_coeff.to_csv("BIGCSV_coeff.csv")

final = pd.DataFrame()
final['SA']=SA
final['average_slope'] = slopesAverage
final['max_slope'] = maxAverage
final['min_slope'] = minAverage
final['diff'] = diffAverage
final.to_csv("average_linears.csv")
plt.savefig("allSlopes.png")

