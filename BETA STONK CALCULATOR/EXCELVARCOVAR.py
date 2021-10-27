#EXCEL VARIANCE AND COVARIANCE CALCULATOR

def variance(timeSeries):
    mean = 0
    sum = 0
    
    for i in range(len(timeSeries)):
        mean += timeSeries[i]
    
    mean = mean/len(timeSeries)
    
    for i in range(len(timeSeries)):
        sum += (timeSeries[i] - mean)*(timeSeries[i] - mean)

    return sum/(len(timeSeries) - 1)

def covariance(timeSeries1, timeSeries2):
    mean1 = 0
    mean2 = 0
    sum = 0
    
    for i in range(len(timeSeries1)):
        mean1 += timeSeries1[i]
        mean2 += timeSeries2[i]
        
    mean1 = mean1/len(timeSeries1)
    mean2 = mean2/len(timeSeries2)
    
    for i in range(len(timeSeries1)):
        sum += (timeSeries1[i]-mean1)*(timeSeries2[i]-mean2)
        
    return sum/(len(timeSeries1) - 1)
