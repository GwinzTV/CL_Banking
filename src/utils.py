def draw_line(symbol="-", length=80, end="\n"):
    return symbol * length + end

def intro():
    output = '''
***********************************************
*=============================================*
*|=     Welcome to Command Line Banking     =|*
*=============================================*
***********************************************
'''
    return output

def success():
    input("*** Sucessful Transaction ***\n    Press Enter to continue")

def fail():
    input("*** Unsucessful Transaction ***\n    Press Enter to continue")