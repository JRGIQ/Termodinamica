#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 17:27:25 2018

@author: jheison
"""
######## ESTE PROGRAMA CALCULA LAS PROPIEDADES TERMODINAMICAS 

# SUSTANCIAS PURAS SIN REACCION

class propiedades_termodinamicas():
    def capacidad_calorica_gas_ideal(self):
        self.T=float(input("ingrese la temperatura del sistema (K): "))
        self.A=float(input("ingrese la constante A: "))### Tabla C1 smith van ness
        self.B=float(input("ingrese la constante B e-00: "))
        self.C=float(input("ingrese la constante C e-00: "))
        self.D=float(input("ingrese la constante D e-00: "))
        self.Cp=self.A+self.B*self.T+self.C*self.T*self.T+self.D/self.T*self.T
        print("la capacidad calorica del gas ideal es (Cp/R): ",self.Cp)
    
    def integral_calor_sensible(self): #cap 4 pag 130 smith van ness
        self.T0=float(input("ingrese la temperatura inicial (K): "))
        self.T=float(input("ingrese la temperatura final (K): "))
        self.R=8.314 #J/mol*K #float(input("ingrese la constante de los gases cualquier dimension: "))
        self.A=float(input("ingrese la constante A: "))### Tabla C1 smith van ness
        self.B=float(input("ingrese la constante B e-03: "))*1e-03
        self.C=float(input("ingrese la constante C e-06: "))*1e-06
        self.D=float(input("ingrese la constante D e-00: "))
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
       
    def calor_estandar_reaccion(self):
        self.ΔHe=float(input("ingrese el calor estandar de la reaccione completa J a (298K): "))
        self.ΔHer=self.ΔHe+self.ΔH
        print("el calor estandar de reaccion en (J) a Temperatura T es: ",self.ΔHer)
        
calor1=propiedades_termodinamicas()
calor1.integral_calor_sensible()
#calor1.calor_estandar_reaccion()


    

        
        