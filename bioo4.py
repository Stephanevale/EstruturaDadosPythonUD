lista = [1,2,3,4,5]
def constant(n): #constant O(1)
    print(n[0])
    print()

constant(lista)

def linear(m): #Linear O(n)
    for i in m:
        print(i)
        print()

linear(lista)

def quadratica(o): #quadratica O(n^2)- polinomial
    for l in o:
        for j in o:
            print(l,j)
            print('----')
quadratica(lista)

def combinacao(b): #o(1) + o(5) + o(n) + o(3) o(9) + o(2n) -> O(n)
    print(b[0]) #big O(1)
    for k in range(5):  #big o(5)
        print('test ', k)
    for k in b: #big o(n)
        print(k)
    for k in b: #big o(n)
        print(k)

    print('python') #big o(3)
    print('python')
    print('python')

combinacao(lista)

