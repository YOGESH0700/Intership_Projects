def add(n1,n2):
    return n1+n2


def sub(n1,n2):
    return n1-n2


def multi(n1,n2):
    return n1*n2


def divi(n1,n2):
    return n1/n2


operations = {
    "+":add,
    "-":sub,
    "/":divi,
    "*":multi,
}
def calculator():
    is_loop_on = True
    num_n1 = input("Enter The  Number: ")
    while is_loop_on:
        for i in operations:
            print(i)
        ope = input("Enter The Operation: ")
        num_n2 = input("Enter The  Number: ")
        answer = operations[ope](int(num_n1),int(num_n2))
        print(f"{num_n1} {ope} {num_n2} = {answer}")
        continue_loop = input("Do You Want Continue Calculate With Number Type (Yes or NO): ").lower()

        if continue_loop == "yes":
            num_n1 = answer
        else:
            is_loop_on = False
            restart = input("If You Want To Restart Calculator Type (Yes or No): ").lower()
            if restart == "yes":
                calculator()
            else:
                print("Thank You For Using Calculator")

calculator()
