import os

class component:
    def __init__(self,uid):
        self.uid=int(uid)
        if self.uid >=70000000 and self.uid < 81000000:
            self.version='44'
            self.medium='8'
        elif self.uid >=81000000:
            self.version='52'
            self.medium='8'
        elif self.uid > 40000000 and self.uid < 50000000:
            self.version='20'
            self.medium='8'
        elif self.uid >= 50000000 and self.uid < 60000000:
            self.version='65'
            self.medium='6' ##Potrebbe essere un errore!
        else:
            self.version='xxx'
            self.medium='xxx'
    def __str__(self):
        string='LSE'+'\t'+str(self.uid)+'\t'+self.version+'\t'+self.medium+'\n'
        return string

def plt_writer(csv,cond,col):
    file=open(csv,'r')
    mappatura=file.readlines()
    rip=list()
    tmp=list()
    for i in mappatura:
        try:
            tmp.append(i.split('\t')[col-1])
        except IndexError:
            pass
            ##print 'Index Error: controllare file plt, potrebbe essere errato.'
    for i in tmp:
        try:
            int(i)
        except:
            pass
        else:
            rip.append(component(i))                       
    plt=open(cond , 'w')
    plt.write('[PLANT]\n')
    plt.write('Number\tManufacturer\tDevice ID\tFabrication No.\tVersion\tMedium\n')
    c=0
    for i in rip:
        c+=1
        if len(str(c))==1:
            num='00'+str(c)
        elif len(str(c))==2:
            num='0'+str(c)
        else:
            num=str(c)
        plt.write(num+'\t'+str(i))
    plt.close()
    file.close()
    print 'PLT FILE HAS BEEN WRITTEN'
    return True

def main():
    csv=raw_input('Inserisci file .csv-> ')
    cond=raw_input('Inserisci nome condominio-> ')
    while True:
        try:
            tmp=raw_input('Inserisci colonna ripartitori in csv-> ')
            col=int(tmp)
        except ValueError:
            print 'Inserisci un intero!'
        else:
            break
        
    plt_writer(csv,cond,col)
    os.system('pause')
    

if __name__=='__main__':
    setup(console=['PLT Generator v1.0 BETA.py'])
    main()
    













        
