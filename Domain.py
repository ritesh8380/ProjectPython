mail = input("enter the E-mail address :")
index = mail.index("@")
print(f"The Name is {mail[:index]}")
print(f"The domain is {mail[index:]}")

#[start:end:step]