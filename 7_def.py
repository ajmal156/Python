def sum_of_num(*args):
    print(args)
    for i in args:
        print(i *2)
    return sum(args)

get =print(sum_of_num(1,2,3,4,5))
print(sum_of_num(1,2,3,4,5,6))
print(sum_of_num(1,2,3,4,5,6,7))
print(sum_of_num(1,2,3,4,5,6,7,8,9))