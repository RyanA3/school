inpt = "";
while(len(inpt) < 9):
    inpt = input("enter something");

for i in range(3):
    lineout = "";
    for j in range(3):
        lineout = lineout + inpt[i * 3 + j];
    print(lineout + "\n");
