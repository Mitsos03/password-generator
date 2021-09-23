import colorama
from colorama import Fore,Style
import random
import string
length_of_string = int(input(Fore.MAGENTA+"Set length of characters: "))
random_string = "".join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(length_of_string))
if length_of_string  <6:
    print(Fore.RED,"Weak password:",random_string)
elif 6 <= length_of_string <=8  :
   print (Fore.YELLOW,"Medium password:",random_string)
else: print(Fore.GREEN,"Strong password:",random_string)