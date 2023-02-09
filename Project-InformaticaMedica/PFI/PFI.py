from calendar import Calendar, month
from os import close
from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import date
from datetime import datetime
import tkinter as tk
from tkinter import ttk, font
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import messagebox as mb
#from tkinter import scrolledtext as st
import random
import numpy as np

#***************************************************************FUNCIONES DE LOS BOTONES************************************************************
def verificar_cupo():
    conexion = mysql.connect(host="localhost", user="root", password="", database="database-patient")
    cursor = conexion.cursor()  
    cursor.execute("select area_asignada from datos")
    rows = cursor.fetchall()

    cupos=[]
    for row in rows:
        cupos.append(row)

    cupos = np.array(cupos).T
    cupos = list(cupos[0])
    #cupos.count('Urgencias')
    u = StringVar()
    c = StringVar()
    h = StringVar()

    fuente = font.Font(family="Calibri Light", size=10, weight='bold')
    fuente_n = font.Font(family="Calibri Light", size=10)

    label_cupo = Label(Frame_buttons, text='Cantidad de pacientes por área:',font=fuente, bg='snow3').place(x=20, y=30)

    label_u = Label(Frame_buttons, text='Urgencias:',font=fuente, bg='snow3').place(x=20, y=70)
    label_c = Label(Frame_buttons, text='Cirugía:',font=fuente, bg='snow3').place(x=20, y=100)
    label_h = Label(Frame_buttons, text='Hospitalización:',font=fuente, bg='snow3').place(x=20, y=130)

    label_maxu = Label(Frame_buttons, text='(Max. 2)',font=fuente, bg='snow3').place(x=170, y=70)
    label_maxc = Label(Frame_buttons, text='(Max. 4)',font=fuente, bg='snow3').place(x=170, y=100)
    label_maxh = Label(Frame_buttons, text='(Max. 46)',font=fuente, bg='snow3').place(x=170, y=130)

    cupo_urgencias = Label(Frame_buttons, text="",textvariable=u,font=fuente_n, bg='snow3').place(x=140, y=70)
    cupo_cirugia = Label(Frame_buttons, text="",textvariable=c, font=fuente_n, bg='snow3').place(x=140, y=100)
    cupo_hospitalizacion = Label(Frame_buttons, text="",textvariable=h, font=fuente_n, bg='snow3').place(x=140, y=130)

    global cupos_urgencias
    global cupos_cirugia 
    global cupos_hospitalizacion 

    cupos_urgencias =  cupos.count('Urgencias')
    cupos_cirugia =  cupos.count('Cirugia')
    cupos_hospitalizacion = cupos.count('Hospitalizacion')

    u.set(cupos_urgencias)
    c.set(cupos_cirugia)
    h.set(cupos_hospitalizacion)

    conexion.close()

def ingresar():
    id = c_id.get()
    nombres = c_nombres.get()
    apellidos = c_apellidos.get()
    edad = c_edad.get()

    if c_sexo.get() == 1:
        sexo = 'H'
    else:
        sexo = 'M'

    direccion = c_direccion.get()
    ciudad = c_ciudad.get()
    celular = c_celular.get()
    fecha_ingreso = c_fecha_ingreso.get()
    area_asignada = c_area_asignada.get() 

    conexion = mysql.connect(host="localhost", user="root", password="", database="database-patient")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, COUNT(*) Contador FROM datos GROUP BY id HAVING COUNT(*) = 1")
    rows = cursor.fetchall()
    
    historial_id = []
    for row in rows:
        historial_id.append(str(row[0]))

    if historial_id.count(id) == 1:
        MessageBox.showerror("Estado", "Usuario ya existente")

    else:
        if(id=="" or nombres=="" or apellidos=="" or edad == "" or c_sexo.get()==0 or direccion=="" or ciudad=="" or celular==""  or c_area_asignada.get()=='Sin definir'):
            MessageBox.showinfo("Insert status", "Se deben diligenciar todos los datos")

        elif((area_asignada=='Urgencias') & (cupos_urgencias==2)):
            MessageBox.showerror("Estado", "No hay cupo en urgencias")

        elif((area_asignada=='Cirugia') & (cupos_cirugia==4)):
            MessageBox.showerror("Estado", "No hay cupos en cirugía")

        elif((area_asignada=='Hospitalizacion') & (cupos_hospitalizacion==46)):
            MessageBox.showerror("Estado", "No hay cupos en hospitalización")
        
        else:
            if area_asignada == areas[0]:
                medicos_urgencias = ['Jaime Rozo',]
                var_doc.set(medicos_urgencias[0])

            elif area_asignada == areas[1]:
                medicos_cirugia = ['Paula Villa','Carlos López']
                var_doc.set(random.choice(medicos_cirugia))

            elif area_asignada == areas[2]: 
                medicos_hospitalizacion = ['Stephany Arevalo','Camilo Ortega','Diego Ortiz']
                var_doc.set(random.choice(medicos_hospitalizacion))
            
            doctor = c_doctor_asignado.get()

            conexion = mysql.connect(host="localhost", user="root", password="", database="database-patient")
            cursor = conexion.cursor()
            cursor.execute("insert into datos values('"+ id +"','"+ nombres +"','"+ apellidos +"','"+ edad +"','"+ sexo +"','"+ direccion +"','"+ ciudad +"','"+ celular +"', STR_TO_DATE('"+fecha_ingreso+"', '%d/%m/%y'),'"+ area_asignada +"','"+ doctor +"')")
            cursor.execute("commit")

            c_id.delete(0, 'end')
            c_nombres.delete(0, 'end')
            c_apellidos.delete(0, 'end')
            c_edad.delete(0, 'end')
            c_sexo.set(0)
            c_direccion.delete(0, 'end')
            c_ciudad.delete(0, 'end')
            c_celular.delete(0, 'end')
            c_fecha_ingreso.delete(0, 'end')
            c_area_asignada.delete(0, 'end')
            var.set('Sin definir')
            var_doc.set('Sin definir')
            c_doctor_asignado.delete(0, 'end')
            verificar_cupo()

            MessageBox.showinfo("Estado", "Datos del paciente ingresados satisfactoriamente")
            conexion.close()

    conexion.close()

def eliminar():
    if(c_id.get() == ""):
        MessageBox.showinfo("Estado","El campo de cedula es obligatorio")
    else:
        conexion = mysql.connect(host="localhost", user="root", password="", database="database-patient")
        cursor = conexion.cursor()
        cursor.execute("delete from datos where id='"+ c_id.get() +"'")
        cursor.execute("commit")

        c_id.delete(0, 'end')
        c_nombres.delete(0, 'end')
        c_apellidos.delete(0, 'end')
        c_edad.delete(0, 'end')
        c_sexo.set(0)
        c_direccion.delete(0, 'end')
        c_ciudad.delete(0, 'end')
        c_celular.delete(0, 'end')
        c_fecha_ingreso.selection_clear()
        var.set('Sin definir')
        var_doc.set('Sin definir')

        verificar_cupo()
        MessageBox.showinfo("Estado", "Datos del paciente eliminados satisfactoriamente")
        conexion.close()

def actualizar():
    id = c_id.get()
    nombres = c_nombres.get()
    apellidos = c_apellidos.get()
    edad = c_edad.get()

    if c_sexo.get() == 1:
        sexo = 'H'
    else:
        sexo = 'M'

    direccion = c_direccion.get()
    ciudad = c_ciudad.get()
    celular = c_celular.get()
    fecha_ingreso = c_fecha_ingreso.get()
    area_asignada = c_area_asignada.get()

    if(id=="" or nombres=="" or apellidos=="" or edad == "" or c_sexo.get()==0 or direccion=="" or ciudad=="" or celular=="" or c_area_asignada.get()=='Sin definir'):
        MessageBox.showinfo("Update status", "Se deben diligenciar todos los datos")

    else: 
        conexion = mysql.connect(host="localhost", user="root", password="", database="database-patient")
        cursor = conexion.cursor()
        cursor.execute("select area_asignada from datos where id='"+ c_id.get() +"'")
        rows = cursor.fetchall() 

        if area_asignada == areas[0]:
            medicos_urgencias = ['Jaime Rozo',]
            var_doc.set(medicos_urgencias[0])

        elif area_asignada == areas[1]:
            medicos_cirugia = ['Paula Villa','Carlos López']
            var_doc.set(random.choice(medicos_cirugia))
        else: 
            medicos_hospitalizacion = ['Stephany Arevalo','Camilo Ortega','Diego Ortiz']
            var_doc.set(random.choice(medicos_hospitalizacion))

        doctor = c_doctor_asignado.get()
        
        print(rows)
        for row in rows: 

            if ((area_asignada == row[0]) or ((area_asignada=='Urgencias') & (cupos_urgencias < 2)) or
            ((area_asignada=='Cirugia') & (cupos_cirugia < 4)) or ((area_asignada=='Hospitalizacion') & (cupos_hospitalizacion < 46))):
                conexion = mysql.connect(host="localhost", user="root", password="", database="database-patient")
                cursor = conexion.cursor()
                cursor.execute("update datos set nombres='"+ nombres +"', apellidos='"+ apellidos +"', edad='"+ edad +"', sexo='"+ sexo +"', direccion='"+ direccion +"', ciudad='"+ ciudad +"', celular='"+ celular +"', fecha_ingreso=STR_TO_DATE('"+fecha_ingreso+"', '%d/%m/%y'), area_asignada='"+ area_asignada +"', doctor='"+ doctor +"' where id='"+ id +"'")
                cursor.execute("commit");

                c_id.delete(0, 'end')
                c_nombres.delete(0, 'end')
                c_apellidos.delete(0, 'end')
                c_edad.delete(0, 'end')
                c_sexo.set(0)
                c_direccion.delete(0, 'end')
                c_ciudad.delete(0, 'end')
                c_celular.delete(0, 'end')
                c_fecha_ingreso.delete(0, 'end')
                var.set('Sin definir')
                var_doc.set('Sin definir')

                verificar_cupo()
                MessageBox.showinfo("Estado", "Datos del paciente actualizados satisfactoriamente")
                conexion.close()

            elif((area_asignada=='Urgencias') & (cupos_urgencias==2)):
                MessageBox.showwarning("Estado", "No hay más cupo en urgencias")

            elif((area_asignada=='Cirugia') & (cupos_cirugia==4)):
                MessageBox.showwarning("Estado", "No hay más cupo en cirugía")

            elif((area_asignada=='Hospitalizacion') & (cupos_hospitalizacion==46)):
                MessageBox.showwarning("Estado", "No hay más cupo en hospitalización")

            conexion.close()

def imprimir():
    if(c_id.get() == ""):
        MessageBox.showinfo("Estado","El campo de cedula es obligatorio")

    conexion = mysql.connect(host="localhost", user="root", password="", database="database-patient")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, COUNT(*) Contador FROM datos GROUP BY id HAVING COUNT(*) = 1")
    rows = cursor.fetchall()
    
    historial_id = []
    for row in rows:
        historial_id.append(str(row[0]))

    if (c_id.get() != "") & (historial_id.count(c_id.get()) == 0): 
        MessageBox.showerror("Estado","Usuario no registrado")

    else:
        cursor.execute("select * from datos where id='"+ c_id.get() +"'")
        rows = cursor.fetchall()

        for row in rows:    
            c_nombres.insert(0, row[1])
            c_apellidos.insert(0, row[2])
            c_edad.insert(0, row[3])
            if row[4] == 'M':
                c_sexo.set(2)
            else:
                c_sexo.set(1)
            c_direccion.insert(0, row[5])
            c_ciudad.insert(0, row[6])
            c_celular.insert(0, row[7])
            c_fecha_ingreso.set_date(row[8])
            var.set(row[9])
            var_doc.set(row[10])

            conexion.close()

            if(): #Para no superponer cuando se quiere obtener nuevo usuario
                pass

def limpiar():
        c_id.delete(0, 'end')
        c_nombres.delete(0, 'end')
        c_apellidos.delete(0, 'end')
        c_edad.delete(0, 'end')
        c_sexo.set(0)
        c_direccion.delete(0, 'end')
        c_ciudad.delete(0, 'end')
        c_celular.delete(0, 'end')
        c_fecha_ingreso.delete(0, 'end')
        c_area_asignada.delete(0, 'end')
        var.set('Sin definir')
        var_doc.set('Sin definir')
        c_doctor_asignado.delete(0, 'end')

def tabla():
    ventana_tabla = tk.Toplevel(root)
    ventana_tabla.geometry("800x540")
    ventana_tabla.resizable(width=False, height=False) #Para no redimensionar

    columnas_tabla = ('id','Nombre','Apellidos','Edad','Sexo','Direccion','Ciudad','Celular','Fecha de ingreso','Area','Medico')
    tabla_datos = ttk.Treeview(ventana_tabla, columns=(1,2,3,4,5,6,7,8,9,10,11), show='headings', height=8)
    tabla_datos.pack(fill=tk.BOTH,expand=True)
    
    tabla_datos.heading(1, text = columnas_tabla[0])
    tabla_datos.heading(2, text = columnas_tabla[1])
    tabla_datos.heading(3, text = columnas_tabla[2])
    tabla_datos.heading(4, text = columnas_tabla[3])
    tabla_datos.heading(5, text = columnas_tabla[4])
    tabla_datos.heading(6, text = columnas_tabla[5])
    tabla_datos.heading(7, text = columnas_tabla[6])
    tabla_datos.heading(8, text = columnas_tabla[7])
    tabla_datos.heading(9, text = columnas_tabla[8])
    tabla_datos.heading(10, text = columnas_tabla[9])
    tabla_datos.heading(11, text = columnas_tabla[10])

    sb = Scrollbar(ventana_tabla, orient=HORIZONTAL)
    sb.pack(fill=X)

    tabla_datos.config(xscrollcommand=sb.set)
    sb.config(command=tabla_datos.xview)

    conexion = mysql.connect(host="localhost", user="root", password="", database="database-patient")
    cursor = conexion.cursor()  
    cursor.execute("select * from datos")
    rows = cursor.fetchall()

    i=0
    for row in rows:  
        tabla_datos.insert(parent='',index=i,text="",values = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
        i += 1

    conexion.close()
    root.iconify()

#***************************************************************ROOT Y FRAMES************************************************************
root = tk.Tk()
root.geometry("800x540")
root.title("iPatient App")
root.config(bg="white")
root.config(relief="groove")
root.config(bd=8)
root.resizable(width=False, height=False) #Para no redimensionar


Frame_head = Frame(root,borderwidth=5)
Frame_head.pack(side='top',fill="x")
Frame_head.config(bg="white") 
Frame_head.config(height='80') 
Frame_head.config(relief="sunken")

Frame_buttons = Frame(root)
Frame_buttons.pack(side='right',fill="y")
Frame_buttons.config(bg="snow3") 
Frame_buttons.config(width='240') 

Frame_body = Frame(root)
Frame_body.pack(side='left',fill="y")
Frame_body.config(bg="SlateGray3") 
Frame_body.config(width='540') 


#***************************************************************LABELS************************************************************
verificar_cupo()
fuente = font.Font(family="Calibri Light", size=12, weight='bold')

titulo = Label(Frame_head, text='DATOS PARA REMISIÓN DEL PACIENTE', font=fuente, bg='white', anchor='center')
titulo.pack()

id = Label(Frame_body, text='No. de identificación:',font=fuente, bg='SlateGray3')
id.place(x=20, y=30)

nombres = Label(Frame_body, text='Nombre:',font=fuente, bg='SlateGray3')
nombres.place(x=20, y=70)

apellidos = Label(Frame_body, text='Apellidos:',font=fuente, bg='SlateGray3')
apellidos.place(x=20, y=110)

edad = Label(Frame_body, text='Edad:',font=fuente, bg='SlateGray3')
edad.place(x=20, y=150)

sexo = Label(Frame_body, text='Sexo:',font=fuente, bg='SlateGray3')
sexo.place(x=20, y=190)

direccion = Label(Frame_body, text='Dirección:',font=fuente, bg='SlateGray3')
direccion.place(x=20, y=230)

ciudad = Label(Frame_body, text='Ciudad:',font=fuente, bg='SlateGray3')
ciudad.place(x=20, y=270)

celular = Label(Frame_body, text='Celular:',font=fuente, bg='SlateGray3')
celular.place(x=20, y=310)

fecha_ingreso = Label(Frame_body, text='Fecha de ingreso:',font=fuente, bg='SlateGray3')
fecha_ingreso.place(x=20, y=350)

area_asignada = Label(Frame_body, text='Área asignada:',font=fuente, bg='SlateGray3')
area_asignada.place(x=20, y=390)

doctor_asignado = Label(Frame_body, text='Doctor asignado:',font=fuente, bg='SlateGray3')
doctor_asignado.place(x=20, y=430)

#***************************************************************CAMPOS DE ENTRADA************************************************************
c_id = Entry(Frame_body, width=30)
c_id.place(x=200,y=30)

c_nombres = Entry(Frame_body,width=30)
c_nombres.place(x=200,y=70)

c_apellidos = Entry(Frame_body,width=30)
c_apellidos.place(x=200,y=110)

c_edad = Entry(Frame_body,width=10)
c_edad.place(x=200,y=150)

c_sexo = IntVar()
c_sexo.set(0)
Radiobutton(Frame_body, text='H', variable=c_sexo, value=1, bg='SlateGray3').place(x=240,y=190)
Radiobutton(Frame_body, text='M', variable=c_sexo, value=2,bg='SlateGray3').place(x=150,y=190)

# generos = ['Masculino','Femenino']
# cccc = ttk.Combobox(Frame_body,state="readonly").place(x=200,y=190)
# cccc["values"] = ["Python", "C", "C++", "Java"]
# value = cccc.get()

c_direccion = Entry(Frame_body,width=30)
c_direccion.place(x=200,y=230)

c_ciudad = Entry(Frame_body,width=30)
c_ciudad.place(x=200,y=270)

c_celular = Entry(Frame_body,width=30)
c_celular.place(x=200,y=310)

now = datetime.now()
c_fecha_ingreso = DateEntry(Frame_body, selectmode="day", textvariable=now)
c_fecha_ingreso.place(x=200,y=350)

var = tk.StringVar(Frame_body)
var.set('Sin definir')
areas = ['Urgencias','Cirugia','Hospitalizacion']
menu_area = tk.OptionMenu(Frame_body, var, *areas)
menu_area.config()

c_area_asignada = Entry(Frame_body, textvariable=var, state='readonly',readonlybackground='SlateGray3', font=fuente)
c_area_asignada_op = menu_area
c_area_asignada_op.place(x=400,y=380)
c_area_asignada.place(x=200,y=390)

var_doc = tk.StringVar(Frame_body)
var_doc.set('Sin definir')

c_doctor_asignado = Entry(Frame_body, textvariable=var_doc, state='readonly', readonlybackground='SlateGray3', font=fuente)
c_doctor_asignado.place(x=200,y=430)

#***************************************************************BUTTONS************************************************************

ingresar = Button(Frame_buttons, text="Registar",  foreground='white', background='green',relief = 'raised',font=fuente, anchor='center',width=20,command=ingresar)
ingresar.place(x=20, y=170)

eliminar = Button(Frame_buttons, text="Eliminar", foreground='white', background='red',relief = 'raised',font=fuente, anchor='center', width=20,command=eliminar)
eliminar.place(x=20, y=220)

actualizar = Button(Frame_buttons, text="Actualizar", foreground='white', background='blue',relief = 'raised',font=fuente, anchor='center', width=20, command=actualizar)
actualizar.place(x=20, y=320)

imprimir = Button(Frame_buttons, text="Obtener", foreground='white', background='blue',relief = 'raised',font=fuente, anchor='center', width=20, command=imprimir)
imprimir.place(x=20, y=370)

limpiar = Button(Frame_buttons, text="Limpiar", foreground='white', background='blue',relief = 'raised',font=fuente, anchor='center', width=20, command=limpiar)
limpiar.place(x=20, y=420)

# TABLA
tabla = Button(Frame_buttons, text="Pacientes registrados",foreground='white', background='blue',relief = 'raised',font=fuente, anchor='center', width=20, command=tabla)
tabla.place(x=20, y=270)
#tabla_datos.bind('<Double-Button-1>', imprimir)


root.mainloop()