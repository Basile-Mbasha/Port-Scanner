import re
import pyfiglet

def check_password_strength(password):
 score = 0
 suggestions = []

 # Check length
 if len(password) >= 8:
   score += 1
 else:
   suggestions.append("Password should be at least 8 characters long")

 # Check for uppercase letter
 if re.search(r"[A-Z]", password):
   score += 1
 else:
   suggestions.append("Password should contain at least one uppercase letter")

 # Check for lowercase letter
 if re.search(r"[a-z]", password):
   score += 1
 else:
   suggestions.append("Password should contain at least one lowercase letter")

 # Check for numeric digit
 if re.search(r"\d", password):
   score += 1
 else:
   suggestions.append("Password should contain at least one numeric digit")

 # Check for special character
 if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
   score += 1
 else:
   suggestions.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")

 return score, suggestions

# Print ASCII art banner
ascii_banner = pyfiglet.figlet_format("Password Checker", width=100)
ascii_banner = ascii_banner.center(100)
print(ascii_banner)

while True:
 password = input("Input a password: ")
 score, suggestions = check_password_strength(password)

 if score == 5:
  print("Password strength: Strong")
  break
 elif score == 4:
  print("Password strength: Medium")
  break
 else:
  print("Password strength: Weak")

 if suggestions:
  print("Suggestions to strengthen your password:")
  for suggestion in suggestions:
      print(suggestion)

 retry = input("Do you want to try again? (Y/N): ")
 if retry.lower() not in ['yes', 'y']:
   break
