import pandas as pd
import matplotlib.pyplot as plt # type: ignore

mydata = pd.read_xlsx("E:\\Akgec\\AddItems.xlsx")
print(type(mydata))
print(mydata)
totalbill = sum(mydata["Bill"])
print("Total Billing = ", totalbill)


xaxis = mydata("Item Name")
yaxis = mydata("Bill")
plt.title = ()