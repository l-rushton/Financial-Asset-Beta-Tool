#************************************************************
#              //STOCK COMPARISON BETA CALCULATOR\\
#            //////////////\\\\\\\\\\\\\\\

import eel
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import numpy
import EXCELVARCOVAR as ex

eel.init("www")
eel.start("index.html")

@eel.expose
def main():
    #USER INPUTS 2 STOCKS TO COMPARE
    stonk1 = input("Enter ticker 1 symbol here: ")
    stonk2 = input("Enter ticker 2 symbol here: ")

    print("Ticker 1: " + stonk1 + " Ticker 2: " + stonk2)

    #USER INPUTS DATES 
    startYear = int(input("Enter start year of comparison (YYYY): "))

    #input checking NEED TO DO FOR ALL INPUTS
    #if (startYear < 1000 | startYear > 9999):
    #    print("Please enter a valid year to start")
        
    startMonth = int(input("Enter start month of comparison (MM): "))
    startDay = int(input("Enter start day of comparison (DD): "))

    startDate = datetime.datetime(startYear,startMonth,startDay)


    endYear = int(input("Enter end year of comparison (YYYY): "))

    endMonth = int(input("Enter end month of comparison (MM): "))

    endDay = int(input("Enter end day of comparison (DD): "))

    endDate = datetime.datetime(endYear,endMonth,endDay)

    #FETCH STOCK DATA
    stonk1Data = yf.download(stonk1,startDate,endDate)
    stonk2Data = yf.download(stonk2,startDate,endDate)

    #plot stonks
    stonk1Data['Adj Close'].plot()
    stonk2Data['Adj Close'].plot()

    #figure out variance by working out itemwise pct delta
    percentageChangeSeries1 = [0]
    percentageChangeSeries2 = [0]

    timeSeries1 = list(stonk1Data['Adj Close'])
    timeSeries2 = list(stonk2Data['Adj Close'])

    for i in range(len(timeSeries1)-1):
        percentageChangeSeries1.append(((timeSeries1[i+1]-timeSeries1[i])/timeSeries1[i])*100)
        percentageChangeSeries2.append(((timeSeries2[i+1]-timeSeries2[i])/timeSeries2[i])*100)
        

    #print(percentageChangeSeries1)
    #print(percentageChangeSeries2)

    var1 = ex.variance(percentageChangeSeries1)

    covariance = ex.covariance(percentageChangeSeries1,percentageChangeSeries2)

    print("COV = " + str(covariance))
    print("VAR1 = " + str(var1))

    beta = covariance/var1

    print("BETA = " + str(beta))

    plt.show()

    return Beta

main()
