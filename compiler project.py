from tabulate import tabulate  # pip3 install tabulate

file=open('code_input_file.txt',encoding="utf-8")
f=file.readlines()
newlist=[]
for line in f:
    if line[-1] == '\n':
        newlist.append(line[:-1])
    else:
        newlist.append(line)
s=newlist

bracket = ['(', ')', '{', '}', '[', ']']

digt=["0","1","2","3","4","5","6","7","8","9"]

keyw = ['printf','abort', 'abs', 'ceil', 'exit', 'exp', 'floor', 'scanf', 'sqrt', 'strcasecmp',
                'strcmp', 'strcpy', 'auto', 'double', 'int',	'struct', 'break', 'else', 'long',	'switch',
              'case', 'enum',	'register', 'typedef', 'char', 'extern', 'return', 'union', 'continue',
              'for', 'signed',	'void', 'do', 'static', 'while', 'default', 'goto', 'sizeof',
              'volatile', 'const', 'float', 'short', 'unsigned',]

opet = ['+', '-', '*', '/', '%', '++', '--', '+=', '-=', '*=', '!=', '%=', '=', '==', '>', '<', '>=', '<=',
        '!=', '&&', '!', '<<', '<<', '^', '~', '&', '|']



tbl=[]
li=0
idd=0
op=0
other=0
num=0
semi=0
iff=0

for i in range(0,len(s)):

    while (s[i] != ''):
        s[i] = s[i].lstrip()
        #Keyword cheak
        for j in range(0, len(keyw)):
            r=len(keyw[j])
            n=s[i][0:r]
            if(n == keyw[j]):
                idd= idd+1
                y="id"
                z= y + str(idd)
                s[i]=s[i].replace(s[i][0:r],'')
                s[i]=s[i].lstrip()
                tbl.append([keyw[j],z,"id", "-", i + 1])

        #Operator cheak
        for j in range(0, len(opet)):
            r=len(opet[j])
            n=s[i][0:r]
            if(n == opet[j]):
                op= op+1
                y="op_"
                z= y + str(idd)
                s[i]=s[i].replace(s[i][0:r],'')
                s[i]=s[i].lstrip()
                tbl.append([opet[j],z,opet[j], "-", i + 1])

        #Bracket cheak
        for j in range(0, len(bracket)):
            r=len(bracket[j])
            n=s[i][0:r]
            if(n == bracket[j]):
                other= other+1
                y="other_"
                z= y + str(other)
                s[i]=s[i].replace(s[i][0:r],'')
                s[i]=s[i].lstrip()
                tbl.append([bracket[j],z,"other", "-", i + 1])

        #Digit cheak
        for j in range(0, len(digt)):
            if (s[i][0:1]==digt[j]):
                w=0
                for p in range(0, len(s[i])):
                    for b in range(0, len(digt)):
                        if (s[i][p] == digt[b]):
                            w = w + 1
                val = (s[i][0:w])
                r = len(val)
                num = num + 1
                y = "num_"
                z = y + str(num)
                tbl.append([val, z, "number", val, i + 1])
                s[i] = s[i].replace(s[i][0:r], '')
                s[i] = s[i].lstrip()
        #semiclone cheak
        if (s[i][0:1]==';'):
            semi = semi + 1
            y = "Semicolon_"
            z = y + str(semi)
            tbl.append([";", z, "Semicolon", "-", i + 1])
            s[i] = s[i].replace(";", "")
            s[i] = s[i].lstrip()

        #if cheak
        elif (s[i][0:2]=='if'):
            iff = iff + 1
            y = "if_"
            z = y + str(iff)
            tbl.append(["if", z, "if", "-", i + 1])
            s[i] = s[i].replace("if", "")
            s[i] = s[i].lstrip()

        #literal cheak
        elif (s[i][0:1] == '"'):
            count = 0
            for j in range(0, len(s[i])):
                count = count + 1
                if (s[i][j + 1] == '"'):
                    break
            liter = s[i][1:count]
            s[i] = s[i].replace(s[i][0:count + 1], '')
            s[i] = s[i].lstrip()
            liter = liter.split(" ")
            for l in range(0, len(liter)):
                li = li + 1
                y = "literal_"
                z = y + str(li)
                tbl.append([liter[l], z, "literal", "-", i + 1])
        else:
            count = 0
            for j in range(0, len(s[i])-1):
                count = count + 1
                if ((s[i][j + 1]) == " ") or ((s[i][j + 1]) == "=") or ((s[i][j + 1]) == ";") or \
                        ((s[i][j + 1]) == "+") or ((s[i][j + 1]) == "-") or ((s[i][j + 1]) == "*") or \
                        ((s[i][j + 1]) == "/") or ((s[i][j + 1]) == "%") or ((s[i][j + 1]) == ">") or \
                        ((s[i][j + 1]) == "<") or ((s[i][j + 1]) == ")") or ((s[i][j + 1]) == "("):
                    break
            iden = s[i][0:count]
            iden = iden.rstrip()
            s[i] = s[i].replace(s[i][0:count], '')
            s[i] = s[i].lstrip()
            flag=0
            for itm in range(0,len(tbl)):
                if tbl[itm][0]==iden:
                    flag=1

            if (iden.isidentifier() == True):
                if flag==0:
                    idd = idd + 1
                    y = "id"
                    z = y + str(idd)
                    tbl.append([iden, z, "id", "-", i + 1])




print(tabulate(tbl, headers=["Symble", "Symble_Id", "Token_Type","Value","Line Number"],tablefmt="grid"))