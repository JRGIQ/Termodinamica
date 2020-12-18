#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:35:19 2018

@author: jheison
"""

###CALCULO DE VOLUMEN Y FACTOR Z DE UNA SUSTANCIA PURA EN DOS FASES ECUACION DE ESTADO RK

class calculo_propiedades_termodinamicas:
    def parametros_intensivos(self):
        self.R= 83.14 #float(input("ingrese constante de los gases (cm3*bar/mol*K): "))
        self.T=350 #float(input("ingrese la temperatura del sistema(K): "))
        self.P= 9.4573 #float(input("ingrese la presion del sistema (bar): "))
        self.Tc=425.1 #float(input("ingrese la temperatura critica (apendice B smith van ness)  (K): "))
        self.Pc=37.96 #float(input("ingrese la presion critica (bar) (apendice B smith van ness): "))
        self.omega=0.2 #float(input("ingrese factor acentrico (apendice B smith van ness): "))
        self.Tr=self.T/self.Tc
        self.Pr=self.P/self.Pc
        
    def parametros_ecuacion_estado_RK(self):
        self.sigma=1
        self.epsilon=0
        self.landa=0.08664
        self.sita=0.42748
        self.alphaTr=self.Tr**(-0.5)
#        self.q=((self.sita*self.alphaTr)/(self.landa*self.Tr)) #opcional
#        self.q=((self.sita*self.Tr**-0.5)/(self.landa*self.Tr)) #opcional
        self.q=((self.sita)/(self.landa))*self.Tr**(-3/2)
        self.Zc=1/3
        self.a=(self.sita*self.alphaTr*(self.R**2)*(self.Tc**2))/self.Pc ### a(T)
        self.b=((self.landa*self.R*self.Tc)/(self.Pc))
#        self.beta=((self.b*self.P)/(self.R*self.T)) #opcionalfile:///G:/
        self.beta=((self.landa*self.Pr)/(self.Tr))
        
    def calculo_volumen_liquido_saturado(self):
        self.V0=self.b
        for iteration in range(1,100):
            self.Vl=self.b+((self.V0+self.epsilon*self.b)*(self.V0+self.sigma*self.b))*((self.R*self.T+self.b*self.P-self.V0*self.P)/(self.a)) ### para liquido saturado
            self.V0=self.Vl
            print("el volumen del liquido saturado (cm3) es: ",self.V0)
            
    def calculo_factor_compresibilidad(self):
        self.Z0=0.001
        for iteration in range(1,100):
#            self.Z=1+self.beta-(self.q*self.beta)*((self.Z0-self.beta)/((self.Z0+self.epsilon*self.beta)*(self.Z0+self.sigma*self.beta))) ###para vapor saturado pag 97 smith van ness
            self.Z=1+self.beta+(self.q*self.beta)*((self.beta-self.Z0)/((self.Z0)*(self.Z0+self.beta)))### para vapor saturado
#            self.Z=self.beta+(self.Z0+self.epsilon*self.beta)*(self.Z0+self.sigma*self.beta)*((1+self.beta-self.Z0)/(self.q*self.beta))####para liquido saturado pag 87 smith
            self.Z0=self.Z
            print("el factor de compresibilidad es: ",self.Z0)
            
    def calculo_volumen_vapor_saturado(self):
        self.Vg=self.Z0*self.R*self.T/self.P
        print("el volumen del vapor saturado (cm3) es: ", self.Vg)
        

volumen1=calculo_propiedades_termodinamicas()
volumen1.parametros_intensivos()
volumen1.parametros_ecuacion_estado_RK()
volumen1.calculo_volumen_liquido_saturado()
volumen1.calculo_factor_compresibilidad()
volumen1.calculo_volumen_vapor_saturado()
    
        
        