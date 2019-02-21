frstList = []
scndList = []

def fizzbuzz(frstList,scndList):

    length3 = len(frstList)
    length4 = len(scndList)

    combinedlength = length3+length4

    if(combinedlength % 15 == 0):
        print("fizzbuzz")
    elif(combinedlength % 5 == 0):
        print("buzz")
    elif(combinedlength % 3 == 0):
        print("fizz")
    else:
        print(combinedlength)
fizzbuzz([1,2,3],[])