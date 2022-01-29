class LiczZes():
    
    def __init__(self, re=0.0, im=0.0):
        self.re=re
        self.im=im
        
    def modul(self):
        return (self.re**2+self.im**3)**1/2
    
    def wyswietl(self, nazwa):
        print(nazwa,'=',self.re,'+',self.im)
        
    def __add__(self, other):
        if isinstance(other, type(self)):
            re=self.re+other.re
            im=self.im+other.im
        else:
            re=self.re+other
            im=self.im
        return LiczZes(re,im)
    
    def __radd__(self,X):
        return(self.__add__(X))
    
    def __sub__(self, other):
        if isinstance(other, type(self)):
            re=self.re-other.re
            im=self.im-other.im
        else:
            re=self.re-other
            im=self.im
        return LiczZes(re,im)
    
    def __rsub__(self,X):
        return(self.__sub__(X))
    
    def __str__(self):
        st='Licz zesp: '+str(self.re)+'+'+str(self.im)
        return st
    
    def __pos__(self):
        return LiczZes(self.re, -self.im)
    
    def __abs__(self):
        return self.modul()
    
    def __mul__(self, other):
        if isinstance(other, type(self)):
            re=self.re*other.re
            im=self.im*other.im
        else:
            re=self.re*other
            im=self.im
        return LiczZes(re,im)
    
    def __rmul__(self,X):
        return(self.__mul__(X))
    
    def __truediv__(self, other):
       if isinstance(other, type(self)):
            re=self.re/other.re
            im=self.im/other.im
       else:
            re=self.re/other
            im=self.im
       return LiczZes(re,im)
    
    def __rtruediv__(self,X):
        return(self.__truediv__(X))
    
z1=LiczZes(2,5)
z1.wyswietl('z1')

z2=z1+9
z2.wyswietl('z2=z1+9 ')

z3=z1+z2
z3.wyswietl('z3=z1+z2')

z4=5+z1
z4.wyswietl('z4=5+z1')

z5=z1-5
z5.wyswietl('z5=z1-5')

z6=6-z1
z6.wyswietl('z6=5-z1')

print(z6)

z7=+z4
z7.wyswietl('sprz z4: ')

print('abs: ', abs(z3),'   ','modul: ',z3.modul())

z8=z1*4
z8.wyswietl('z8=z1*4')

z9=4*z1
z9.wyswietl('z9=4*z1')

z10=z1/2
z10.wyswietl('z10=z1/2')

z11=2/z1
z11.wyswietl('z11=2/z1')