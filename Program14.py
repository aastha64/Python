import numpy as np # type: ignore

#Numeric List

priceList = [210,45,69,84,90,51,26]
maxprice = np.max(priceList)
minprice = np.min(priceList)
avgprice = np.mean(priceList)
print("Max price is: ", maxprice)
print("Min price is: ", minprice)
print("Average price is: ", avgprice)

