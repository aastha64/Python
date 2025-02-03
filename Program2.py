# program to write temperature conversion  from centigrade to fahrenheit
centigrade = float(input("Enter celsius value : " ))
fahrenheit = (centigrade/5)*9 + 32

print("Celsius Temp = {:.2f} \nFahrenheit Temp = {:.2f}".format(centigrade, fahrenheit))# here we define to print the answer in 2 digits after decimal


print("Celsius Temp = %.2f\nFahrenheit Temp = %.2f" %(centigrade, fahrenheit))# here we define to print the answer in 6 digits after decimal
