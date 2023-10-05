'''
Example Return Type:

return {
    "success": False,
    "response": "Password less than * characters.",
    "data": {}
}

return {
    "success": True,
    "response": "Password available.",
    "data": {}
}
'''

# AA
def check_security(password: str) -> dict:
    ...