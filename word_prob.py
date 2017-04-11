#Author: Chitrarth Tomar
import json
fname='spam_count.json'
def prob(w):
    '''
    This function will return the probability of a word present in the mail.
    '''
    db=json.load(open(fname))
    if w in db:
        p=db[w]
        return p
    else:
        return 0.4

def update(wlist,val,s,total):
    '''
    Add word to the list.
    The probability is updated if word is present.
    '''
    db=json.load(open(fname))
    for w in wlist:
        if w not in db:
            db[w]=val
        else:
            db[w]=((s*val)+(wlist[w]*db[w]))/(1+wlist[w])
    with open(fname,'wt') as fn:
        json.dump(db,fn)
