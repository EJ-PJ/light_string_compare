import sys

def main():

    args_list = get_args()

    print("====================COMPARE TWO STRING====================")

    #lower case string 
    first_string_lw = args_list[1].lower()

    #lower case second string 
    second_string_lw = args_list[2].lower()

    if(first_string_lw == second_string_lw):
        print("Strings are EQUAL")
    else:
        print("Strings are NOT EQUAL")

#returns a list of args
def get_args():

    #proofs if there are more than 2 aguments
    if((len(sys.argv) == 1) or (len(sys.argv) == 2) or (len(sys.argv) > 3)):
        print("Error: Too many or very few arguments")
        sys.exit(0)

    arg_list = [] #list of args

    for arg in sys.argv: #looping throuhg every arg pass
        arg_list.append(arg)

    return arg_list

main()