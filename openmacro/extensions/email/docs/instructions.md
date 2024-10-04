# EMAIL APP
email = Email()
status = email.send("amor.budiyanto", title, content) # Sends an email to recipient
print(status) # {"state": "success"}