#!/usr/bin/python
#Author: Chitrarth Tomar
import word_prob_new
def check(a):
    '''
    This function will take in email,convert it into dictionary
    and return True if it is a spam
    '''
    B=[]
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
    #print(C)
    return calc(C,total)


def calc(wlist,total):
    '''
    calculate probability of email being a spam
    '''

    p=word_prob_new.prob(wlist)
    
    spam_prob=0.0
    if(p!=0):
        spam_prob=1/(1+p)
    val=0;
    print("Spam probability is "+str(spam_prob))
    if(spam_prob>=0.50):
    #    word_prob_new.update(wlist,"spam",total)
        return True;
    else:
    #    word_prob_new.update(wlist,"not_spam",total)
        return False;

