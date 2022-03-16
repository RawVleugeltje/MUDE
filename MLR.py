def MRL(sample, alpha): #MRL function
    import numpy as np
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    import seaborn as sns; sns.set(style = 'whitegrid')
    from scipy.stats import genpareto
    import pandas as pd
    import math as mt
    import scipy.special as sm
    #Defining the threshold array and its step
    step = np.quantile(sample, .995)/60
    threshold = np.arange(0, max(sample), step=step) 
    z_inverse = norm.ppf(1-(alpha/2))

    #Initialization of arrays
    mrl_array = [] #mean of excesses intialization
    CImrl = [] #confidence interval for the excesses initialization

    #First Loop for getting the mean residual life for each threshold value and the 
    #second one getting the confidence intervals for the plot
    for u in threshold:
        excess = [] #initialization of the excesses array for each loop
        for data in sample:
            if data > u:
                excess.append(data - u) #adding excesses to the excesses array
        mrl_array.append(np.mean(excess)) #adding the mean of the excesses in the mean excesses array
        std_loop = np.std(excess) #getting standard deviation in the loop
        CImrl.append(z_inverse*std_loop/(len(excess)**0.5)) #getting confidence interval 

    CI_Low = [] #initialization of the low confidence interval array
    CI_High = [] #initialization of the high confidence interval array

    #Loop to add in the confidence interval to the plot arrays
    for i in range(0, len(mrl_array)):
        CI_Low.append(mrl_array[i] - CImrl[i])
        CI_High.append(mrl_array[i] + CImrl[i])

    #Plot MRL
    plt.figure(1)
    sns.lineplot(x = threshold, y = mrl_array)
    plt.fill_between(threshold, CI_Low, CI_High, alpha = 0.4)
    plt.xlabel('u')
    plt.ylabel('Mean Excesses')
    plt.title('Mean Residual Life Plot')
    plt.show()
