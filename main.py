import os
from time import sleep
"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""

dic_empresas = {
    '123456789':{
        'nombre':'HyJ Ingeniros',
        'email' : 'HyJIngeniros@gmail.com'
    }
}

ANCHO =100

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR ALUMNOEMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        
        ruc = input("Ingrese RUC: ")
        nombre = input("Ingrese Nombre: ")
        email = input("Ingrese Email: ")
        dic_nuevo_empresa = {
            'nombre': nombre,
            'email': email
        }
        dic_empresas[ruc] = dic_nuevo_empresa
        print("Empresa registrado existosamente")
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESA")
        print("=" * ANCHO)
        for ruc,info in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"Nombre : {info['nombre']}")
            print(f"Email : {info['email']}")
            print('*' * ANCHO)
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR  EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC de la empresa a actualizar : ")
        if ruc in dic_empresas:
            print(f"Empresa Encontrada : {dic_empresas[ruc]['nombre']}")
            nuevo_nombre = input(f"NUEVO NOMBRE({dic_empresas[ruc]['nombre']}) : ")
            nuevo_email = input(f"NUEVO EMAIL({dic_empresas[ruc]['email']}) : ")
            if nuevo_nombre:
                dic_empresas[ruc]['nombre'] = nuevo_nombre
            if nuevo_email:
                dic_empresas[ruc]['email'] = nuevo_email
            print("EMPRESA ACTUALIZADA EXITOSAMENTE!!!")
        else:
            print('No se econtro la emprsa para el RUC ingresado')
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC de la empresa a actualizar : ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print('EMPRESA ELIMINADO EXITOSAMENTE')
        else:
            print('No se econtro el empresa para el RUC ingresado')
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(1)
        break
    else:
        print("OPCION NO VALIDA...")
    
    input("Presione ENTER para continuar...")
