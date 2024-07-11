import smtplib
password = 'txxn noyc igch qzup'
email = 'mandal4u1002@gmail.com'

connection = smtplib.SMTP("173.194.193.108", port=587)

connection.starttls()
connection.login(email,password)
connection.sendmail(from_addr=email, to_addrs='csramdev@gmail.com', msg='subject:hello\n\nThe email send by me')
connection.close()