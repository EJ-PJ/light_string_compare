import sys
from colors_text import bcolors


def main():

    args_list = get_args()

    print("====================COMPARE TWO STRING====================")

    #lower case first string 
    first_string_lw = args_list[1].lower()

    #lower case second string 
    second_string_lw = args_list[2].lower()

    print("First string: ", bcolors.WARNING + first_string_lw + bcolors.ENDC)

    print("Second string: ",  bcolors.WARNING + second_string_lw + bcolors.ENDC)

    if(first_string_lw == second_string_lw):
        print(bcolors.OKGREEN + "STRING ARE EQUAL" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "STRINGS NOT EQUAL" + bcolors.ENDC)

#returns a list of args
def get_args():

    #useage program print
    if((len(sys.argv) == 1)):
        usage_output()
        sys.exit(0)

    #proofs if there are more than 2 aguments
    if((len(sys.argv) == 2) or (len(sys.argv) > 3)):
        print("Error: Too many or very few arguments")
        sys.exit(0)

    arg_list = [] #list of args

    for arg in sys.argv: #looping throuhg every arg pass
        arg_list.append(arg)

    return arg_list

def usage_output():
    description = " Light String Compare - compares two simples strings"
    usage = " USAGE: "
    args_description = "string_compare string1 string2"

    print(description)
    print(usage, end="")
    print(args_description)  
main()