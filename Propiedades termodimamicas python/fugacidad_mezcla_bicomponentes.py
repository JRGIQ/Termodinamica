# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:41:42 2019

@author: Jheison Gutierrez
"""

########## ESTE PROGRAMA CALCULA LA FUGACIDAD Y EL COEFICIENTE CON AYUDA DE LA ECUACION VIRIAL TRUNCADA 
######################## PARA MEZCLAS DE GASES BICOMPONENTES

import numpy as np
import math as mt

class fugacidad():
    
    def variables(self):
        self.R=8.314e-5 #m3*bar/K*mol
        self.T=323.15#input(float("ingrese la temperatura del sistema K : "))
        self.P=0.25#input(float("ingrese la presion del sistema bar : "))
        self.y1=0.5#input(float("ingrese la fraccion de vapor de la sustancia 1 : "))
        self.y2=1-self.y1
        self.Tc11=535.5#input(float("ingrese la temperatura critica de la sustancia 1 (K) : "))
        self.Tc22=591.8#input(float("ingrese la temperatura critica de la sustancia 2 (K) : "))
        self.Pc11=41.50#input(float("ingrese la presion critica de la sustancia 1 (bar) : "))
        self.Pc22=41.06#input(float("ingrese la presion critica de la sustancia 2 (bar) : "))
        self.Vc11=267e-6#input(float("ingrese el volumen critico de la sustancia 1 (m3/Kmol) : "))
        self.Vc22=316e-6#input(float("ingrese el volumen critico de la sustancia 2 (m3/Kmol) : "))
        self.Zc11=0.249#input(float("ingrese el factor de compresibilidad critico para la sustancia 1 : "))
        self.Zc22=0.264#input(float("ingrese el factor de compresibilidad critico para la sustancia 2 : "))
        self.Zc12=((self.Zc11+self.Zc22)/(2))
        self.Vc12=(((self.Vc11**(1/3))+(self.Vc22**(1/3)))/2)**3
        self.Tc12=(self.Tc11*self.Tc22)**0.5
        self.w11=0.323#input(float("ingrese el factor acentrico de la sustancia 1"))
        self.w22=0.262#input(float("ingrese el factor acentrico de la sustancia 2"))
        self.w12=((self.w11+self.w22)/(2))
#        self.V11=input(float("ingrese el volumen molar de la sustancia 1"))
#        self.V22=input(float("ingrese el volumen molar de la sustancia 2"))
#        self.V12=(((self.V11**1/3)+(self.V22**1/3))/2)**3
        self.Tr1=self.T/self.Tc11
        self.Tr2=self.T/self.Tc22
        self.Tr12=self.T/self.Tc12
        
    def coeficientes_viriales_sustancias_puras(self):       
        
                       
             
        self.B011=((0.083)-((0.422)/(self.Tr1**1.6)))
        self.B111=(0.139)-((0.172)/(self.Tr1**4.2))
        self.B11=((self.B011)+(self.w11*self.B111))
        self.B022=((0.083)-((0.422)/(self.Tr2**1.6)))
        self.B122=((0.139)-((0.172)/(self.Tr2**4.2)))
        self.B22=((self.B022)+(self.w22*self.B122))
        self.B1=((self.B11*self.R*self.Tc11)/(self.Pc11))
        self.B2=((self.B22*self.R*self.Tc22)/(self.Pc22))
        print("----------------------------------------------------------------")
        print("el segundo coeficiente virial B11 m3/mol es : ",self.B1)
        print("----------------------------------------------------------------")
        print("el segundo coeficiente virial B22 m3/mol es : ",self.B2)
        print("----------------------------------------------------------------")        
    
        
        
            
    def coeficiente_virial_mezcla_B12(self):
        self.B012=((0.083)-((0.422)/(self.Tr12**1.6)))
        self.B112=((0.139)-((0.172)/(self.Tr12**4.2)))
        self.Pc12=((self.Zc12*self.Tc12*self.R)/(self.Vc12))
        self.Bmezcla=self.B012+self.w12*self.B112
        self.B12=((self.Bmezcla*self.R*self.Tc12)/(self.Pc12))
        print("el segundo coeficiente virial B12 m3/mol es :",self.B12)
        print("----------------------------------------------------------------")
        
    def calculo_Z11_Z22_Z12(self):
        self.Z11=1+((self.B1*self.P)/(self.R*self.T))
        self.Z22=1+((self.B2*self.P)/(self.R*self.T))
        self.Z12=1+((self.B12*self.P)/(self.R*self.T))
        print("el factor de compresibilidad Z11 es : ",self.Z11)
        print("----------------------------------------------------------------")
        print("el factor de compresibilidad Z22 es : ",self.Z22)
        print("----------------------------------------------------------------")
        print("el factor de compresibilidad de la sustancia 1 Z1 es : ",self.Z11)
        print("----------------------------------------------------------------")
        print("el factor de compresibilidad de la sustancia 2 Z2 es : ",self.Z22)
        print("----------------------------------------------------------------")
        print("el factor de compresibilidad de la mezcla de gases Z12 es : ",self.Z12)
        print("----------------------------------------------------------------")
        
    def calculo_V11_V22_V12(self):
        self.V11=((self.R*self.T*self.Z11)/(self.P))
        self.V22=((self.R*self.T*self.Z22)/(self.P))
        print("el volumen molar de la sustancia 1 V1 m3/mol es : ",self.V11)
        print("----------------------------------------------------------------")
        print("el volumen molar de la sustancia 2 V2 m3/mol es : ",self.V22)
        print("----------------------------------------------------------------")
        print("el volumen molar de la mezcla V12 m3/mol es : ",self.V11)
        print("----------------------------------------------------------------")
        
    def delta12(self):
        self.delta12=((2*self.B12)-(self.B1-self.B2))
        
    def coeficiente_fugacidad(self):
        self.LnΦ1=((self.P)/(self.R*self.T))*((self.B1)+(self.y2*self.y2*self.delta12))
        self.Φ1=np.exp(self.LnΦ1)
        self.LnΦ2=(((self.P)/(self.R*self.T))*(self.B2+((self.y1**2)*(self.delta12))))
        self.Φ2=np.exp(self.LnΦ2)
        print("el coeficiente de fugacidad Φ1 en mezcla para la sustancia 1 es : ",self.Φ1)
        print("----------------------------------------------------------------")
        print("el coeficiente de fugacidad Φ2 en mezcla para la sustancia 2 es : ",self.Φ2)
        print("----------------------------------------------------------------")
        
    def coeficiente_fugacidad_mezcla(self):
        self.LnΦ=self.y1*self.LnΦ1+self.y2*self.LnΦ2
        self.Φ=np.exp(self.LnΦ)
        print("el coeficiente de fugacidad de la mezcla Φ por el teorema de euler LnΦ=y1*LnΦ1+y2*LnΦ2 es : ",self.Φ)
        print("----------------------------------------------------------------")
        
fugacidad=fugacidad()
fugacidad.variables()
fugacidad.coeficientes_viriales_sustancias_puras()
fugacidad.coeficiente_virial_mezcla_B12()
fugacidad.calculo_Z11_Z22_Z12()
fugacidad.calculo_V11_V22_V12()
fugacidad.delta12()
fugacidad.coeficiente_fugacidad()  
fugacidad.coeficiente_fugacidad_mezcla()    
    
   
        
    
    
        
    
        
        