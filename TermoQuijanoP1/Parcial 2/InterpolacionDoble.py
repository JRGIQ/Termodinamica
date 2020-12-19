# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:03:30 2020

@author: JRGIQ
"""

class parcial2():
    
    def InterpolacionDoble(self):
        
    

        self.T1=350
        self.P1=1
        self.X11=0.28250
        self.X12=0.30661
        self.T2=400
        self.P2=1.2
        self.X21=0.23455 
        self.X22=0.25482
        
        ### Las que dan
        
        self.Tprom=385
        self.Pprom=1.1
        
        self.m1=((self.X12-self.X11)/(self.T2-self.T1))
        
        
        self.V1=self.m1*(self.Tprom-self.T1)+self.X11
        
        self.m2=((self.X22-self.X21)/(self.T2-self.T1))
        
        self.V2=self.m2*(self.Tprom-self.T1)+self.X21
        
        self.m3=((self.V2-self.V1)/(self.P2-self.P1))
        
        self.V=self.m3*(self.Pprom-self.P1)+self.V1
        
        print("Volumen especifico {}".format(self.V),"[m3/kg]")
        
        
        
    def CalorEspecfico(self):        
                
        
        self.T1=30+273
        self.T2=350+273
        self.a=25.48 
        self.b=1.520e-2
        self.c=-0.7155e-5
        self.d=1.312e-9
        self.m=3.6
        self.M=32
        self.Cpgas=self.a*(self.T2-self.T1)+((self.b*(self.T2**2-self.T1**2))/(2))+((self.c*(self.T2**3-self.T1**3))/(3))+((self.d*(self.T2**4-self.T1**4))/(4))
        self.C=(self.Cpgas/self.M)*self.m
        print("El calor es {} ".format(self.C))
        
    def VanDerWaals(self):
        
        
        self.P=120
        self.v=0.4718
        self.R=0.1052
        self.Tc=673.6
        self.Pc=588.7
        self.a=((27*(self.R**2)*(self.Tc**2))/(64*self.Pc))
        self.b=((self.R*self.Tc)/(8*self.Pc))
        
        self.T=round((((self.P+(self.a/self.v**2))*(self.v-self.b))/self.R),4)
        
        print("La temperatura es {} ".format(self.T),"°C")
        
    def tanques(self):
        
        self.mA=4
        self.mB=3
        
        self.PA=1100
        self.TA=385
        self.TB=170
        self.X=0.6
        
        self.Pf=375
        
        ## datos de Interpolación
        
        self.T1=350
        self.P1=1
        self.X11=2875.7
        self.X12=2957.9
        self.T2=400
        self.P2=1.2
        self.X21=2872.7 
        self.X22=2955.5
        
        ### Las que dan
        
        self.Tprom=self.TA
        self.Pprom=self.PA/1000
        
        self.m1=((self.X12-self.X11)/(self.T2-self.T1))
        
        
        self.V1=self.m1*(self.Tprom-self.T1)+self.X11
        
        self.m2=((self.X22-self.X21)/(self.T2-self.T1))
        
        self.V2=self.m2*(self.Tprom-self.T1)+self.X21
        
        self.m3=((self.V2-self.V1)/(self.P2-self.P1))
        
        self.V=self.m3*(self.Pprom-self.P1)+self.V1
        
        print("La propiedad específica es {}".format(self.V),"[m3/kg]")  
        
        
        
        

        
        

objeto=parcial2()
# objeto.CalorEspecfico()
# objeto.InterpolacionDoble()
# objeto.VanDerWaals()
objeto.tanques()
