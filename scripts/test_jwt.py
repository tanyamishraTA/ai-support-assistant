from app.auth.jwt import (
    create_access_token,
    decode_access_token,
)

token = create_access_token(
    {
        "sub": "1",
        "email": "tanya@gmail.com",
        "role": "employee",
    }
)

print("TOKEN")
print(token)

print()

print("PAYLOAD")
print(decode_access_token(token))