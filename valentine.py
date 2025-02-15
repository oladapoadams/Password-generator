from datetime import datetime

today = datetime.today ()
valentine = datetime(today.year,2, 14)

if today > valentine:
    valentine = datetime(today.year + 1,2, 14)

days_left = (valentine - today).days

def print_heart():
    heart = """
    ******     *****  
    *******   ******* 
   ***************** 
    **************** 
      ***********   
        *******     
          ***       
           *        
    """
    print(heart)
print_heart()
 
import sys
import time

def glowing_text(text, repeat=3):
    colors = ["\033[91m]", "\033[95']","\\033[94m]", "\033[92m]"]
    reset = "\033[0m]"

    for _ in range(repeat):
        for color in colors:
            sys.stdout.write(f"\r{color}{text} {reset}")
            sys.stdout.flush()
            time.sleep(0.5)
glowing_text("Happy Valentine's Day! ", 5)



print(f" Only {days_left} days until Valentine's Day! ")


