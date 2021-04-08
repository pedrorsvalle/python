def retangulo(lado_a,lado_b):
    """calcula a area de um retangulo"""
    area= lado_a*lado_b
    return area

def triangulo(base,altura):
    """calcula a area de um triangulo"""
    area=(base*altura)/2
    return area

def circulo(raio):
    """calcula a area de um circulo"""
    area=3.14*(raio**2)
    return area

opcao= -1
while opcao!=0:
    print('ecolha o objeto que deseja calcular a area')
          print()
          print('1- retangulo')
          print('2-triangulo')
          print('3-circulo')
          print('0-sair')
          print()
          opcao=int(input('entre com um numero da opcao desejada:'))
          if(opcao==1)
          lado_a = float(input('entre com um lado do retangulo:'))
          lado_ b=
     
    
          
    
















elif(opcao==2):
    base=float(inptut("entre com a base do trianf=gulo:"))
    altura= float(input("entre com a alturado triangulo:"))
    area=triangulo(base,altura)
    print("\nA area do triangulo eh: "area)

elif (opcao==3)
     raio= float(input("entre com o raio do circulo:"))
      area= circilo(raio)
      print("\nA area do circulo eh:" area)

elif(opcao!=0):
     print("\n  nao é uma opcao valida", opcao)
     print()
     print("volte a qualquer hora")                   
