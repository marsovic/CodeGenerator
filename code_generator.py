import subprocess
from pathlib import Path

total = 2

f = open("gen/generated.py", "w+")

for i in range(0,total):
	f.write("f = open(\"gen/trash/generated%d.py\", \"w+\")\n" % (i+1))
	f.write("f.write(\"print(\\\"bien ou quoi %d\\\")\") \n\n" % (i+1))
	f.write("f.close()\n")

f.close()

exec(open("gen/generated.py").read())

f = open("gen/generated.sh", "w+")

pathToDir = str(Path.cwd()) + "/gen/trash"

for i in range(0,total):
	f.write("osascript -e \'tell app \"Terminal\" \n")
	f.write(" do script \" ")
	f.write("/usr/bin/python3 ")
	f.write(pathToDir + "/generated%d.py \n"  % (i+1))
	f.write(" \" \nend tell\' \n")

f.close()

subprocess.run(["sh gen/generated.sh"], shell=True)


