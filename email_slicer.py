email = input("Enter you email: ").strip()

if "@" in email and email.count("@") ==1:

    parts = email.split("@")
    username = parts[0]
    domain = parts[1]
    

    if username =="" or domain =="":
        print("Invalid email : Username or Domain Name is missing")

    else:
         
        print(f"The Username is : {username}")
        print(f"The domain is : {domain}")
else:
    print("Invalid Email: Please make sure you email has exactly one '@' symbol." )

print(email)
