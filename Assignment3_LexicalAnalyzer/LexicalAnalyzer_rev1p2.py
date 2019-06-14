#Compilers and Development of Libraries
#Assignment-3
#Lexical Analyzer for the C language
#Code is written in Python
#It must return a symbol table in the next form:
#Token type / Lexeme / Line numbe / Column number
#It should be able to identify lexical errors (use a special token type "unknown")
#Marcos A. Camarena R.
#June 2019
#based on https://www.pythonmembers.club/2018/05/01/building-a-lexer-in-python-tutorial/  

import sys
from prettytable import PrettyTable
sys.path.append(r'C:\temp\Python')
sys.path.append(r'C:\temp\Python\Assignment-3')

#Defining Keywords and Operators for C Language
keywordsC = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double',
             'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 
             'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch',
             'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
operatorsArithmeticC = ['+', '-', '*', '/', '%']
#print operatorsArithmeticC[0]
operatorsIncDecC = ['++', '--']
operatorsAsignmentC = ['=', '+=', '-=', '*=', '/=', '%=', ',']
operatorsRelationalC = ['==', '>', '<', '!=', '>=', '<=']
opeartorsLogicalC = ['&&', '||', '!']
operatorsBytwiseC = ['&', '|', '^', '~', '<<', '>>']
operatorsTernaryC = ['?']
specialCharactersC = ['(', ')', '[', ']', '.', '#', '%', '"']
whiteSpaceC = ' '
lexeme = ''

#Read a string char by char
#rjust() returns the string right justified in a string of specified length
string = 'x = 1 + 2'
for i, char in enumerate(string):
    print 'char', str(i+1).rjust(2, ' '), ':', char 

#Check if next char is a keyword (whiteSpaceC)
string = 'x = 1 + 3 '
print
for i,char in enumerate(string):
    if char != whiteSpaceC:
        lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == whiteSpaceC: # if next char == ' '
            print lexeme
            lexeme = ''
    
#Adding Keywords and Operators
KEYWORDS = keywordsC + operatorsIncDecC + operatorsAsignmentC + operatorsRelationalC + opeartorsLogicalC + operatorsBytwiseC + operatorsTernaryC + specialCharactersC 
string = '''
#include <stdio.h>

int main()
{
int x;
printf("Introduce un numero: ");
scanf("%d",&x);
if (x>=0) {
	printf("El numero %d es positivo \n",x);
	} else {
	printf("El numero %d es negativo \n",x);
	}
}
'''
print
for i,char in enumerate(string):
    if char != whiteSpaceC:
            lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == whiteSpaceC or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
            if lexeme != '':
                print(lexeme.replace('\n', '<newline>'))
                lexeme = ''

#Token Table for the C language
#print 'The Keywords for C are: auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while'
t = PrettyTable(['Token type', 'Lexeme'])
t.add_row(['Digits', '0 1 2 3 4 5 6 7 8 9'])
t.add_row(['Lower Case', 'a ... z'])
t.add_row(['Upper Case', 'A ... Z'])
t.add_row(['Arithmetic Operators', '+ - * / %'])
t.add_row(['Increment Decrement Operators', '++ --'])
t.add_row(['Assignment Operators', '= += -= * /= %= ,'])
t.add_row(['Relational Operators', '== > < != >= <='])
t.add_row(['Logical', '&& || !'])
t.add_row(['Bitwise', '& | ^ ~ << >>'])
t.add_row(['Ternary Operator', '?'])
t.add_row(['Special Characters', '( ) [ ] . # % "'])
print
print "Token table for the C Language"
print t

