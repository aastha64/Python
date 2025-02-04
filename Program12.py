# You have to input the IP address of a server - 145.89.23.70
# The output should show all the octate seperately

IpAdd = input("Enter the ip address: ").strip()
octets = IpAdd.split(".")
print("Octets are")
for x in octets:
    print("Octets are:", x)
