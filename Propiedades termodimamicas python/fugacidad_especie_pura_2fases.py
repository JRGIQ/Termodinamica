# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:58:09 2019

@author: Jheison Gutierrez
"""
   ## EL PROGRAMA CALCULA LA FUGACIDAD Y SU COEFICIENTE PARA UNA ESPECIE PURA (LIQUIDO O VAPOR)
   
   
   
   
#### ESTE PROGRAMA CALCULA fi,Φi,Zi,Vi PARA UNA SUSTANCIA PURA EN FASE DE VAPOR

import math as mt
import numpy as np
import matplotlib.pyplot as pt


##### NOTA: para usar el programa primero verificar el estado de la sustancia P<Psat (vapor), P>Psat (liquido)

class fugacidad_y_coeficiente():
    
    
    def variables(self):
        self.T=573.15#input(float("ingrese la temperatura del sistema K : "))
        self.Ts=300#input(float("ingrese la temperatura del sistema en °C : "))
        self.P=10000#input(float("ingrese la presion del sistema Kpa : "))
        self.R=8.314 # J/Kmol*K
        self.w=0.345#input(float("ingrese el factor acentrico : "))
        self.Tc=647.1#input(float("ingrese la temperatura critica de la sustancia (K) : "))
        self.Pc=22055#input(float("ingrese la presion critica de la sustancia Kpa : "))
        self.A=16.3872#float(input("ingrese la constante A de Antoine para la sustancia :"))
        self.B=3885.70#float(input("ingrese la constante B de Antoine para la sustancia :"))
        self.C=230.170#float(input("ingrese la constante C de Antoine para la sustancia :"))
        self.Vc=5.59e-5#input(float("ingrese el volumen critico de la sustancia m3 : "))
        self.Zc=0.229#input(float("ingrese el factor de compresibilidad critico de la sustancia : "))
        self.Tr=self.T/self.Tc
        self.Pr=self.P/self.Pc
        
        
    def presion_saturacion(self):
        self.Ps=np.exp(self.A-((self.B)/(self.Ts+self.C)))
        print("----------------------------------------------------------------")
        print("la presion de saturacion en Kpa es : ",self.Ps)
        print("----------------------------------------------------------------")
        if self.P > self.Ps:
            print("La sustancia a la presion indicada se encuentra en estado de liquido P>Psat")
            print("----------------------------------------------------------------")
        if self.P < self.Ps:
            print("La sustancia a la presion indicada se encuentra en estado de vapor P<Psat")
            print("----------------------------------------------------------------")
            
    def coeficientes_viriales(self):
        self.B0=0.083-((0.422)/(self.Tr**1.6))
        self.B1=0.139-((0.172)/(self.Tr**4.2))
        self.B=(self.R*self.Tc/self.Pc)*(self.B0+self.w*self.B1)
        
        
    def calculo_coeficiente_y_fugacidad_vapor(self):
        self.LnΦ=((self.B*self.P)/(self.R*self.T))
        self.Φ=np.exp(self.LnΦ)
        self.f=self.Φ*self.P
        print("El coeficiente de fugacidad para el vapor es : ",self.Φ)
        print("----------------------------------------------------------------")            
        print("La fugacidad de la sustancia en vapor Kpa es : ",self.f)
        print("----------------------------------------------------------------")
        
    def calculo_Z_y_V(self):
        self.Z=1+self.LnΦ
        print("El factor de compresibilidad Z es : ",self.Z)
        print("----------------------------------------------------------------")
        self.V=((self.Z*self.R*self.T)/(self.P))
        print("el volumen molar del vapor en m3/Kmol es : ",self.V)
        print("----------------------------------------------------------------")
        
        


##### EL SIGUIENTE ALGORITMO PERMITE EL CALCULO DE fi Y Φi PARA LIQUIDOS    
        
    def calculo_coeficiente_y_fugacidad_liquido(self):
        self.Φsat=np.exp(((self.B*self.Ps)/(self.R*self.T)))
        print("el coeficiente de fugacidad de saturacion es : ",self.Φsat)
        print("----------------------------------------------------------------")
        self.a=(1-self.Tr)**(2/7)
        self.Vl=(self.Vc)*(self.Zc**self.a)
        print("el volumen del liquido m3/Kmol es : ",self.Vl)
        print("----------------------------------------------------------------")
        self.fl=self.Φsat*self.Ps*np.exp(((self.Vl)/(self.R*self.T))*(self.P-self.Ps))
        print("la fugacidad del liquido Kpa es : ",self.fl)
        print("----------------------------------------------------------------")
        print("el coeficiente de fugacidad del liquido es :",(self.fl/self.P))
        print("----------------------------------------------------------------")
        
        
### para el vapor    
        
#fugacidad=fugacidad_y_coeficiente()
#fugacidad.variables()
#fugacidad.presion_saturacion()
#fugacidad.coeficientes_viriales()
#fugacidad.calculo_coeficiente_y_fugacidad_vapor()
#fugacidad.calculo_Z_y_V()
        
### para el liquido 
       
fugacidad=fugacidad_y_coeficiente()
fugacidad.variables()
fugacidad.presion_saturacion()
fugacidad.coeficientes_viriales()
fugacidad.calculo_coeficiente_y_fugacidad_liquido()          
        
        
        
            

    
        
        
        
        
        
            
















