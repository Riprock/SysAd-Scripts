import re
import geoip2.database
reader = geoip2.database.Reader("./GeoLite2-City.mmdb")
filename = input("What log file to open?")
pattern = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
iptonum ={}
with open(filename) as f:
    for ln in f:
        line = f.readline().strip().split()
        for i in line:
            if(pattern.match(i)):
                if(i in iptonum):
                    iptonum[i] += 1
                else:
                    iptonum[i] = 1
for key in iptonum:
    response = reader.city(key)
    print(str(iptonum[key]) + "," + str(key) +"," + str(response.country.name))