

nombre = input("ingrese su nombre") 
estatura = float(input("ingrese su estatura")) 
peso = float(input("ingrese su peso")) 
imc = peso/ estatura**2 
print ("su indice de masa corporal es:", imc) 

if imc < 16.5:
    print ("su indice de masa corporal es: delgadez severa")
elif imc >= 18.5 and imc < 25:
    print ("su indice de masa corporal es: peso normal")
elif imc >= 25 and imc < 30:
    print ("su indice de masa corporal es: sobrepeso")
elif imc >= 30 and imc < 35:
    print ("su indice de masa corporal es: obesidad")
elif imc >= 35 and imc < 40:
    print ("su indice de masa corporal es: obesidad severa")
else:
    print ("su indice de masa corporal es: extrema obesidad")

if estatura < 1.50:
    print ("su estatura es: eres muy pequeño")
elif estatura >= 1.50 and estatura < 1.60:
    print ("su estatura es: eres pequeño")
elif estatura >= 1.60 and estatura < 1.70:
    print ("su estatura es: tienes una estatura normal")
elif estatura >= 1.70 and estatura < 1.80:
    print ("su estatura es: estás un poco alto")
elif estatura >= 1.80 and estatura < 1.90:
    print ("su estatura es: eres alto")
else:
    print ("su estatura es: eres muy alto")

