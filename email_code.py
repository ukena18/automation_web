#get the emails from gmail
import imaplib
import email

#gmail imap host
host = 'imap.gmail.com'
#credentials
username = "email"
password = 'password'


def get_code():
    try:
        #set mail to gmail
        mail = imaplib.IMAP4_SSL(host)
        #login to gmail
        mail.login(username, password)
        #select the inbox yuo can changed it later
        mail.select("inbox")
        #search for all
        #you can change to UNSEEN/SEEN
        _, search_data = mail.search(None, "ALL")

        for num in search_data[0].split():
            _, data = mail.fetch(num, '(RFC822)')
            _, b = 

data[0]


            email_message = email.message_from_bytes(b)
            #get the subject and split get the code part
            #it is from 10 to -2 always
            my_sub = email_message["Subject"]
            print(my_sub, type(my_sub))
            try:
                if str(type(my_sub)) == "<class 'str'>":
                    line = email_message["subject"].split(" ")[-1][10:-2]
                    # decoding from base64 to str
                    import base64
                    the_code = 0
                    register_code = base64.b64decode(line).decode().split(" ")
                    print(register_code, len(register_code[-1]))
                    # split it again and get the code
                    if len(register_code[-1]) == 6:
                        the_code = register_code[-1]
                        return the_code
            except:
                pass
    except Exception as err:
        print("fail to parse code from email ", err)


if __name__ == '__main__':
    print(get_code())

