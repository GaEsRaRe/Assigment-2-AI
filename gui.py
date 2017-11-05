# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 10:19:23 2017

@author: Gabriel PC
"""

import qtpy.QtGui as gui
import qtpy.QtWidgets as wid
import sys



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
    tab3	= wid.QWidget()
    tab4	= wid.QWidget()
    
    tabs.resize(800, 800)
    
    #Primera Tab
    tab_1	= wid.QVBoxLayout()
    pushButton1 = wid.QPushButton("Start")
    pushButton2 = wid.QPushButton("Settings")
    pushButton3 = wid.QPushButton("Stop")
    tab_1.addWidget(pushButton1)
    tab_1.addWidget(pushButton2)
    tab_1.addWidget(pushButton3)
    
    
    #Segunda Tab
    tab_2	= wid.QVBoxLayout()
    #textbox
    lx = wid.QLabel()
    lx.setText("Inserte valor en X: ")
    
    pushButton1 = wid.QPushButton("Start")
    pushButton2 = wid.QPushButton("Settings")
    pushButton3 = wid.QPushButton("Stop")
    tab_2.addWidget(lx)
    tab_2.addWidget(pushButton1)
    tab_2.addWidget(pushButton2)
    tab_2.addWidget(pushButton3)
    
    tab2.setLayout(tab_2)
    
    
     #Tercera Tab
    tab_3	= wid.QVBoxLayout()
    pushButton1 = wid.QPushButton("Start")
    pushButton2 = wid.QPushButton("Settings")
    pushButton3 = wid.QPushButton("Stop")
    tab_3.addWidget(pushButton1)
    tab_3.addWidget(pushButton2)
    tab_3.addWidget(pushButton3)
    tab3.setLayout(tab_3)
    
    #Cuarta Tab
    
    
    ## information
    l1 = wid.QLabel()
    l1.setText("Agrega la cantidad de puntos hasta que desee generar el spline")
    l1.setGeometry(200, 200, 600, 600)
    tab_1.addWidget(l1)
    tab1.setLayout(tab_1)   
    # Add tabs
    tabs.addTab(tab1,"Introduccion")
    tabs.addTab(tab2,"Sistema Experto")
    tabs.addTab(tab3,"enfermedades y sintomas")
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