import subprocess as sub
import os
sub.run(["clear"])
proc1 = sub.Popen('pwd', stdout=sub.PIPE)
a = proc1.stdout.read()
b = a.decode("utf-8").strip()
numlinks = 0
file_array =[]
user = os.environ["USER"]
if(b != "/home/"+user):
    print("Not in Home Directory")
file_name =""
while(True):
    file_name = input("What file do you want to link?")
    if(file_name == "exit"):
        break
    os.symlink(file_name, "/home/"+ user +"/Desktop/" + file_name)
    numlinks += 1
    file_array.append(file_name)
print("Summary")
for i in file_array:
    print("File " + i + " Is linked")
print("The number of links are " + str(numlinks))
print("desktop Symlinks")
query = "^l"
ls1_process = sub.Popen(["ls", "-lhaF","/home/"+user+"/Desktop"], stdout=sub.PIPE)
grep1_process = sub.Popen(["grep", query], stdin=ls1_process.stdout, stdout=sub.PIPE)
ls1_process.stdout.close()
print(grep1_process.communicate()[0].decode("utf-8"))
print("Current Dir Symlinks")
query = "^l"
ls2_process = sub.Popen(["ls", "-lhaF"], stdout=sub.PIPE)
grep2_process = sub.Popen(["grep", query], stdin=ls2_process.stdout, stdout=sub.PIPE)
ls2_process.stdout.close()
print(grep2_process.communicate()[0].decode("utf-8"))
