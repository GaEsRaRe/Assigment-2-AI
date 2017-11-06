# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 10:19:23 2017

@author: Gabriel PC
"""

import qtpy.QtGui as gui
import qtpy.QtWidgets as wid
import sys
import logic as lg
import numpy as np


def exist(ar,val): #Detect if X value already exist
    answer = False
    size = np.size(ar,0)
    for i in range(0,size):
        if ar[i][0] == val:
            answer = True
    return answer

def window():
    # Variables
    
    app 	= wid.QApplication(sys.argv)
    tabs	= wid.QTabWidget()
    
    # Create tabs
    tab1	= wid.QWidget()	
    tab2	= wid.QWidget()
    tab4	= wid.QWidget()
    
    tabs.resize(1200, 800)
    
    #Primera Tab
    tab_1 = wid.QVBoxLayout()
    licence = ( "Trabajo de Inteligencia Artificial" +
              " \n Sistema experto para la deteccion de transtornos psicologicos mas comunes"+
              "\n \n Alumnos: \n" +
              "Gabriel Ramirez Reategui \n" +
              "Ricardo Andre Bueno Carrasco \n" +
              "Franco Pastor  \n"
              )
    text0 = wid.QLabel(licence)
    text0.setWordWrap(True)
    tab_1.addWidget(text0)
    tab1.setLayout(tab_1)
    
    
    #Segunda Tab
    tab_2	= wid.QGridLayout()
    #textbox
    lx = wid.QLabel()
    lx.setText("Nombre del Paciente:")
    
    tb = wid.QLineEdit()
    tab_2.addWidget(tb,0,4)
    pushButton1 = wid.QPushButton("Usar S.E.")
    
    tab_2.addWidget(lx,0,3)
    checkboxs = []
    checkboxs.append(wid.QCheckBox("preocupacion_por_imagen"))
    checkboxs.append(wid.QCheckBox("perdida_de_interes"))
    checkboxs.append(wid.QCheckBox("dificultad_respiracion"))
    checkboxs.append(wid.QCheckBox("robos_sin_ganancia"))
    checkboxs.append(wid.QCheckBox("necesidad_orinar_o_defecar"))
    checkboxs.append(wid.QCheckBox("humor_depresivo_anormal"))
    checkboxs.append(wid.QCheckBox("alucinaciones_persistenes"))
    checkboxs.append(wid.QCheckBox("incapacidad_recordar_acontecimiento"))
    checkboxs.append(wid.QCheckBox("transtorno_endocrino"))
    checkboxs.append( wid.QCheckBox("autoinduccion_perdida_peso"))
    checkboxs.append( wid.QCheckBox("escalofrios"))
    checkboxs.append( wid.QCheckBox("intencion_de_resistencia"))
    checkboxs.append( wid.QCheckBox("bajo_peso"))
    checkboxs.append( wid.QCheckBox("obsesiones"))
    checkboxs.append( wid.QCheckBox("pensamientos_suicidas"))
    checkboxs.append( wid.QCheckBox("ideas_de_control"))
    checkboxs.append( wid.QCheckBox("sequedad_boca"))
    checkboxs.append( wid.QCheckBox("jugar_sin_provecho_economico"))
    checkboxs.append( wid.QCheckBox("discurso_incoherente"))
    checkboxs.append( wid.QCheckBox("dolor_pecho"))
    checkboxs.append( wid.QCheckBox("compulsiones"))
    checkboxs.append( wid.QCheckBox("sensacion_ahogo"))
    checkboxs.append( wid.QCheckBox("preocupacion_por_juego"))
    checkboxs.append( wid.QCheckBox("miedo_muerte"))
    checkboxs.append( wid.QCheckBox("disminucion_de_energia"))
    checkboxs.append(wid.QCheckBox("agitacion_o_enlentecimiento"))
    checkboxs.append(wid.QCheckBox("alivio_de_tension_al_robar"))
    checkboxs.append(wid.QCheckBox("disgusto"))
    checkboxs.append(wid.QCheckBox("hormigueo"))
    checkboxs.append(wid.QCheckBox("distorcion_imagen_corporal"))
    checkboxs.append(wid.QCheckBox("ideas_de_poder"))
    checkboxs.append(wid.QCheckBox("temblores"))
    checkboxs.append(wid.QCheckBox("recuerdos_recurrentes_acontecimiento"))
    checkboxs.append(wid.QCheckBox("repitencia_perjudicial"))
    checkboxs.append(wid.QCheckBox("alteracion_de_sueno"))
    checkboxs.append(wid.QCheckBox("indecision"))
    checkboxs.append(wid.QCheckBox("enfermedad"))
    checkboxs.append(wid.QCheckBox("miedo_social"))
    checkboxs.append(wid.QCheckBox("miedo_multitudes"))
    checkboxs.append(wid.QCheckBox("cambio_apetito"))
    checkboxs.append(wid.QCheckBox("evitacion_similar_recuerdo"))
    checkboxs.append(wid.QCheckBox("hipersensibilidad_psicologica"))
    checkboxs.append(wid.QCheckBox("miedo_humillacion"))
    checkboxs.append(wid.QCheckBox("conductas_catatonicas"))
    checkboxs.append(wid.QCheckBox("miedo_humillacion"))
    checkboxs.append(wid.QCheckBox("miedo_vomitar"))
    checkboxs.append(wid.QCheckBox("miedo_humillacion"))
    checkboxs.append(wid.QCheckBox("o_c_reiteradas_y_desagradables"))
    checkboxs.append(wid.QCheckBox("sudoracion"))
    checkboxs.append(wid.QCheckBox("palpitaciones"))
    checkboxs.append(wid.QCheckBox("situacion_extrema_estres"))
    checkboxs.append(wid.QCheckBox("miedo_viajar_lejos"))
    checkboxs.append(wid.QCheckBox("impulso_robar"))
    checkboxs.append(wid.QCheckBox("miedo_viajar_solo"))
    checkboxs.append(wid.QCheckBox("sintomas_negativos"))
    checkboxs.append(wid.QCheckBox("miedo_lugares_publicos"))
    checkboxs.append(wid.QCheckBox("perdida_de_confianza"))
    checkboxs.append(wid.QCheckBox("ruborizacion"))
    checkboxs.append(wid.QCheckBox("ideas_delirantes"))
    checkboxs.append(wid.QCheckBox("impulso_de_jugar"))
    checkboxs.append(wid.QCheckBox("mareos"))
    checkboxs.append(wid.QCheckBox("preocupacion_por_peso"))
    checkboxs.append(wid.QCheckBox("alteracion_del_pensamiento"))
    checkboxs.append(wid.QCheckBox("incapacidad_dejar_jugar"))
    checkboxs.append(wid.QCheckBox("culpa_excesiva"))
    checkboxs.append(wid.QCheckBox("preocupacion_por_peso"))
    checkboxs.append(wid.QCheckBox("miedo_atencion"))
    
    #we add all the checkboks
    for i in range(0,3):
        for n in range(0,22):
            tab_2.addWidget(checkboxs[n + i*22],n,i)
    tab_2.addWidget(checkboxs[66],21,3)
    
    
    tab2.setLayout(tab_2)
    
    def selector():
        #for i in range(0,np.size(checkboxs,0)):
        value = tb.text()
        print(value)
        for i in range(0,np.size(checkboxs,0)):
            if(checkboxs[i].isChecked()):
                print("Se ha agregado: ", checkboxs[i].text())
                lg.A.add_rule(checkboxs[i].text(),value)
        
        a = lg.tiene_depresion(value)
        b = lg.tiene_esquizofrenia(value)
        c = lg.tiene_toc(value)
        d = lg.tiene_fobia_social(value)
        e = lg.tiene_agorafobia(value)
        f = lg.tiene_anorexia(value)
        g = lg.tiene_cleptomania(value)
        h = lg.tiene_ludopatia(value)
        i = lg.tiene_pos_traumatico(value)
        print(c)
        text = "Los resultados son: "+(a*"Depresion" + " " + b*"esquizofrenia " + c*"toc "+ d*"Fobia Social " + e*"agorafobia " + f*"anorexia" + g*"cleptomania " + h*"ludopatia " + i*"Estres postraumatico")
        msg = wid.QMessageBox()
        msg.setIcon(wid.QMessageBox.Information)
        msg.setText("Usted puede tener las siguientes enfermedades: ")
        msg.setWindowTitle("Resultado")
        msg.setDetailedText(text)
        msg.exec_()
        pass
    
    pushButton1.clicked.connect(selector)
    #Cuarta Tab
    
    tab_4 = wid.QVBoxLayout()
    licence = ( "El sistema experto asi como el codigo del mismo se libera bajo la licencia de codigo Abierto para cualquier persona pueda leer, modificar y reutilizar el codigo" +
              " \n Este software fue desarrollado en conjunto por los alumnos de la universidad de ciencias aplicadas"+
              " para el curso de Inteligencia Artificial de la carrera de Ciencias de la Computacion" +
              "\n \n Alumnos: \n" +
              "Gabriel Ramirez Reategui \n" +
              "Ricardo Andre Bueno Carrasco \n" +
              "Franco Pastor  \n"
              )
    text1 = wid.QLabel(licence)
    text1.setWordWrap(True)
    tab_4.addWidget(text1)
    tab4.setLayout(tab_4)
    
    
    ## information
    l1 = wid.QLabel()
    l1.setText("Entrar a la tabla Sistema Experto, seleccionar sintomas y hacer clic en S.E para probar, no olvidar poner nombre")
    l1.setGeometry(200, 200, 600, 600)
    tab_1.addWidget(l1)
    tab1.setLayout(tab_1)   
    # Add tabs
    tabs.addTab(tab1,"Introduccion")
    tabs.addTab(tab2,"Sistema Experto")
    tabs.addTab(tab4,"licencia") 
    
    
 
    # Titulos e informacion
    tabs.setWindowTitle('Trabajo de Inteligencia Artificial: Sistema experto para Enfermedades mentales mas comunes')
    tabs.show()
    sys.exit(app.exec_())

"""    
    data = []
    txt = ""
    app = wid.QApplication(sys.argv)
    w = wid.QWidget()
    w.setGeometry(200, 200, 600, 600)
    w.setWindowTitle("Trabajo de Inteligencia Artificial 2")
    # Labels and text

    #Message box
    

    # Title
    l = wid.QLabel(w)
    l.setText("Trabajo de Algebra Lineal!")
    l.move(170, 50)
    l.setFont(gui.QFont('SansSerif', 20))

    # information
    l1 = wid.QLabel(w)
    l1.setText("Agrega la cantidad de puntos hasta que desee generar el spline")
    l1.move(30, 100)

    # Textbox
    lx = wid.QLabel(w)
    lx.setText("Inserte valor en X: ")
    lx.move(10, 120)
    tx = wid.QLineEdit(w)
    tx.setGeometry(130, 115, 50, 20)

    ly = wid.QLabel(w)
    ly.setText("Inserte valor en Y: ")
    ly.move(10, 150)
    ty = wid.QLineEdit(w)
    ty.setGeometry(130, 145, 50, 20)


    # Functions to add
    def fill():
      
        pass
    labels =wid.QLabel(w)
    labels.setGeometry(30, 130, 600, 300)

        # Boton 1
    def clear():
        print("working")
        
    bta = []
    bta.append(wid.QPushButton(w))
    bta[0].setText("agregar valor!")
    bta[0].move(200, 140)
    bta[0].clicked.connect(fill)
    
    #btn 2
    bta.append(wid.QPushButton(w))
    bta[1].setText("Generar Spline!")
    bta[1].move(300, 140)

    bta.append(wid.QPushButton(w))
    bta[2].setText("Limpiar valores")
    bta[2].move(400, 140)
    bta[2].clicked.connect(clear)
    
    w.show()

"""
   

if __name__ == '__main__':
    window()