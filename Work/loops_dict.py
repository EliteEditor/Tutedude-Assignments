user ={
    "username":"User",
    "password":"123@67",
    "email":"user2026@gmail.com",
    "address":"Mumbai",
    "country":"India"
}

sensitive_info=["password","email"]

for i in sensitive_info:
    user.pop(i)
    
print(user)