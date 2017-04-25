import check_mail
import regex
import os
for i in range(1,3):
    path="/Users/HP 15 P077 TX/Desktop/spam/spam_public/bare/part"+str(i)
    all = os.listdir(path)

    for b in all:
        if "sp" not in b:
            print (path+"/"+b)
            f=open("spam_public/bare/part"+str(i)+"/"+b,"r")
            a=f.read()
            a=regex.sub("<http.{0,}\.com.{0,}>",'@#$%%$#@',a)
            a=regex.sub(r'([^\s\w]|_)+','@#$%%$#@',a)#add for $
            a=a.replace("\n","@#$%%$#@").replace("\r","@#$%%$#@").replace(" ","@#$%%$#@").replace("\t","@#$%%$#@")
            ans=check_mail.check(a)
            if(ans):print("Spam")
            else:print("OK mail")
"""
f=open("spam_public/lemm/part1/spmsga129.txt","r")
#f=open("spam.txt")
a=f.read()
a=regex.sub("<http.{0,}\.com.{0,}>",'@#$%%$#@',a)
a=regex.sub(r'([^\s\w]|_)+','@#$%%$#@',a)#add for $
a=a.replace("\n","@#$%%$#@").replace("\r","@#$%%$#@").replace(" ","@#$%%$#@").replace("\t","@#$%%$#@")
ans=check_mail.check(a)
print (ans)
"""
