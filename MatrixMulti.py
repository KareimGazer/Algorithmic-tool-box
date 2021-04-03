#Strassen's Subcubic Matrix Multiplication Algorithm

def getMatrix(lst, N):
    return [lst[i*N:N*(i+1)]for i in range(N)]

def getSubMatrix(M, r1, r2, c1, c2):
    return [M[i][c1:c2]for i in range(r1,r2)]

def add(A, B):
    #A,B must have the same dimensions
    result = [[A[i][j]+B[i][j] for j in range(len(A[i]))] for i in range(len(A))]
    return result

def subtract(A, B):
    #A,B must have the same dimensions
    result = [[A[i][j]-B[i][j] for j in range(len(A[i]))] for i in range(len(A))]
    return result

def multiply(X, Y):
    if len(X)==1 and len(X[0])==1 and len(Y)==1 and len(Y[0])==1:
        return [[X[0][0]*Y[0][0]]]
    else:
        n, k, m = len(X), len(Y), len(Y[0])
        a = getSubMatrix(X, 0, n//2, 0, k//2)
        b = getSubMatrix(X, 0, n//2, k//2, k)
        c = getSubMatrix(X, n//2, n, 0, k//2)
        d = getSubMatrix(X, n//2, n, k//2, k)
    
        e = getSubMatrix(Y, 0, k//2, 0, m//2)
        f = getSubMatrix(Y, 0, k//2, m//2, m)
        g = getSubMatrix(Y, k//2, k, 0, m//2)
        h = getSubMatrix(Y, k//2, k, m//2, m)
        
        p1 = multiply(a, subtract(f, h))
        p2 = multiply(add(a, b), h)
        p3 = multiply(add(c, d), e)
        p4 = multiply(d, subtract(g,e))
        p5 = multiply(add(a,d), add(e,h))
        p6 = multiply(subtract(b,d), add(g, h))
        p7 = multiply(subtract(a, c), add(e,f))
        
        A = subtract(add(p5, p4), add(p2, p6))
        B = add(p1, p2)
        C = add(p3, p4)
        D = subtract(add(p1, p5), subtract(p3, p7))
        left = A+C
        right = B+D
        return [[left[i]+right[i]] for i in range(len(left))]
        

matrix = getMatrix(lst, 3)
print(matrix)
print(getSubMatrix(matrix, 0, 2, 0, 2))

A = [[1,1], [1,1]]
B = [[2,2], [2,2]]
print(add(A,B))
print(multiply(A, B))

