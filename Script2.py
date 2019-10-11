import csv, os, random,re
def main():
    with open("Lab02_Users.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_process(row, line_count)
                line_count += 1
def line_process(row, lncnt):
    val_1 = 1
    val_2 = 2
    val_3 = 3
    val_5 = 5
    val_6 = 6
    end = random.randint(1,100)
    if(row[val_1] == "" or row[val_2] == "" or row[val_5] == "" ):
        print("The Line " + str(lncnt) + " is formatted incorrectly")
        return
    else:
        if(os.system("grep -q " + row[val_5] + " /etc/group")):
            os.system("groupadd -f " + row[val_5])
        if(row[val_5] == "security" or row[val_5] == "office"):
            shell = "bash"
        elif(row[val_5] == "ceo"):
            shell = "csh"
        firstname = row[val_2]
        lastname = row[val_1]
        regex = re.compile('[^a-zA-Z]')
        firstname = regex.sub('', firstname).lower()
        lastname = regex.sub('', lastname).lower()
        username = firstname[0] + lastname + str(end)
        passwd = username[::-1]
        os.system("useradd -m -d /home/" + row[val_5] + "/" + username + " -s /bin/" + shell + " -g " + row[val_5] + " " + username)
        os.system("echo " + passwd  + " | passwd --stdin " + username)
        os.system("passwd -e " + username)
main()         
