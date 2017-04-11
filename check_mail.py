#Author: Chitrarth Tomar
#import email
import word_prob
def check(a):
    '''
    This function will take in email,convert it into dictionary
    and return True if it is a spam
    '''
    B=[]
    B=a.split(" ")
    C={}
    total=0;
    for token in B:
        C[token]= 0
    for token in B:
        C[token]+=1
        total+=1
    if "" in C: del C[""]
    print (C)
    return calc(C,total)


def calc(wlist,total):
    '''
    calculate probability of email
    '''
    nr=1.00
    dr=1.00
    for w in wlist:
        nr*=word_prob.prob(w)
        dr*=(1-word_prob.prob(w))
    spam_prob=0.0
    if(nr+dr!=0):
        spam_prob=nr/(nr+dr)
    val=0;
    #if(spam_prob>=0.80):
        #considering new word in spam will be in spam again
    word_prob.update(wlist,0.51,1,total)
    return True;
#    else:
        #considering new word in non spam will not be in spam
#        word_prob.update(wlist,0.4,0.01,total)
#        return False;
f=open("testspam.txt","r")
a=f.read()
#print(a)
check(a)
