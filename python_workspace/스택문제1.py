def reverse(data):
    stack = list()
    for c in data:
        stack.append(c)

    result=""
    while len(stack)!=0:
        result = result + stack.pop()
    return result 

print( reverse("korea") )
