# def add(num1,num2):
#     return num1+num2
# variable length argument method
# def pri(name,loca):
#     print(name)
#     print(loca)
# pri("ajay","kakkand","aliva")
#
# TypeError: pri() takes 2 positional arguments but 3 were given

def add(**args):#accecpt any value by key avlue pair
    print(args)
    res=0
    for k,v in args.items():
        res+=v
    print(res)
add(num1=10,num2=20,num3=30)
