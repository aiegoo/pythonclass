def sum(n):
    """
    이 함수는 재귀호출로 1~n까지의 합계를 
    구하는 함수입니다.
    호출예) print(sum(10))
    """
    if n ==1:
        return 1
    else:
        return n + sum(n-1)

print( sum( 10 ))
print( help(sum))
