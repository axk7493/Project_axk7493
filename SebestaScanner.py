# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 22:52:50 2014

@author: Abhinav Kotha
"""


charClass=''
nextChar=''
nextToken=0
lexLen=0
lexeme=[]


INT_LIT=10
IDENT=11
ASSIGN_OP=20
ADD_OP=21
SUB_OP=22
MULT_OP=23
DIV_OP=24
LEFT_PAREN=25
RIGHT_PAREN=26

LETTER=0
DIGIT=1
UNKNOWN=99
EOF= -1
in_fp='c'
isFirst=True


def getChar():
    global nextChar
    global charClass
    global EOF
    global in_fp
    global isFirst
    if isFirst:
        in_fp=open('C:\Users\Abhinav Kotha\Desktop\Front.in','r')
        isFirst=False
       
    try:
        
        nextChar=in_fp.read(1) 
        
        if nextChar > EOF:
            
            if nextChar.isalpha():
                
                charClass=LETTER
            elif nextChar.isdigit():
                charClass=DIGIT
            else:
                charClass=UNKNOWN
                                
        else:
            charClass=EOF
        
    except:
        print 'File cant be read'
        

def lex():
    global lexLen
    global nextToken
    
    getNonBlank()
    
    if charClass==LETTER:
        addChar()
        getChar()
        while (charClass==LETTER):
            addChar()
            getChar()
        nextToken=IDENT
        
    elif charClass==DIGIT:
        addChar()
        getChar()
        while (charClass==DIGIT):
            addChar()
            getChar()
        nextToken=INT_LIT
    
    elif charClass==UNKNOWN:
        lookup(nextChar)
        getChar()
    
    else:
        nextToken=EOF
        lexeme[0]='E'
        lexeme[1]='0'
        lexeme[2]='F'
        lexeme[3]='\0'
    
    print 'Next Token is:'+str(nextToken)+',Next Lexeme is '+''.join(lexeme)
    del lexeme[:]
    return nextToken

def addChar():
    global lexLen
    global lexeme
    if len(lexeme)<=98:
        lexeme.append(nextChar)
       
    else:
        print 'Error: Lexeme is too long'
def getNonBlank():
    while (nextChar.isspace()):
        getChar()

def lookup(ch):
    
    if ch == '(':
        addChar()
        nextToken=LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken=RIGHT_PAREN
    elif ch=='+':
        addChar()
        nextToken=ADD_OP
    elif ch=='-':
        addChar()
        nextToken=SUB_OP
    elif ch=='*':
        addChar()
        nextToken=MULT_OP
    elif ch=='/':
        addChar()
        nextToken=DIV_OP
        
    return nextToken
    
    
def main():
    
    
    global EOF
   
    getChar()

        
    print 'main'
    
        
    while (True):
        lex()
        
        
        if nextToken == EOF:
            break
                   
if __name__=='__main__':
    main()
