from clases import *
from funcionesExternas import *



def main():
    sis= Sistema()
    while True:
        def menu():
            return input('¡BIENVENIDO!\nIngrese su desicion:\n\n1.Agregar un paciente.\n2.Eliminar un paciente\n3.Ver un paciente\n4.Modificar un paciente\n5.Salir\n opcion seleccionada: ')
        if menu() == '1':
            cedula = datoEntero('Cédula: ')
            if sis.verificarExistencia(cedula) == True:
                print(f'El paciente con cedula {cedula} ya se encuentra registrado')
                print(sis.verPaciente(cedula))
                continue
            else:
                p = Paciente()
                p.asignarCedula(cedula)
                p.asignarNombre(obtener_nombre())

                nImplantes = datoEntero('Cuantos implantes tiene el paciente: ')
                while p.lenImplantes() != nImplantes:
                    Tipo = input('\n¿cuál es el implante a ingresar?\n1.Marcapaso\n2.Stent Coronario\n3.Implante Dental\n4.Implante de Rodilla\n5.Implante de Cadera\nOpcion seleccionada: ')
                    if Tipo == "1":
                        m = Marcapasos()
                        m.asignarNumElectrodos(datoEntero('\nNúmero de Electrodos: '))
                        m.asignarConexion(input('Tipo de conexión: '))
                        m.asignarFRECUENCIA(input('Frecuencia de estimulación: '))
                        m.asignarFechaImplantacion(pedir_fecha('Fecha de Implantacion: '))
                        m.asignarDoctor(input('Doctor Responsable de la instalación: '))
                        m.asignarEstado('Estado del Implante: ')

                        p.asignarImplantes(m)
                        continue
                    elif Tipo == '2':
                        st = StentCoronario()
                        st.asignarLongitud(datoFloat('Longitud del stend Coronario: '))
                        st.asignarDiametro(datoFloat('Diametro del implante: '))
                        st.asignarMaterial(input('Material: '))
                        st.asignarFechaImplantacion(pedir_fecha('Fecha de Implantacion: '))
                        st.asignarDoctor(input('Doctor Responsable de la instalación: '))
                        st.asignarEstado(input('Estado del Implante: '))

                        p.asignarImplantes(st)
                        continue
                    elif Tipo == '3':
                        imd = ImplanteDental()
                        imd.asignarSistemaFijacion(input('sistema de fijacion: '))
                        imd.asignarMaterial(input('Material: '))
                        imd.asignarForma(input('Forma: '))
                        imd.asignarFechaImplantacion(pedir_fecha('Fecha de Implantacion: '))
                        imd.asignarDoctor(input('Doctor Responsable de la instalación: '))
                        imd.asignarEstado(input('Estado del Implante: '))

                        p.asignarImplantes(imd)
                        continue
                    elif Tipo == '4':
                        imr = ImplanteRodilla()
                        imr.asignarForma(input('Forma: '))
                        imr.asignarMaterial(input('Material: '))
                        imr.asignarSize(datoFloat('tamaño del Implante: '))
                        imr.asignarFechaImplantacion(pedir_fecha('Fecha de Implantacion: '))
                        imr.asignarDoctor(input('Doctor Responsable de la instalación: '))
                        imr.asignarEstado(input('Estado del Implante: '))

                        p.asignarImplantes(imr)
                        continue
                    elif Tipo == '5':
                        imc = ImplanteCadera()
                        imc.asignarForma(input('Forma: '))
                        imc.asignarMaterial(input('Material: '))
                        imc.asignarSize(datoFloat('tamaño del Implante: '))
                        imc.asignarFechaImplantacion(pedir_fecha('Fecha de Implantacion: '))
                        imc.asignarDoctor(input('Doctor Responsable de la instalación: '))
                        imc.asignarEstado(input('Estado del Implante: '))

                        p.asignarImplantes(imc)
                        continue
                    else:
                        continue
                sis.ingresarPaciente(p)
                
        # if menu() == '2':
        #     cedula = int(input('Ingrese la cédula del paciente a eliminar: '))
        #     if sis.verificarExistencia(cedula) == True:
        #         print(f'¡¡¡¡¡¡El paciente con la cedula {cedula} NO se encuentra registrado!! \n')
        #     else:
        #         sis.eliminarPaciente(cedula)
        #         print('\n---------------------Paciente eliminado con exito.--------------------\n')
        
        if menu() == '3':
            buscar = datoEntero('ingrese la cedula a buscar')
            if sis.verificarExistencia(buscar) == True:
                print(sis.verPaciente(buscar))
        
main()