# Python program to clear the screen using os.system

# Import os module
import os

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')
    
#    print("Screen Cleared")
# clrscr()