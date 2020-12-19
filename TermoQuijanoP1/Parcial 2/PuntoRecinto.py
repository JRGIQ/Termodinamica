# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:15:04 2020

@author: JRGIQ
"""

class punto3():
    
    def Recinto(self):
        
        self.Cv=0.718
        
        
        # Datos del recinto cerrado
        
        self.VR=6*6*8
        self.TR=10
        self.PR=125
        self.RR=0.4615
        
        ## Datos sistema de calefacción
        
        self.RC=0.2870
        self.PC=300
        self.TC=250
        self.VC=16/1000
        self.W=165/1000
        
        self.min=45
        
        ## Datos finales
        
        self.Pf=125 #kpa
        self.vf=0.001048
        self.vg=1.375
        
        
        self.mR=((self.PR*self.VR)/(self.RC*(self.TR+273)))
        self.mC=((self.PC*self.VC)/(self.RR*(self.TC+273)))
        
        self.WU=self.W*60*self.min
        
        print("Energia interna = {} ".format(self.WU),"[KJ/kg]")
        
        self.T=((self.WU)/(self.mR*self.Cv))+self.TR
        
        print("Temperatura final = {} ".format(self.T),"°C")
        
        self.vpromC=self.VC/self.mC
        
        self.X=((self.vpromC-self.vf)/(self.vg-self.vf))
        
        print("Calidad = {} ".format(self.X))
        
        print(self.mC)
        
objeto=punto3()
objeto.Recinto()
        