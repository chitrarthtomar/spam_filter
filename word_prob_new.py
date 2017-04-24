#!/usr/bin/python
#Author: Chitrarth Tomar
import json
import math
fname='spam_count.json'
notfname='not_spam_count.json'
def prob(wlist):
    '''
    This function will return the probability of a word present in the mail.
    '''
    p_spam=1.00
    p_not_spam=1.00
    db=json.load(open(fname))
    notdb=json.load(open(notfname))


    for w in wlist:
        if w in db:
            p_spam+=math.log(db[w]/db["total_words_in_spam"])
        if w in notdb:
            p_not_spam+=math.log(notdb[w]/notdb["total_words_in_notspam"])

    if "spam_count_total" in db:
        p_spam+=math.log(db["spam_count_total"])
    if "not_spam_count_total" in notdb:
        p_not_spam+=math.log(notdb["not_spam_count_total"])

    print(str(p_spam)," ",str(p_not_spam),"####")
    return math.exp(p_not_spam/p_spam)

def update(wlist,what,total):
    '''
    Add word to the list.
    The probability is updated if word is present.
    '''
    db=json.load(open(fname))
    notdb=json.load(open(notfname))

    if "total_words_in_spam" not in db:
        db["total_words_in_spam"]=1
    if "total_words_in_notspam" not in notdb:
        notdb["total_words_in_notspam"]=1

    if "spam_count_total" not in db:
        db["spam_count_total"]=0
    if "not_spam_count_total" not in notdb:
        notdb["not_spam_count_total"]=0
    if what == "spam":
            db["spam_count_total"]+=1
            db["total_words_in_spam"]+=total
    else:
            notdb["not_spam_count_total"]+=1
            notdb["total_words_in_notspam"]+=total
    for w in wlist:
        if what == "spam":
            if w not in db:
                db[w]=wlist[w]
            else:
                db[w]+=wlist[w]
        else:
            if w not in notdb:
                notdb[w]=wlist[w]
            else:
                notdb[w]+=wlist[w]
    print (db["spam_count_total"],notdb["not_spam_count_total"])
    with open(fname,'wt') as fn:
        json.dump(db,fn)
    with open(notfname,'wt') as fn:
        json.dump(notdb,fn)
