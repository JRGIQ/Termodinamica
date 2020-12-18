# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import math as mt
class calculo_entropia():
    def variables(self):
        self.T0=float(input("ingrese la temperatura inicial gas ideal (K): "))
        self.P0=float(input("ingrese la presion inicial del gas ideal (bar): "))
        self.T=float(input("ingrese la temperatura final gas ideal (K): "))
        self.P=float(input("ingrese la presion final del gas ideal (bar): "))
        self.tao=self.T/self.T0
        self.tao2=self.P/self.P0
        self.R=8.314 #J/mol*K
        self.ΔA=float(input("ingrese la constante ΔA o A del gas ideal"))
        self.ΔB=float(input("ingrese la constante ΔB o B del gas ideal"))
        self.ΔC=float(input("ingrese la constante ΔC o C del gas ideal"))
        self.ΔD=float(input("ingrese la constante ΔD o D del gas ideal"))
        
        
    def capacidad_calorifica_media_especifica(self): ## pag 172 smith van ness
        self.Cps=self.ΔA+(self.ΔB*self.T0+(self.ΔC*self.T0**2+((self.ΔD)/(self.tao**2*self.T0**2)))*((self.tao+1)*0.5))*((self.tao-1)/(mt.log(self.tao)))
        print("la capacidad calorifica media gas ideal (Cps/R)ig es: ",self.Cps)
        
    def cambio_entropia_gas_ideal(self):
        self.ΔS=self.R*(self.Cps*mt.log(self.tao)-mt.log(self.tao2))
        print("el cambio de entropia ΔS del gas ideal (J) es: ",self.ΔS)
        
entropia=calculo_entropia()
entropia.variables()
entropia.capacidad_calorifica_media_especifica()
entropia.cambio_entropia_gas_ideal()