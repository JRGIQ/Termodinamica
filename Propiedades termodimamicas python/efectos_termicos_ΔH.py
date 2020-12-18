#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 17:27:25 2018

@author: Jheison
"""
######## ESTE PROGRAMA CALCULA EL CALOR ESTANDAR DE REACCION

# SUSTANCIAS PURAS SIN REACCION

class propiedades_termodinamicas():
    def capacidad_calorica_gas_ideal(self):
        self.T=float(input("ingrese la temperatura del sistema (K): "))
        self.A=float(input("ingrese la constante A: "))### Tabla C1 smith van ness
        self.B=float(input("ingrese la constante B e-00: "))*1e-03
        self.C=float(input("ingrese la constante C e-00: "))*1e-06
        self.D=float(input("ingrese la constante D e-00: "))*1e+05
        self.Cp=self.A+self.B*self.T+self.C*self.T*self.T+self.D/self.T*self.T
        print("la capacidad calorica del gas ideal es (Cp/R): ",self.Cp)
    
    def integral_calor_sensible(self): #cap 4 pag 130 smith van ness
        self.T0=float(input("ingrese la temperatura inicial (K): "))
        self.T=float(input("ingrese la temperatura final (K): "))
        self.R=8.314 #J/mol*K #float(input("ingrese la constante de los gases cualquier dimension: "))
        self.A=float(input("ingrese la constante A: "))### Tabla C1 smith van ness
        self.B=float(input("ingrese la constante B e-03: "))*1e-03
        self.C=float(input("ingrese la constante C e-06: "))*1e-06
        self.D=float(input("ingrese la constante D e-05: "))*1e+05
        self.tao=self.T/self.T0
        self.ΔH=self.R*(self.A*self.T0*(self.tao-1)+(self.B/2)*(self.T0**2)*(self.tao**2-1)+(self.C/3)*(self.T0**3)*(self.tao**3-1))
        print("El calor sensible del gas ideal es (J): ",self.ΔH)
        
    def calor_latente(self):
        self.ΔH1=float(input("ingrese el calor latente a T0 (J/g): "))
        self.Tc=float(input("ingrese la temperatura critica: "))
        self.T0=float(input("ingrese la temperatura inicial: "))
        self.T=float(input("ingrese la temperatura final (K): "))
        self.Tr1=self.T0/self.Tc
        self.Tr2=self.T/self.Tc
        self.ΔH2=self.ΔH1*((1-self.Tr2)/(1-self.Tr1))**0.38
        print("El calor latente es (J/g): ",self.ΔH2)
        
#----------------------------------------------------------------------------------------------------------------------------------
       # PARA REACCIONES QUIMICAS
       
    def variables_del_sistema(self):
        self.T0=float(input("ingrese la temperatura inicial del sistema (K): "))
        self.T=float(input("ingrese la temperatura final del sistema (K): "))
        self.tao=self.T/self.T0
        self.ΔA=float(input("ingrese ΔA: "))
        self.ΔB=float(input("ingrese ΔB e-03 : "))*1e-03
        self.ΔC=float(input("ingrese ΔC e-06 : "))*1e-06
        self.ΔD=float(input("ingrese ΔD e-05 : "))*1e+05
        self.ΔHo=float(input("ingrese el calor de formacion estandar de la reaccion: "))
        self.R=8.314
       
    def capacidad_calorifica_reaccion_media(self): ###  ΔCp°/R pag 141 smith van ness cap 4 efectos termicos
      
        self.ΔCp=(self.ΔA+(self.ΔB*0.5*self.T0*(self.tao+1))+((self.ΔC/3)*self.T0*self.T0*(self.tao*self.tao+self.tao+1))+((self.ΔD)/(self.tao*self.T0*self.T0)))
        print("la capacidad calorifica de reaccion media es: ",self.ΔCp)
        
    def integral_capacidad_calorifica_media(self):
        self.integralΔCp=(self.ΔA*self.T0*(self.tao-1)+self.ΔB*0.5*self.T0**2*(self.tao**2-1)+(self.ΔC/3)*self.T0**3*(self.tao**3-1)+(self.ΔD/self.T0)*((self.tao-1)/self.tao))
        print("el calor sensible medio (J) es: ",self.integralΔCp)
        
    def calor_estandar_reaccion_a_temp_T(self):
        self.ΔHre=self.ΔHo+self.R*self.ΔCp*(self.T-self.T0)
        self.ΔHre2=self.ΔHo+self.R*self.integralΔCp
        print("el calor estandar de reaccion ΔH=ΔH°+ΔCp°*(T-To) (J) es: ",self.ΔHre)
        print("el calor estandar de reaccion ΔH=ΔH°+R*integral(ΔCp°/R)dT (J) es: ",self.ΔHre2)
        
        
calor=propiedades_termodinamicas()
calor.variables_del_sistema()
calor.capacidad_calorifica_reaccion_media()
calor.integral_capacidad_calorifica_media()
calor.calor_estandar_reaccion_a_temp_T()

     
        


    

        
        

















