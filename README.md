# Endpoint

The endpoint data json request goes as follow:


# Method Type: "user"

```json
{
    "method": "user/login",
    "data": {
        "username": "admin",
        "password": "password123"
    }
}
```

```json
{
    "method": "user/register",
    "data": {
        "username": "admin",
        "password": "password123"
    }
}
```

```json
{
    "method": "user/change_password",
    "data": {
        "oldpassword": "password123",
        "newpassword": "password1234",
        "sessionid": ""
    }
}
```
```json
{
    "method": "user/logout_everywhere",
    "data": {
        "sessionid": ""
    }
}
```
```json
{
    "method": "action/main",
    "data": {
        "sessionid": ""
    }
}
```

