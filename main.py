from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

def borrar():
    print("entro")
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comidas[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

def revisar_check_bebidas():
    x = 0
    for c in cuadros_bebida:
        if variables_bebidas[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

def revisar_check_postre():
    x = 0
    for c in cuadros_postre:
        if variables_postres[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0,END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.21
    total = sub_total + impuestos

    var_costo_comida.set(f'{round(sub_total_comida,2)} €')
    var_costo_bebida.set(f'{round(sub_total_bebida,2)} €')
    var_costo_postre.set(f'{round(sub_total_postre,2)} €')
    var_subtotal.set(f'{round(sub_total,2)} €')
    var_impuestos.set(f'{round(impuestos,2)} €')
    var_total.set(f'{round(total,2)} €')

def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos: \t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END,f'*' * 75 +'\n')
    texto_recibo.insert(END,'Comida\t\tCant. \tCosto comida\n')
    texto_recibo.insert(END, f'-' * 90 + '\n')
    x=0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END,f'{lista_comida[x]}\t\t{comida.get()}\t'
                                    f' {int(comida.get()) * precios_comida[x]} €\n')
        x +=1
    x = 0
    for comida in texto_bebida:
        if comida.get() != '0':
            texto_recibo.insert(END,f'{lista_bebida[x]}\t\t{comida.get()}\t'
                                    f' {int(comida.get()) * precios_bebida[x]} €\n')
        x +=1
    x = 0
    for comida in texto_postre:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_postre[x]}\t\t{comida.get()}\t'
                                     f' {int(comida.get()) * precios_postres[x]} €\n')
        x += 1
    texto_recibo.insert(END, f'-' * 90 + '\n')
    texto_recibo.insert(END, f'Precio de comida:\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Precio de bebida:\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Precio de postres:\t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 90 + '\n')
    texto_recibo.insert(END, f'Sin IVA:\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'IVA 21%:\t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total:\t\t\t{var_total.get()}\n')

def guardar():
    info_recibo = texto_recibo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información','Recibo guardado')

def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for c in variables_comidas:
        c.set(0)
    for c in variables_bebidas:
        c.set(0)
    for c in variables_postres:
        c.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')

aplicacion = Tk()

aplicacion.iconbitmap('icono\\palillos.ico')
aplicacion.geometry('1220x630+0+0')
#aplicacion.geometry('1020x630+0+0')

aplicacion.resizable(0,0)

aplicacion.title('Sistema de facturacion')

aplicacion.config(bg='burlywood')

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

etiqueta_titulo = Label(panel_superior, text='Sistema de facturacion', fg='azure4', font=('Dosis',58),bg='burlywood',width=23)

etiqueta_titulo.grid(row=0,column=0)

#panel izquierda
panel_izquierdo = Frame(aplicacion,bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo,bd=1, relief=FLAT,bg='azure4',padx=80)
panel_costos.pack(side=BOTTOM)

#panel_comidas
panel_comidas = LabelFrame(panel_izquierdo,text='Comida',font=('Dosis',19,'bold'), bd=1, relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)

#panel_bebidas
panel_bebidas = LabelFrame(panel_izquierdo,text='Bebidas',font=('Dosis',19,'bold'), bd=1, relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel_postres
panel_postres = LabelFrame(panel_izquierdo,text='Postres',font=('Dosis',19,'bold'), bd=1, relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)

#panel_derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

#panel_calculadora
panel_calculadora = Frame(panel_derecho,bd=1,relief=FLAT,bg='burlywood')
panel_calculadora.pack()

#panel_recibo
panel_recibo = Frame(panel_derecho,bd=1,relief=FLAT,bg='burlywood')
panel_recibo.pack()

#panel_botones
panel_botones = Frame(panel_derecho,bd=1,relief=FLAT,bg='burlywood')
panel_botones.pack()

# Productos
lista_comida = ['arroz','pollo','cerdo','ternera','tallarines','pato','plato 2','plato 3']
lista_bebida = ['fanta','cola','cerveza','tinto','vino','agua','refresco 2','refresco 3']
lista_postre = ['helado 1','helado 2','helado 3','helado 4','helado 5','helado 6','helado 7','helado 8']


variables_comidas = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comida:
    #crea los check
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis',19,'bold'), onvalue=1,offvalue=0,variable=variables_comidas[contador],command=revisar_check)
    comida.grid(row=contador,column=0,sticky=W)

    #crear los textfielt
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

variables_bebidas = []
cuadros_bebida = []
texto_bebida = []
contador2 = 0
for comida in lista_bebida:

    variables_bebidas.append('')
    variables_bebidas[contador2] = IntVar()
    comida = Checkbutton(panel_bebidas, text=comida.title(), font=('Dosis',19,'bold'), onvalue=1,offvalue=0,variable=variables_bebidas[contador2],command=revisar_check_bebidas)
    comida.grid(row=contador2,column=0,sticky=W)

    # crear los textfielt
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador2] = StringVar()
    texto_bebida[contador2].set('0')
    cuadros_bebida[contador2] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador2])
    cuadros_bebida[contador2].grid(row=contador2,
                                  column=1)
    contador2 += 1

variables_postres = []
cuadros_postre = []
texto_postre = []
contador3 = 0
for comida in lista_postre:
    variables_postres.append('')
    variables_postres[contador3] = IntVar()
    comida = Checkbutton(panel_postres, text=comida.title(), font=('Dosis',19,'bold'), onvalue=1,offvalue=0,variable=variables_postres[contador3],command=revisar_check_postre)
    comida.grid(row=contador3,column=0,sticky=W)

    # crear los textfielt
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador3] = StringVar()
    texto_postre[contador3].set('0')
    cuadros_postre[contador3] = Entry(panel_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postre[contador3])
    cuadros_postre[contador3].grid(row=contador3,
                                   column=1)
    contador3 += 1


#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# etiqueta de coste y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Coste comida',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=1,
                           column=0)

texto_coste_comida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_coste_comida.grid(row=1,column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Coste bebida',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=2,
                           column=0)

texto_coste_bebida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_coste_bebida.grid(row=2,column=1, padx=41)

etiqueta_costo_postre= Label(panel_costos,
                              text='Coste postre',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=3,
                           column=0)

texto_coste_postre = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_coste_postre.grid(row=3,column=1, padx=41)

etiqueta_subtotal= Label(panel_costos,
                              text='sin IVA',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=1,column=3)

texto_coste_subtotal = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_coste_subtotal.grid(row=1,column=4, padx=41)

etiqueta_impuestos= Label(panel_costos,
                              text='IVA 21',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuestos.grid(row=2,column=3)

texto_coste_impuestos = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_coste_impuestos.grid(row=2,column=4, padx=41)

etiqueta_total= Label(panel_costos,
                              text='total',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=3,column=3)

texto_coste_total = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_coste_total.grid(row=3,column=4, padx=41)

#botones
botones = ['total','recibo','guardar','resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',14,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9
                   )
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas +=1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

#area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=51,
                    height=10)
texto_recibo.grid(row=0,column=0)

#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis',16,'bold'),
                          width=40,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7','8','9','+','4','5','6','-',
                       '1','2','3','*','R','B','0','/']
botonesParaCalcular= []

fila = 1
columna = 0
n = 0
for x in range(1,5):
    for y in range(0,4):
        boton = Button(panel_calculadora,
                       text=botones_calculadora[n].title(),
                       font=('Dosis',16,'bold'),
                       fg='white',
                       bg='azure4',
                       bd=1,
                       width=8)
        botonesParaCalcular.append(boton)
        boton.grid(row=x,
                   column=y)
        n +=1

botonesParaCalcular[0].config(command=lambda: click_boton(botones_calculadora[0].title()))
botonesParaCalcular[1].config(command=lambda: click_boton(botones_calculadora[1].title()))
botonesParaCalcular[2].config(command=lambda: click_boton(botones_calculadora[2].title()))
botonesParaCalcular[3].config(command=lambda: click_boton(botones_calculadora[3].title()))
botonesParaCalcular[4].config(command=lambda: click_boton(botones_calculadora[4].title()))
botonesParaCalcular[5].config(command=lambda: click_boton(botones_calculadora[5].title()))
botonesParaCalcular[6].config(command=lambda: click_boton(botones_calculadora[6].title()))
botonesParaCalcular[7].config(command=lambda: click_boton(botones_calculadora[7].title()))
botonesParaCalcular[8].config(command=lambda: click_boton(botones_calculadora[8].title()))
botonesParaCalcular[9].config(command=lambda: click_boton(botones_calculadora[9].title()))
botonesParaCalcular[10].config(command=lambda: click_boton(botones_calculadora[10].title()))
botonesParaCalcular[11].config(command=lambda: click_boton(botones_calculadora[11].title()))
botonesParaCalcular[12].config(command=obtener_resultado)
botonesParaCalcular[13].config(command=borrar)
botonesParaCalcular[14].config(command=lambda: click_boton(botones_calculadora[14].title()))
botonesParaCalcular[15].config(command=lambda: click_boton(botones_calculadora[15].title()))




aplicacion.mainloop()
