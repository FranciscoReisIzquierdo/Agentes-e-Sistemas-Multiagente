
class Person:
    def __init__(self, firstname, lastname, age, nacionality):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.nacionality = nacionality


class Student(Person):
    def __init__(self, ano, curso):
        self.ano = ano
        self.curso = curso


def isParOrImpar(number):
    if number % 2 == 0:
        print("O número " + str(number) + " é par")
    else: 
        print("O número " + str(number) + " é ímpar")

def media(lista):
    acumulator = 0
    quantidade = 0
    for number in lista:
        acumulator += number
        quantidade += 1
    print("Média: " + str(acumulator/ quantidade))


def t1():
    isParOrImpar(int(input("Insira o número: ")))

def t2():
    lista = []
    while True:
        value = input("Insira o número para a lista: ")
        if value == "done":
            break
        else:
            lista.append(int(value))
    media(lista)

def printfname(p):
    print(p.firstname, p.lastname)


def t3():
    p = Person("Francisco", "Izquierdo", 22, "Português")
    printfname(p)



def t5():
    phone_book = { "John" : [8592970000], "Bob" : [7994880000], "Tom" : [9749552647] }

    key = input("Insira a chave: ")

    for element in phone_book:
        if element == str(key):
            print("Chave encontrada: " + element + ":" + str(phone_book[element]))
            return
        
    print("Chave não encontrada!")



# main - tests
if __name__ == '__main__':
    t1()
    t2()
    t3()
    t5()
    
    