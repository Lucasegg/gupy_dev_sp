def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

#loop para verificar a sequencia do numero digitado anteriormente
def is_fibonacci(x):
    i = 0
    while True:
        if fibonacci(i) == x:
            return True
        elif fibonacci(i) > x:
            return False
        i += 1
#Aqui o usuário irá digitar um número:
num = int(input("Digite o n[umero que deseja  "))

if is_fibonacci(num):
    print("O número pertence a sequencia Fibonacci")

else:
    print("O número não pertence a sequencia Fibonacci")

