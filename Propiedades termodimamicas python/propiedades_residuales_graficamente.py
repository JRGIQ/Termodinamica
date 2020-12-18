# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:23:07 2018

@author: Jheison Gutierrez
"""

### ESTE PROGRAMA CALCULAR ΔG,ΔH,ΔS, RESIDUALES 

import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
from sympy import Symbol
from sympy import integrate
from scipy.integrate import quad

#### GRAFICA FACTOR DE COMPRESIBILIDAD EN FUNTCION DE T.

class propiedades_residuales():
    
    def datos_sistema(self):
        self.R=8.315 #J/mol*K
        self.presion=[0.1,0.5,2,4,6,8,10,12,14,15.41]
        self.temperatura=[340,350,360,370,380]
        self.factorZ_360K=[0.99737,0.98907,0.96483,0.93635,0.90734,0.87586,0.84077,0.80103,0.75506,0.71727]
        self.factorZ1=[0.997,0.99719,0.99737,0.99753,0.99767]
        self.factorZ2=[0.9874,0.9883,0.98907,0.98977,0.9904]
        self.factorZ3=[0.95895,0.96206,0.96483,0.9673,0.96953]
        self.factorZ4=[0.92422,0.93069,0.93635,0.94132,0.94574]
        self.factorZ5=[0.88742,0.89816,0.90734,0.91529,0.92223]
        self.factorZ6=[0.84575,0.86218,0.87586,0.88745,0.89743]
        self.factorZ7=[0.79659,0.82117,0.84077,0.85695,0.87061]
        self.factorZ8=[0.7731,0.80103,0.82315,0.84134]
        self.factorZ9=[0.75506,0.78531,0.80923]
        self.factorZ10=[0.71727]
        self.Z_1=[0.0263,0.02186,0.017585,0.0159125,0.015443333,0.0155175,0.015923,0.016580833,0.017495714,0.018347177]
        self.Testandar=298.15
        self.T=float(input("ingrese la temperatura T de interes para evaluar H residual (K) : "))
        self.tao=self.T/self.Testandar
        self.A=1.7765
        self.B=33.037e-03
        self.C=0
        self.D=0
        
        
    def grafica_temperatura_vs_factorZ(self):

        pt.plot(self.temperatura,self.factorZ1,'ko--',linewidth = 2,label="P=0.1bar")
        pt.plot(self.temperatura,self.factorZ2,'go--',linewidth = 2,label="P=0.5bar")
        pt.plot(self.temperatura,self.factorZ3,'ro--',linewidth = 2,label="P=2bar")
        pt.plot(self.temperatura,self.factorZ4,'bo--',linewidth = 2,label="P=4bar")
        pt.plot(self.temperatura,self.factorZ5,'yo--',linewidth = 2,label="P=6bar")
        pt.plot(self.temperatura,self.factorZ6,'r^--',linewidth = 2,label="P=8bar")
        pt.plot(self.temperatura,self.factorZ7,'b^--',linewidth = 2,label="P=10bar")
        pt.plot(self.temperatura[1:5],self.factorZ8,'y^--',linewidth = 2,label="P=12bar")
        pt.plot(self.temperatura[2:5],self.factorZ9,'k^--',linewidth = 2,label="P=14bar")
        pt.plot(self.temperatura[2],self.factorZ10,'b*--',linewidth = 2,label="P=15.41bar")
        pt.xlabel('Temperatura')
        pt.ylabel('Factor de compresibilidad')
        pt.grid(True)
        leg = pt.legend(loc='lower right', ncol=1, mode="center", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.7)
        pt.show()
        print("---------------------------------------------------------------")
        
    def polinomio_interpolante_TvsZ(self):
        self.coeficientes1=np.polyfit(self.temperatura,self.factorZ1,2)
        self.polinomio2=np.poly1d(self.coeficientes1)
        print("El polinomio interpolante de grado 3 Z=f(T) es: ",self.polinomio2)
        print("----------------------------------------------------------------")  
        
    def derivada_dZ_dT(self):  ### derivada sin evaluar
        x=Symbol('x')
        self.Z_fT=-8.571e-08 *x**2 + 7.851e-05* x + 0.9802
        print("La derivada dZ/dT es: ",self.Z_fT.diff(x))
        print("----------------------------------------------------------------")
        
    def calculo_derivada_dZ_dT(self): ##  (dZ/dT)/P  ###derivada evaluada en este caso a 360K        
       
        self.dZ1_dT=1.7142e-7*self.T + 7.851e-5
        print("La derivada evaluada en T=360 K es: ",self.dZ1_dT)
        print("----------------------------------------------------------------")
        
    def grafica_derivada_vs_presion(self):
        self.dZ_P=((self.dZ1_dT)/(np.array(self.presion)))
        pt.xlabel('Presion')
        pt.ylabel('(dZ/dT)/P')
        pt.title('Presion VS (dZ/dT)/P')
        pt.grid()
        
        pt.plot(self.presion,self.dZ_P)
        print("Los valores de (dZ/dT)/P f(P) son: ",self.dZ_P)
        pt.show()
        print("-----------------------------------------------------------------") 
        
    def polinomio_interpolante_dZ_dT_fP(self):
        self.coeficientes2=np.polyfit(self.presion,self.dZ_P,3)
        self.polinomio2=np.poly1d(self.coeficientes2)
        print("El polinomio interpolante dZ/dT f(P) es: ",self.polinomio2)
        print("----------------------------------------------------------------")
        
    def integral_polinomio_interpolante_dZ_dT_fP(self):  ####integral de (dZ/dT)/P
        x=Symbol('x')
        print("la integral del polinomio interpolante (dz/dT)/P) es: ",integrate(-4.422e-06 *x**3 + 0.0001229 *x**2 - 0.001003 *x + 0.002261))
        print("----------------------------------------------------------------")
        g=lambda x:-4.422e-06*x**3 + 0.0001229* x**2 - 0.001003 *x + 0.002261
        self.integral1=quad(g,0,15.41)
        print("El valor de la integral evaluada desde P0 a P (dZ/dT)/P es: ",self.integral1)
        print("----------------------------------------------------------------")
        
 #*****************************************************************************************************#       

    def grafica_Z_vs_P(self):
        pt.title('Grafica P  VS (Z-1)/P ')
        pt.xlabel('presion')
        pt.ylabel('factor de compresibilidad')
        pt.grid(True)
        leg = pt.legend(loc='lower right', ncol=1, mode="center", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.7)        
        pt.plot(self.presion,self.Z_1,'k*--',linewidth = 2,label="Z-1/P  vs  P")
        pt.show()
        print("----------------------------------------------------------------")
        
    def polinomio_interpolante_PvsZ(self):
        
        self.coeficientes=np.polyfit(self.presion,self.Z_1,3)
        self.polinomio=np.poly1d(self.coeficientes)
        print("El polinomio interpolante z-1/P f(P) es: ",self.polinomio)
        print("----------------------------------------------------------------")           
        
                          
        
    def integral_polinomio_interpolante_PvsZ(self):
        x=Symbol('x')
        print("La integral del polinomio interpolante es: ",integrate(-1.32e-05* x**3 + 0.0004145* x**2 - 0.003711 *x + 0.02486,x))
        print("-----------------------------------------------------------------")
        f=lambda x:-(-1.32e-05* x**3 + 0.0004145 *x**2 - 0.003711 *x + 0.02486)
        self.integral=quad(f,0.,15.41)
        print("el valor de la integral (Z-1) dp/P y el error es: ",self.integral)
        print("----------------------------------------------------------------")

### PARA EL CALCULO DE Hr/RT y Sr/R
        
    def calculo_H_residual(self):
    
        self.Hr=-self.T*np.array(self.integral1[0])
        print("El valor de la Entalpia residual Hr/RT (J/mol*K) es: ",self.Hr)
        print("-----------------------------------------------------------------")

        
    def calculo_S_residual(self):
        self.Sr=self.Hr-self.integral[0]
        print("El valor de la entropia residual (J/mol*K) Sr/R es: ",self.Sr)
        print("----------------------------------------------------------------")
        
    def integral_Cp_R(self):
        self.Cp_R=(self.A+(self.B*0.5*self.Testandar*(self.tao+1))+((self.C/3)*self.Testandar**2*(self.tao**2+self.tao+1))+((self.D)/(self.tao*self.Testandar**2)))*(self.T-self.Testandar)
        self.Cp=8.314*self.Cp_R
        print("La integral de capacidad calorifica Cp/R J/mol Cp es: ",self.Cp)
        print("----------------------------------------------------------------")
        
        
        
    
            
        
# integral(dZ/dT)dp/P) para el calculo de entalpia residual
       
       
a=propiedades_residuales()
a.datos_sistema()
a.grafica_temperatura_vs_factorZ()
a.polinomio_interpolante_TvsZ()
a.derivada_dZ_dT()
a.calculo_derivada_dZ_dT()
a.grafica_derivada_vs_presion()
a.polinomio_interpolante_dZ_dT_fP()
a.integral_polinomio_interpolante_dZ_dT_fP()
a.calculo_H_residual()

 ##     INTEGRAL (z-1)dP/P   para el calculo de entropia residual
#a.grafica_Z_vs_P()
#a.polinomio_interpolante_PvsZ()
#a.integral_polinomio_interpolante_PvsZ()
#a.calculo_S_residual()
#a.integral_Cp_R()
        
        
        


