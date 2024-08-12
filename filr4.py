class samsung:
    def __init__(self, name,inch):
        self.name = name
        self.inch = inch
    def features_sumg(self):
        lst1=self.name,self.inch
        return lst1
class vivo(samsung):
    def __init__(self, name, inch, salary, post):
        samsung.__init__(self,name,inch)
        self.salary = salary
        self.post = post
    def features_vivo(self):
        lst=self.name,self.inch,self.salary,self.post
        return lst
            
        
a=samsung("Nikil","6")
s=a.features_sumg()
for k in s:
    print(k)
b=vivo("Nikil","6","20000", "1")
m=b.features_vivo()
for k in m:
    print(k)




