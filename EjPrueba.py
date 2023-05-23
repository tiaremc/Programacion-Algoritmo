opc=0
total=0
cont1=0
cont2=0
cont3=0
cant=0
cot=0
pagototal=0
totalcaja=0
print("Bienvenido a nuestra consulta dental")
while opc!=3:
    while True:
        try:
            opc=int(input("1.-Cotización\n2.-Renunciar\n3.-SALIR:\n"))
            if opc>=1 and opc<=3:
                break
            else:
                print("Ingrese opcion valida")
        except:
            print("Ingrese opcion valida")
    if opc==1:
        total=0
        while True:
            try:
                print("Tratamientos")
                print("*"*10)
                print("1.-Carillas Porcelana  $250.000")
                print("2.-Implantes Dentales  $475.000")
                print("3.-Ortodoncia Brackets $800.000")
                print("4.-Salir")
                cot=int(input("Ingrese opcion:\n"))
            except:
                print("Ingrese opcion valida")
                if cot==4:
                    break
                else:
                    if opc>=1 and opc<=4:
                        while True:
                            try:
                                cant=int(input(f"¿Cuantos tratamientos quiere?\n"))
                                if cant>0:
                                    break
                                else:
                                    print("Ingrese cantidad valida")
                            except:
                                print("Ingrese opcion valida")
            if cot==1:
                cont1+=cant
                total+=250000*cont1
                print(f"Su total es {total}")
            elif cot==2:
                cont2+=cant
                total+=475000*cont2
                print(f"Su total es {total}")
            elif cot==3:
                cont3+=cant
                total+=800000*cont3
                print(f"Su total es {total}")
            else:
                print("Ingrese opcion valida")
            subtotal=total+cont1+cont2+cont3
        while True:
            try:
                print("DESCUENTOS")
                print("1.-Trabajador Auxiliar, se aplicará un descuesto del 15%")
                print("2.-Trabajador Administrativo, se aplica un descuento del 10%")
                print("3.-Trabajador Docente, 5% descuento.")
                desc=int(input("Si tiene algun descuento, ingreselo:\n"))
                if desc>=1 and desc<=3:
                    break
                else:
                    print("Ingrese opcion valida")
            except:
                print("Ingrese opcion valida")
        if desc==1:
            desc=total*0.15
            total-=desc
            print(f"Usted lleva {cont1} de Carillas Porcelana por {total}")
        elif desc==2:
            desc=total*0.10
            total-=desc
            print(f"Usted lleva {cont2} Implantes Dentales por {total}")
        elif desc==3:
            desc=total*0.05
            total-=desc
            print(f"Usted lleva {cont3} de Ortodoncia Bracket")
    if opc==2:
        totalcaja=0
        totalcaja+=total
print("Adios")

    




                

