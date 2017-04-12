#!/usr/bin/python
#Author: Chitrarth Tomar
import word_prob
def check(a):
    '''
    This function will take in email,convert it into dictionary
    and return True if it is a spam
    '''
    B=[]
    a=a.replace(" ","@#$%%$#@").replace("\n","@#$%%$#@")
    B=a.split("@#$%%$#@")
    C={}
    total=0;
    for token in B:
        C[token.lower()]= 0
    for token in B:
        C[token.lower()]+=1
        total+=1
    if "" in C: del C[""]
    for num in list(C):
        if num.isnumeric():
            del C[num]
    print(C)
    return calc(C,total)


def calc(wlist,total):
    '''
    calculate probability of email being a spam
    '''

    p,np=word_prob.prob(wlist)
    
    spam_prob=0.0
    if(p+np!=0):
        spam_prob=p/(p+np)
    val=0;
    if(spam_prob>=0.50):
        word_prob.update(wlist,"spam",total)
        return True;
    else:
        word_prob.update(wlist,"not_spam",total)
        return False;
f=open("testspam.txt","r")
a=f.read()
#print(a)
check(a)
