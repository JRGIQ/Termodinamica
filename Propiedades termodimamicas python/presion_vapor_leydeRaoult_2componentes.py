# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:42:55 2018

@author: Jheison Gutierrez
"""
#### Este programa grafica la (presion y/o temperatura) vs la composicion(liquida o vapor) para sistemas bicomponentes.

import math as mt
import matplotlib.pyplot as pt
import numpy as np


class presion_vapor():
    
    def variables(self):
        self.T=float(input("ingrese la temperatura del sistema en °C :"))
        self.A1=14.2724#float(input("ingrese la constante A de Antoine para la sustancia 1(mas volatil) :"))
        self.B1=2945.47#float(input("ingrese la constante B de Antoine para la sustancia 1(mas volatil) :"))
        self.C1=224#float(input("ingrese la constante C de Antoine para la sustancia 1(mas volatil) :"))
        self.A2=14.2043#float(input("ingrese la constante A de Antoine para la sustancia 2(menos volatil) :"))
        self.B2=2972.64#float(input("ingrese la constante B de Antoine para la sustancia 2(menos volatil) :"))
        self.C2=209#float(input("ingrese la constante  de Antoine para la sustancia 2(menos volatil) :"))
        self.X1=np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
               
              
    def presion_saturacion(self):  #### de acuerdo a la ecuacion de antoine pag 352 smith,van ness
        self.Ps1=mt.exp(self.A1-((self.B1)/(self.T+self.C1)))
        self.Ps2=mt.exp(self.A2-((self.B2)/(self.T+self.C2)))
        print("la presion de saturacion Ps1 en Kpa es :",self.Ps1)
        print("----------------------------------------------------------------")
        print("la presion de saturacion Ps2 en Kpa es :",self.Ps2)
        print("----------------------------------------------------------------")
        
        
    def funcion_PvsX1(self):
        self.P=self.Ps2+((self.Ps1-self.Ps2)*self.X1)  ##### en funcion de la mas volatil X1
               
        
    def grafica_PvsX1(self):
        pt.xlabel('composicion')
        pt.ylabel('presion P')
        pt.grid(True)
        pt.title(' PRESION VS COMPOSICION')
        pt.plot(self.X1,self.P,'k',linewidth=2,label="fase liquida")
        
    def grafica_PvsY1(self):
        self.Y1=((self.X1*self.Ps1)/(self.P))
        pt.xlabel('Composicion X1,Y1')
        pt.ylabel('Presion P Kpa')
        pt.grid(True)
        pt.title(' PRESION VS COMPOSICION')
        pt.plot(self.Y1,self.P,'b',linewidth=2,label="fase vapor")
        leg = pt.legend(loc='lower right', ncol=1, mode="center", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.7)
        pt.show()
        
        
        
presion=presion_vapor()
presion.variables()
presion.presion_saturacion()
presion.funcion_PvsX1()
presion.grafica_PvsX1()
presion.grafica_PvsY1()
        
        
        
        
#####################################################################################################################
#####################################################################################################################
        
class temperatura_saturacion():
    
    def variables(self):
        
        self.P=float(input("ingrese la presion del sistema en KPa :"))
        self.A1=14.2724#float(input("ingrese la constante A de Antoine para la sustancia 1(mas volatil) :"))
        self.B1=2945.47#float(input("ingrese la constante B de Antoine para la sustancia 1(mas volatil) :"))
        self.C1=224#float(input("ingrese la constante C de Antoine para la sustancia 1(mas volatil) :"))
        self.A2=14.2043#float(input("ingrese la constante A de Antoine para la sustancia 2(menos volatil) :"))
        self.B2=2972.64#float(input("ingrese la constante B de Antoine para la sustancia 2(menos volatil) :"))
        self.C2=209#float(input("ingrese la constante  de Antoine para la sustancia 2(menos volatil) :"))
    
    def temp_saturacion(self):
        self.Ts1=((self.B1)/(self.A1-mt.log(self.P)))-self.C1
        self.Ts2=((self.B2)/(self.A2-mt.log(self.P)))-self.C2
        print("La temperatura de saturacion Ts1 en °C es :",self.Ts1)
        print("----------------------------------------------------------------")
        print("La temperatura de saturacion Ts2 en °C es :",self.Ts2)
        print("----------------------------------------------------------------")
        
    def intervalo_temperaturas(self):
       self.T=np.array(range(int(self.Ts1),int(self.Ts2+2)))

    def presion_saturacion(self):  #### de acuerdo a la ecuacion de antoine pag 352 smith,van ness
        self.LnPs1=(self.A1-((self.B1)/(self.T+self.C1)))
        self.LnPs2=(self.A2-((self.B2)/(self.T+self.C2)))
        self.Ps1=np.exp(self.LnPs1)
        self.Ps2=np.exp(self.LnPs2)
#        print("la presion de saturacion Ps1 en Kpa es :",self.Ps1)
#        print("----------------------------------------------------------------")
#        print("la presion de saturacion Ps2 en Kpa es :",self.Ps2)
#        print("----------------------------------------------------------------")
        
    def composicion_X1(self):
        self.X1=((self.P-self.Ps2)/(self.Ps1-self.Ps2))
        
    def composicion_Y1(self):
        self.Y1=((self.X1*self.Ps1)/(self.P))
        
    def grafica_TvsX1(self):
        pt.plot(self.X1,self.T,'k',linewidth=2,label="fase liquida")
        
        
    def grafica_TvsY1(self):
        pt.plot(self.Y1,self.T,'b',linewidth=2,label="fase vapor")
        pt.grid(True)
        pt.xlabel('Composicion X1,Y1')
        pt.ylabel('Temperatura K')
        pt.title('Temperatura vs Composicion')
        leg = pt.legend(loc='upper right', ncol=1, mode="center", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.7)
        
        
        
temp=temperatura_saturacion()
temp.variables()
temp.temp_saturacion()
temp.intervalo_temperaturas()
temp.presion_saturacion()
temp.composicion_X1()
temp.composicion_Y1()   
temp.grafica_TvsX1()
temp.grafica_TvsY1()
        
        
        
        
        
        
        
        