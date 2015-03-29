with open("/home/mathieu/jaus/definitions.txt", "r") as f:
    text = "".join(f.readlines())

text = text.replace(">", ">\n")
lines = text.split("\n")

to_delete = []
for i, l in enumerate(lines):
    if l.startswith("TRANSPORT"):
        to_delete.append(i)
    if "SAE" in l:
        print l

for i in to_delete:
    del lines[i]

print lines