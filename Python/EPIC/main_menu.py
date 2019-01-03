import bfi
import roadrunner
import sys
import fileclean
languages = ["brainf**k","roadrunner"]

def lan_input():
    lang = input("\nLanguage: ")
    return lang
    
def main():
    lan_choice = lan_input()
    lan_organize(lan_choice)    
    
def lan_organize(lan):
    if lan == languages[0] or lan == "brainfuck":
        printlan = languages[0].upper()
        print(printlan.center(120,"="))
        inputs = bfi.script_input()
        print(bfi.command_script(inputs))
    elif lan == languages[1]:
        printlan = languages[1].upper()
        print(printlan.center(120,"="))
        inputs = roadrunner.script_meep()
        print(roadrunner.meep_script(inputs))
    else:
        print("Error: Invalid Language")
        newlan = lan_input()
        lan_organize(newlan)
        
def filecheck(argument):
    check = fileclean._Fileclean(argument)
    if argument.endswith(".b"):
        print("RESTART: BRAINF**K".center(120,"="))
        bf_clean_code = check.bfclean()
        bfi.command_script(bf_clean_code)
    elif argument.endswith(".rr"):
        print("RESTART: ROADRUNNER".center(120,"="))
        roadrunner.meep_script(check)
    main()
        
        
    
if __name__ == "__main__":
    print("Esoteric Programming Interpreter and Compiler (C) Nicholas Gray 2017\n\nLanguages:")
    for lan in languages:
        print(" " + lan)
    if len(sys.argv) > 1:        
        argu = str(sys.argv[1])
        filecheck(argu)
    else:
        main()
    
