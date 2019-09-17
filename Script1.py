import os
def main():
	print("=============================")
	print("Running the test")
	print("=============================")
	gate = os.popen("ip r").read().split('\n')
	gate = gate[0].split()
	print("Your Default gateway is " + gate[2])
	pingtests(gate[2])
	print("=============================")
	print("Tests have concluded")
	print("=============================")
def pingtests(gateip):
	gateping = "ping -c 1 " + gateip + "> /dev/null"
	if (os.system(str(gateping)) == 0):
		print("Connection to default gateway is Sucessful")
	else:
		print("Connection to default gateway is Unsucessful")
	if(os.system("ping -c 1 8.8.8.8 > /dev/null") == 0):
		print("Remote Conneciton Complete")
	else:
		print("Remote connection failed")
	if(os.system("host google.com  > /dev/null") == 0):
		print("DNS resolution was sucsessful")
	else:
		print("Resolution was not sucessful")
main()
