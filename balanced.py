#The first part of this project reads the command line argument and opens the file.

#loading the file into lines, and then using the enumerate command to parse through each char in 
#each line from the file into multi. it tests for qutations, and look for single line comments. then laoding the
#lines without single line comments into new_lines

#then it tests for double line comments in a similiar fashion, dealing with qutations, using clrd_multi.
#these lines get loaded to final file, which has the file ready to ship

#then we create and write to the file.

#finally, using the list, we pop and append all brackets and braces to make sure they are lines up correctly
#and give a helpful on screen notice on whether the files brackets do or do not line up
import sys
search = sys.argv[1]
with open(search,'r') as file:
    lines = []
    while True:
        each_line = file.readline()
        if not each_line: 
            break
        lines.append(each_line)
    file.close()
each_line = ''
flag = True
quote = True
new_lines = []
new_line = ''
multi = []
for i in lines:
    for j, c in enumerate(i):
       multi.append(c)
    for p in range(len(multi)):
        if(multi[p] is '"' and quote == False):
            quote = True
        if(multi[p] is '"'):
            quote = False
        if(multi[p] is '/' and multi[p+1] is '/' and flag == True and quote == True):
            m = p
            flag = False
        if(flag == True):
            new_line = new_line + multi[p]
    new_lines.append(new_line)
    new_line = ''
    flag = True
    quote = True
    multi.clear()
clr_multi = []
clrd_string = ''
final_file = []
flag = True
for i in new_lines:
    for j, c in enumerate(i):
        clr_multi.append(c)
    for p in range(len(clr_multi)):
        if(clr_multi[p] is '"' and quote == False):
            quote = True
        if(clr_multi[p] is '"'):
            quote = False
        if(clr_multi[p] is '/' and clr_multi[p+1] is '*' and flag == True and quote == True):
            flag = False
        if(flag == False and clr_multi[p-1] is '/' and clr_multi[p-2] is '*' and quote == True):
            flag = True
        if(flag == True):
            clrd_string = clrd_string + clr_multi[p]
    final_file.append(clrd_string)
    clrd_string = ''
    quote = True
    clr_multi.clear()
for i in range(len(search)):
    if(search[i] is '.'):
        m = i
search = search[:m] + '.nocom' + search[m:]
f = open(search,"w+")
for i in final_file:
    f.write(i)
f.close()
brackets = []
flag = True
for u in final_file:
    for j in u:
        if (j is "{"):
            brackets.append(j)
        if (j is "["):
            brackets.append(j)
        if (j is "("):
            brackets.append(j)
        try:
            if (j is "}"):
                if(brackets[-1] is not '{'):
                    flag = False
                else:
                    brackets.pop(-1)
            if (j is ")"):
                if(brackets[-1] is not '('):
                    flag = False
                else:
                    brackets.pop(-1)
            if (j is "]"):
                if(brackets[-1] is not '['):
                    flag = False
                else:
                    brackets.pop(-1)
        except:
            flag = False
if (flag == True):
    print('well formed data')
if (flag == False):
    print('brackets do not match')