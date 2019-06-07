#Compilers and Development of Libraries
#Assignment-2
#Pre-processor for the C language
#Code is written in Python
#The following directives are processed by the pre-processor:
#include, define, undef, if, else, endif
#Marcos A. Camarena R.
#June 2019

import sys
sys.path.append(r'C:\temp\Python')

'''
#Reading the File
FileName = ('class2.c')
with open(FileName, 'rt') as file:
    lines_in_file = file.read()
    print lines_in_file
    file.close()
'''
#Reading the line number and content of the File
FileName = ('class2.c')
print
with open(FileName, 'r') as file:
    data = file.readlines()
    #Print each line
    for i in range(len(data)):
        print "Line number:" ,i
        print data[i] 
    file.close()

#Searching for the Directives, if founded we will write to a new file 
FileName = ('class2.c')
print
print "Searching for Preprocessor Directives of (#include, #define, #undef, #if, #else, #endif)"
newFile = open('class2_NewProcDirectives.c', 'w')
with open(FileName, 'r') as file:
    for line in file:
        if "#include" in line:
            print "#include"
            newFile.write('This is a test for the #include directive \n')
        if "#define" in line:
            print "#define"
            newFile.write('This is a test for the #define directive \n')
        if "#undef" in line:
            print "#undef"
            newFile.write('This is a test for the #undef directive \n')
        if "#if" in line:
            print "#if"
            newFile.write('This is a test for the #if directive \n')
        if "#else" in line:
            print "#else"
            newFile.write('This is a test for the #else directive \n')
        if "#endif" in line:
            print "#endif"
            newFile.write('This is a test for the #endif directive \n')
    file.close()
    newFile.close()

#Searching for the Directives and locating the start index position
FileName = ('class2.c')
print
with open(FileName, 'rt') as file:
    data = file.readlines()
    for i in range(len(data)): 
        if data[i].find('#include') != -1:
            print "#include: Line number:",i, "@ Start Index:",(data[i].find('#include'))
        if data[i].find('#define') != -1:
            print "#define: Line number:",i, "@ Start Index:",(data[i].find('#define'))
        if data[i].find('#undef') != -1:
            print "#undef: Line number:",i, "@ Start Index:",(data[i].find('#undef'))
        if data[i].find('#if') != -1:
            print "#if: Line number:",i, "@ Start Index:",(data[i].find('#if'))
        if data[i].find('#else') != -1:
            print "#else: Line number:",i, "@ Start Index:",(data[i].find('#else'))
        if data[i].find('#endif') != -1:
            print "#else: Line number:",i, "@ Start Index:",(data[i].find('#endif')) 
file.close()







        

