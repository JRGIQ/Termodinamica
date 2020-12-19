#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 01:14:56 2020

@author: jheison
"""


import sympy as sp
from sympy.solvers import solve
import numpy as np
import math as mt

class termo():
    
    def ejercicio5(self):
        
        T = sp.Symbol('T')
        self.potencia=float(input("Potencia en W :"))
        self.e=float(input("Emisividad : "))
        self.Area=float(input("Area m² :"))
        self.Tamb=float(input("Temperatura ambiente K :"))
        self.haire=float(input("coeficiente convección aire [W/m² K] :"))
        self.Qconv=self.haire*self.Area*(T-self.Tamb)
        self.Qrad=self.Area*self.e*5.67e-8*(T**4-self.Tamb**4)
        
        self.Tbase=solve(self.Qconv+self.Qrad-self.potencia, T)
        print("Raices",self.Tbase)
        
    def ejercicio6(self):
        self.Tresistencia=float(input("Temp resistencia °C : "))
        self.Potencia=float(input("Potencia KW : "))
        self.Tagua=float(input("Temp agua °C :"))
        self.D=float(input("Diámetro [m] : "))
        self.L=float(input("Longitud [m] : "))
        self.Area=mt.pi*self.D*self.L
        self.U=((self.Potencia)/(self.Area*(self.Tresistencia-self.Tagua)))
        print("Coeficiente de TdeCalor : ",self.U*1000, "W/m² °C")
        
    def ejercicio7(self):
        
        self.Potencia=float(input("Potencia KW : "))
        self.Vutil=float(input("Vida útil años: "))
        self.FactorP=float(input("Factor de planta : "))
        self.Ngeneradores=float(input("Número de generadores : "))
        self.Factornacional=float(input("Factor nacional [tCO2/MW h] : "))
        
        self.horasR=self.FactorP*8760
        self.GeneER=self.Potencia*self.horasR
        self.PMW=self.GeneER/1e3
        self.emisiones=(self.PMW*self.Vutil*self.Factornacional)*self.Ngeneradores
        
        print("Emisiones ",self.emisiones,"toneladas de CO2")
        
    def ejercicio8(self):
        
        self.Vel=float(input("Velocidad del viento m/s : "))
        self.D=float(input("Diámetro del alabe [m] : "))
        self.Vutil=float(input("Vida útil años : "))
        self.FactorP=float(input("Factor Planta : "))
        self.FactorN=float(input("Factor nacional [ton CO2/MW h]: "))
        self.Ro=float(input("Densidad del viento Kg/m³ : "))
        self.Precio=float(input("Precion de la tonelada CO2 [US]: "))
        
        self.caudal=self.Vel*mt.pi*(self.D/2)**2
        self.m=self.caudal*self.Ro
        self.W=(self.m*(self.Vel**2)/2)/1e6
        self.GenER=self.W*self.FactorP*8760
        self.emisiones=self.GenER*self.Vutil*self.FactorN
        self.US=self.emisiones*self.Precio
         
        print("Toneladas de CO2 : ", self.emisiones ," \n Precion en $US ", self.US )
        
    def ejercicio9(self):
        
        self.rpm=float(input("RPM : "))
        self.vel=float(input("Velocidad [m/s] : "))
        self.m=float(input("Flujo másico [Kg/s] : "))
        self.W=float(input("Potencia [KW] : "))
        self.Ro=float(input("Densidad del aire [kg/m³] "))
        
        self.D=((self.vel*60)/(self.rpm*mt.pi))
        self.A=mt.pi*(self.D/2)**2
        self.Q=self.m/self.Ro
        self.vprom=self.Q/self.A
        self.Pot=(self.m*((self.vprom**2)/(2)))/1e3
        self.efic=(self.W/self.Pot)*100
        print("Velocidad promedio [m/s] ", self.vprom)
        print("Eficiencia : ", self.efic)
        
    def ejercicio10(self):
        
        
        print("introducir manualmente el angulo como pi/2, pi/3 ....")
        self.m=float(input("Masa [Kg] : "))
        self.t=float(input("Tiempo [s] : "))
        self.L=float(input("Longitud [m] : "))
        self.ang=float(input("Angulo [°]: "))
        self.T=(self.m*9.81*self.L*mt.sin(mt.radians(self.ang))/1e3)
        self.W=self.T/self.t
        print("Potencia [KW] : ", self.W)
        
    def ejercicio11(self):
        print("introducir manualmente el angulo como pi/2, pi/3 ....")
        self.m=float(input("Masa [Kg] : "))
        self.t=float(input("Tiempo [s] : "))
        self.L=float(input("Longitud [m] : "))
        self.ang=float(input("Angulo [°] : " ))
        self.vel=float(input("Velocidad [m/s] : "))
        self.T=((self.m*9.81*self.L*mt.sin(mt.radians(self.ang))+(self.m*(self.vel**2)/2))/1e3)
        self.W=self.T/self.t
        print("Potencia [KW] : ",self.W)
        
    def ejercicio12(self):
        
        print("introducir manualmente el angulo como pi/2, pi/3 ....")
        self.m=float(input("Masa [Kg] : "))
        self.t=float(input("Tiempo [s] : "))
        self.L=float(input("Longitud [m] : "))
        self.ang=float(input("Angulo [°]: " ))
        self.velIni=float(input("Velocidad inicial [m/s] : "))
        self.velFinal=float(input("Velocidad final [m/s] : "))
        self.T=((self.m*9.81*self.L*mt.sin(mt.radians(self.ang))+(self.m*(self.velFinal**2-self.velIni**2)/2))/1e3)
        self.W=self.T/self.t
        print("Potencia [KW] : ",self.W)        
        
    def ejercicio13(self):
        
        self.vel=float(input("Velocidad [m/s] : "))
        self.D=float(input("Diámetro [m] : "))
        self.Ro=float(input("Densidad [kg/m³] : "))
        self.Q=self.vel*mt.pi*(self.D/2)**2
        self.m=self.Q*self.Ro
        self.W=(self.m*(self.vel**2)/2)/1e3
        print("Potencia [KW] : ",self.W)
        
    def ejercicio14(self):
        
        self.vel=float(input("Velocidad [m/s] : "))
        self.D=float(input("Diámetro [m] : "))
        self.Ro=float(input("Densidad [kg/m³] : "))
        self.FP=float(input("Factor de planta [h/año] : "))
        self.FN=float(input("Factor nacional [0.2917 o 0.3670]  : "))
        self.Vutil=float(input("Vida útil [años]  : "))
        self.Q=self.vel*mt.pi*(self.D/2)**2
        self.m=self.Q*self.Ro
        self.W=(self.m*(self.vel**2)/2)/1e6
        self.GER=self.W*self.FP*8760
        self.emisiones=self.GER*self.Vutil*self.FN
        
        print("Potencia [MW] : ",self.W) 
        print("Emisiones [ton CO2] : ", self.emisiones)
        
    def ejercicio15(self):
        
        self.v1=float(input("Velocidad ciudad 1 [m/s] : "))
        self.v2=float(input("Velocidad ciudad 2 [m/s] : "))
        self.A=float(input("Áres [m²] : "))
        self.horas1=float(input("Horas al año ciudad 1 [horas] : "))
        self.horas2=float(input("Horas al año ciudad 2 [horas] : "))
        self.Ro=float(input("Densidad del aire [kg/m³] : "))
        self.FP1=self.horas1/8760
        self.FP2=self.horas2/8760
        self.Q1=self.v1*self.A
        self.Q2=self.v2*self.A
        self.m1=self.Q1*self.Ro
        self.m2=self.Q2*self.Ro
        self.W1=self.m1*(self.v1**2)/2
        self.W2=self.m2*(self.v2**2)/2
        self.W=(self.W1+self.W2)/1e3
        print("Potencia por las dos ciudades [KW] : ", self.W)
        
    def ejercicio17(self):
        
        self.m=float(input("Masa [kg] : "))
        self.vel=float(input("Velocidad [m/s] : "))
        self.ang=float(input("Angulo [°]: "))
        self.W=(self.m*9.81*self.vel*mt.sin(mt.radians(self.ang))/1e3)
        print("Potencia [KW] : ",self.W)
        
    
    def ejercicio20(self):
        
        self.personas=float(input("Número de personas : "))
        self.m=float(input("Masa de cada persona [kg] : "))
        self.vel=float(input("Velocidad : "))
        self.ang=float(input("Angulo [°]: "))
        self.W=(self.personas*self.m*9.81*self.vel*mt.sin(mt.radians(self.ang))/1e3)
        print("Potencia [KW] " ,self.W)
        print("Potencia duplicando la velocidad [KW] : ", self.W*2)
        
    def ejercicio21(self):
        
        self.L=float(input("Longitud del ducto [ft] : "))
        self.vel=float(input("velocidad [ft/s] : "))
        self.Ro=float(input("Densidad [lbm/ft³] : "))
        self.Q=self.vel*self.L*self.L
        self.m=self.Q*self.Ro
        self.W=self.m*(self.vel**2)/2
        print("Potencia [Btu/s] : ", self.W)
        self.W2=self.W*0.453592*0.3048**2
        print("Potencia [W] : ", self.W2)
        
    def ejercicio22(self):
        
        self.vel=float(input("Velocidad [m/s] : "))
        self.molinos=float(input("Número de molinos : "))
        self.D=float(input("Diámetro alabe [m] : "))
        self.Ro=float(input("Densidad viento [kg/m³] : "))
        self.Q=self.vel*mt.pi*(self.D/2)**2
        self.m=self.Q*self.Ro
        self.W=((self.m*(self.vel**2)/2)/1e3)*self.molinos
        print("Potencia [KW] : ", self.W )
        
    def ejercicio23(self):
        
        self.vel=float(input("Velocidad [m/s] : "))
        self.molinos=float(input("Número de molinos : "))
        self.D=float(input("Diámetro alabe [m] : "))
        self.Ro=float(input("Densidad viento [kg/m³] : "))
        self.FP=float(input("Factor de planta [h/año] : "))
        self.FN=float(input("Factor nacional Factor nacional [0.2917 o 0.3670-ton CO2/MWh] : "))
        self.Vutil=float(input("Vida util [años] : "))
        self.Q=self.vel*mt.pi*(self.D/2)**2
        self.m=self.Q*self.Ro
        self.W=((self.m*(self.vel**2)/2)/1e3)*self.molinos
        self.GER=self.W*self.FP*8760
        self.emisiones=(self.GER/1e3)*self.Vutil*self.FN
        
        print("Generación de energía [KW] : ", self.GER )   
        print("Emisiones [ton CO2] : ",self.emisiones)
        
    def ejercicio24(self):
        
        self.m=float(input("Masa elevador [kg] : "))
        self.vel=float(input("Velocidad [m/s] : "))
        self.W=((self.m*9.81*self.vel)/1e3)
        print("Potencia [KW] : ", self.W)
        
        
    def ejercicio25(self):
        
        self.Welec=float(input("Consumo de energía electrica [KW] : "))
        self.Q=float(input("Flujo volumétrico [m³/s] : "))
        self.Ro=float(input("Densidad fluido [Kg/m³] : "))
        self.Dsuc=float(input("Diámetro de succión [m] : "))
        self.Ddes=float(input("Diámetro de descarga [m] : "))
        self.P=float(input("Aumento de presión [Kpa] : "))
        self.E_motor=float(input("Eficiencia del motor [%] : "))
        
        self.m=self.Ro*self.Q
        self.v1=((self.Q)/(mt.pi*(self.Dsuc/2)**2))
        self.v2=((self.Q)/(mt.pi*(self.Ddes/2)**2))
        self.Wflujo=(self.m*((self.P*1000/self.Ro)+(self.v2**2-self.v1**2)/2))/1e3
        self.E_bombaMotor=(self.Wflujo/self.Welec)*100
        self.E_bomba=(self.E_bombaMotor/self.E_motor)
        print("Trabajo del flujo [KW] : ", self.Wflujo)
        print("Eficiencia bomba-motor [%] : ",self.E_bombaMotor)
        print("Eficiencia bomba [%] : ", self.E_bomba)
        
    def ejercicio26(self):
        
        self.Welec=float(input("Consumo de energía electrica [KW] : "))
        self.P=float(input("Diferencia de presión succión-descarga [Kpa] : "))
        self.Q=self.Welec/self.P
        self.E_elec=float(input("Eficiencia motor : "))
        self.Wmec=float(input("Potencia mecánica bomba [KW] : "))
        self.E_bom_mot=(self.Welec/self.Wmec)
        self.E_bomba=(self.E_bom_mot/self.E_elec)
        print("Eficiencia bomba-motor [%] : ",self.E_bom_mot*100)
        print("Eficiencia bomba [%] : ",self.E_bomba*100)
        
    def ejercicio28(self):
        
        self.L=float(input("Longitud [m] : "))
        self.D=float(input("Diámetro [m] : "))
        self.Tagua=float(input("Temperatura fluido dentro tuberia [°C] : "))
        self.Taire=float(input("Temperatura fluido fuera tuberia  [°C] : "))
        self.h=float(input("Coeficiente convección [W/m² K] : "))
        self.A=mt.pi*self.D*self.L
        self.Q=(self.h*self.A*(self.Tagua-self.Taire))/1e3
        print("Tasa de pérdida de calor [KW] : ", self.Q)
        
    def ejercicio29(self):
        
        self.m=float(input("Flujo másico ventilador [kg/s] : "))
        self.Volt=float(input("Voltaje [V] : "))
        self.I=float(input("Corriente [Amp] : "))
        self.W=self.Volt*self.I
        self.v=(2*self.W/self.m)**0.5
        print("Velocidad del ventilador [m/s] : ",self.v)
        


        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
ejercicio=termo()
ejercicio.ejercicio7()








