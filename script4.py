import re, geoip2.database, csv, os,sys
reader = geoip2.database.Reader("./GeoLite2-City.mmdb")
filename = input("What log file to open?")
if(os.path.isfile(filename)):
    print("Reading Log")
else:
    print("File does not exist")
    sys.exit(1)
pattern = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")#Regex for matching valid Ip addresses
iptonum ={}
with open(filename) as f:
    for ln in f:
        line = f.readline().strip().split()#Setup each line for matching
        for i in line:
            if(pattern.match(i)):#Check if ip addr
                if(i in iptonum):#check if exists in dict
                    iptonum[i] += 1
                else:
                    iptonum[i] = 1
with open('IPlog.csv', 'w', newline='') as file:#Create CSV file
    writer = csv.writer(file)#create writer
    writer.writerow(["Number of Ocurrences", "IP Address", "Country"])#header
    for key in iptonum:
        response = reader.city(key)
        writer.writerow([str(iptonum[key]), str(key), str(response.country.name)])#Writes each row
        if(iptonum[key] >= 10): # ONly display 10 or above occurnces
            print(str(iptonum[key]) + "," + str(key) +"," + str(response.country.name))

