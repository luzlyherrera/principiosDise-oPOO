class Calculadora:

    def __init__(self, num, num1, operacion):
        self.num = num
        self.num1 = num1
        self.operacion = operacion
        
    def calcular(self):
        return self.operacion.op(self.num,self.num1)

	
        
class Operaciones:
	
    def op(self,num,num1):	
        pass
		
class Suma(Operaciones):
	
	def op(self,num,num1):
		return num1+num
	
class Resta(Operaciones):
	
	def op(self,num,num1):
		return num-num1
	
class Multi(Operaciones):
	
	def op(self,num,num1):
		return num*num1
	
class Divi(Operaciones):
	
	def op(self,num,num1):
		if(num1==0):
			print("No se puede realizar esta división, cariña")
		else:
			return num/num1
	      
opt=" "
while opt!="salir":
    opt = input("ingrese la operacion a realizar: ")
    num = int(input("ingrese un primer numero: "))
    num1 = int(input("ingrese un segundo numero: "))
    
    if(opt=="suma"):
        operacion = Suma()
    elif(opt=="resta"):
        operacion = Resta()
    elif(opt == "multiplicacion"):
        operacion = Multi()
    elif(opt == "division"):
        operacion = Divi()
    elif(opt == "salir"):
        print("fin programa")
    else:
        print("ingrese una operacion valida")
    
    calculo = Calculadora(num,num1,operacion)
    print("el resultado de la operacion {} entre {} y {} es : {}".format(opt, num, num1, calculo.calcular()))