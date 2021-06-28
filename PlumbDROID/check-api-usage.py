import sys, os, subprocess, operator, re

keywords = []

for line in open("xml/guideline.xml"):
  result = re.findall(r"<syscall[0-9]+>(.+)?</syscall[0-9]+>",line) 
  if len(result) > 0 and len(result[0]) > 0:
    api_string = result[0]
    idx = api_string.rfind(".")
    if idx == -1:
      api_string = ";->" + api_string
    else:
      api_string = api_string[:idx].replace(".", "/").replace("$", "\$") + ";->" + api_string[idx+1:]
    keywords.append(api_string)

app = sys.argv[1]

os.system("java -jar external_jars/apktool_2.0.0b9.jar -o decompiled/ -r -f d " + app + " > /dev/null")

score = 0

stringy = ""
for keyword in set(keywords):
  if len(stringy) > 0:
    stringy += "\|"
  stringy += keyword +"("

output = (subprocess.check_output("grep -inr \"" + stringy + "\" decompiled/smali", shell=True))

for line in output.split('\n'):
  print
  print line[10:]

#os.system("rm -rf decompiled")
