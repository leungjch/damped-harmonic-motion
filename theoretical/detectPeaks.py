import pandas as pd
import matplotlib.pyplot as plt
import csv

plt.style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (7,10)


for i in range(1,618):
    filename = str(i)
    print(filename)
    n = 0 # for subplots 

    plt.title(filename)

    my_csv = pd.read_csv("SAs/"+filename+".csv")
    my_csv.columns = ['time', 'displacement']
    time = my_csv[my_csv.columns[0]]        
    displacement = my_csv[my_csv.columns[1]]
    # detect peaks
    peaks = pd.DataFrame({"time":[], "displacement":[]}) 
        
    for i in range(2, len(displacement)-1):
        # detect a peak
        if (displacement[i-1] <= displacement[i]) and  (displacement[i+1] <= displacement[i]):
            row = [time[i], displacement[i]]
            peaks.loc[len(peaks)] = row
        # detect a valley
        #elif (displacement[i-1] >= displacement[i]) and  (displacement[i+1] >= displacement[i]):
        #    row = [time[i], displacement[i], -1]
        #    peaks.loc[len(peaks)] = row
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        #print(peaks)
    # axs[n].set_xlim([0, 100]) # set xlims
    plt.plot(time,displacement)
    plt.plot(peaks[peaks.columns[0]],peaks[peaks.columns[1]], 'g*')
    
    peaks.to_csv("peaks/"+filename+".csv")
    n+=1
    
    plt.savefig("plots/"+filename+".png")
    plt.clf()
