#Ricordare che come vincolo, al momento, i nomi degli appartamenti non possono essere uguali.
#Cio' fa in modo che ogni interno abbia effettivamente un nome unico.
#Prossimamente ad ogni interno assegnerò un identificativo unico nel sistema del condominio.
#Con annesse le implementazioni per quanto riguarda interno e piano; anche se dubbie perche se
#nel file di maschera che viene dato in pasto gli interni non sono in ordine o comunque hanno variazioni(basti pensare a tutte quelle persone
#che hanno appartamenti su due piani in un condominio e quindi piu di un interno )

#Prossimo step: -Scrittura ordinata su file
#			    -Selezione dei due file da interfaccia grafica
#				-Unione con il programma per calcolo di plt,magari piu di una window


class Interno:
	def __init__(self):
		self.interno=int()
		self.piano=int()
		self.id=str()
		self.contatori=str()
		self.cons=str()

	def __str__(self):
		return '{}\t{}\t{}\n'.format(self.id,self.contatori,self.cons)




list_int=list()
csv = '/media/leonardo/ZINI_USB/PLT generator/masch.csv'
with open(csv,'r') as f:
	varnom=''
	for i in f.readlines():
		if i.split('\t')[0]!='':
			tmp=Interno()
			tmp.id=i.split('\t')[0]		#nome
			varnom=tmp.id
			tmp.contatori=i.split('\t')[2]
			list_int.append(tmp)
		else:
			tmp=Interno()
			tmp.id=varnom
			tmp.contatori=i.split('\t')[2]
			list_int.append(tmp)




dict_sn=dict()
lettura='/media/leonardo/ZINI_USB/PLT generator/lettura.csv'
with open(lettura,'r') as f:
	for i in f.readlines():
		try:
			lect= i.split('\t')[17]
			sn=i.split('\t')[5]
			dict_sn[sn]=lect
			list_lect.append(tmp_dict)
		except:
			pass


for i in list_int:
	for y in dict_sn.keys():
		if i.contatori == y:
			i.cons=dict_sn[y]

tmpold=''
for i in list_int:
	if i.id == tmpold:
		i.id=''
	else:
		tmpold=i.id

for i in list_int:
	print i
