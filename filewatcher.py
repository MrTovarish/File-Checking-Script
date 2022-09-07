import sys
import time
from main import run_my_script

if __name__ == "__main__":
    
    def read_file():
        with open('match.html', 'r') as my_file:
            results = my_file.readlines()
        return results
    
    current_file = read_file()
    modified_file = 'x'
    
    time.sleep(5)
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    print('Beginning Loop')
    
    while current_file != 'y':
        modified_file = read_file()
        if current_file != modified_file:
            print('Hey! Notice me! *************************************')
            time.sleep(1)
            print('I\'m running the Script now!')
            run_my_script()
            time.sleep(3)
            current_file = modified_file
            continue
        elif current_file == modified_file:
            print('I am still running')
            time.sleep(2)
            continue 
        else:
            print('You have encountered an error, please restart the program.')
            break
            
            
            