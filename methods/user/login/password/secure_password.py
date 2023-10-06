# AA
import re  
def check_security(password: str) -> dict:
    if len(password) < 8:
        return {
     "success": False,
     "response": "Password less than 8 characters.",
     "data": {}
      }
    if not re.search(r"[A-Za-z]",password):
        return {
     "success": False,
     "response": "Password not include:\nat least one uppercase letters and lowercase letters.",
     "data": {}
      }
    if not re.search(r"[a-z]",password):
        return {
     "success": False,
     "response": "Password not include:\nat least one lowercase letters.",
     "data": {}
      }
    if not re.search(r"[A-Z]",password):
        return {
     "success": False,
     "response": "Password not include:\nat least one uppercase letters.",
     "data": {}
      }
    return {
     "success": True,
     "response": "Password available.",
     "data": {}
       }
# if __name__ == "__main__":
#    print(check_security(""))

