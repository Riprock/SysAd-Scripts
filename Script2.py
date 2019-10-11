import csv, os, random,re
def main():
    #file = input("What is the file name that you wish to parse and add?")
    with open("Lab02_Users.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if line_count == 7:
                    line_process(row, 1)
                else:
                    line_process(row, 0)
                line_count += 1

def line_process(row, offset):
    val_1 = 1 + offset
    val_2 = 2 + offset
    val_3 = 3 + offset
    val_5 = 5 + offset
    val_6 = 6 + offset
    end = random.randint(1,100)
    if(os.system("grep -q " + row[val_5] + " /etc/group")):
        os.system("groupadd -f " + row[val_5])
    if(row[val_5] == "security" or row[val_5] == "office"):
        shell = "bash"
    elif(row[val_5] == "ceo"):
        shell = "csh"
    firstname = row[val_2]
    lastname = row[val_1]
    re.sub(r'\W+', '', firstname)
    re.sub(r'\W+', '', lastname)
    username = firstname[0] + lastname + str(end)
    passwd = username[::-1]
    os.system("useradd -m -d /home/" + row[val_5] + "/" + username + " -s /bin/" + shell + " -g " + row[val_5] + " " + username)
    os.system("yes " + passwd  + " | passwd " + username)
    os.system("passwd -e " + username)



main()
