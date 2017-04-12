#!/usr/bin/python
#Author: Chitrarth Tomar
import email
import imaplib
import mailbox
import regex
import check_mail
EMAIL_ACCOUNT = "arduinouno1995@gmail.com"
PASSWORD = "9686859627"
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(EMAIL_ACCOUNT, PASSWORD)
while 1:
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "UNSEEN")
    print (data)
    i = len(data[0].split())
    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        parser = email.parser.HeaderParser()
        header=parser.parsestr(email_message.as_string())
       # for i in header:
        #    print (i)
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                message=part.get_payload(decode=True).decode("utf-8")
                message=regex.sub("<http.{0,}\.com.{0,}>",'',message)
                message=regex.sub(r'([^\s\w]|_)+','',message)#add for $
                a=check_mail.check(message.replace("\n","").replace("\r",""))
                if(a):
                    print("spam")
                else:
                    print("not_spam")
                print("######################################################")
    break
