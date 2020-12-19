# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:30:52 2020

@author: JRGIQ
"""


class tanquesAB():
    
    
    
    def EnergiaInternaA(self):
        
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
        
        self.UA=self.m3*(self.Pprom-self.P1)+self.V1
        
        
        print("Energía interna tanque A = {}".format(self.UA),"[KJ/kg]")  
        
    def VolumenA(self):
        
        # Datos tanque A
        self.PA=1100
        self.TA=385
        self.mA=4
        
        # Datos tanque B
        
        self.mB=3
        self.TB=170
        self.XB=0.6
        
        self.vf=0.001114
        self.vg=0.24260
        
        self.uf=718.2
        self.ufg=1857.5
        
        # Datos estado final
        
        
        self.Pf=375
        self.vff=0.001081
        self.vgf=0.49133
        
        self.Uf=594.32
        self.Ufg=1956.6
        
        ## datos de Interpolación tanque A
        
        self.T1=350
        self.P1=1
        self.X11=0.28250
        self.X12=0.30661
        self.T2=400
        self.P2=1.2
        self.X21=0.23455 
        self.X22=0.25482
        
        ### Las que dan
        
        self.Tprom=self.TA
        self.Pprom=self.PA/1000
        
        self.m1=((self.X12-self.X11)/(self.T2-self.T1))
        
        
        self.V1=self.m1*(self.Tprom-self.T1)+self.X11
        
        self.m2=((self.X22-self.X21)/(self.T2-self.T1))
        
        self.V2=self.m2*(self.Tprom-self.T1)+self.X21
        
        self.m3=((self.V2-self.V1)/(self.P2-self.P1))
        
        self.V=self.m3*(self.Pprom-self.P1)+self.V1
        self.volumenA=self.mA*self.V
        
        
        print("Volumen específico tanque A = {}".format(self.V),"[m3/kg]")  
        print("Volumen del tanque A = {}".format(self.volumenA),"[m3]") 
        
        self.vpromB=self.vf+self.XB*(self.vg-self.vf)
        print("Volumen específico mezcla tanque B = {}".format(self.vpromB),"[m3/kg]")  
        
        self.UB=self.uf+self.XB*self.ufg
        
        self.volumenB=self.mB*self.vpromB
        print("Volumen del tanque B = {}".format(self.volumenA),"[m3]") 
        
        self.volumenT=self.volumenA+self.volumenB
        
        print("Volumen total (A+B) = {}".format(self.volumenT),"[m3]") 
        
        
        self.volEspT=self.volumenT/(self.mA+self.mB)
        
        self.X=((self.volEspT-self.vff)/(self.vgf-self.vff))
        
        print("Calidad final = {}".format(self.X))
        
        self.Ufinal=self.Uf+self.X*self.Ufg
        
        print("Energía interna específica final = {}".format(self.Ufinal),"[KJ/kg]")  
        
        self.Calor=-(self.mA*(self.Ufinal-self.UA)+self.mB*(self.Ufinal-self.UB))
        
        print("Calor transferido = {}".format(self.Calor))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
parcial=tanquesAB()
parcial.EnergiaInternaA()
parcial.VolumenA()