#esse ai eh pra ver qual o recorde de sequencias de azar considerando as 385 chaves disponibilizadas no site
import hashlib
rexe=hashlib.sha256()
arq=open("chaves.txt", "r")
recordeGeral=0
#aqui vc coloca qual o valor q vc considera preocupante e ele vai contar qtas vezes ele eh estourado
valorPreocupante=103
frequenciaPreocupante=0
cont=0
for line in arq:
	cont=cont+1
	recordeLocal=0
	contador=0
	linha=line.split()
	server_seed=linha[0]
	public_seed=linha[1]
	rounde=int(linha[2])
	roundefinal=int(linha[3])
	while(rounde<roundefinal):
		chave=server_seed+"-"+public_seed+"-"+str(rounde)
		rexe.update(chave)
		valor="0x"+rexe.hexdigest()
		roll=int(valor[0:8:], 0) % 15
		if(roll!=0):
			contador=contador+1
			if(contador>recordeLocal):
				recordeLocal=contador
		else: contador=0
		rounde=rounde+1
	if(recordeLocal>=valorPreocupante):frequenciaPreocupante=frequenciaPreocupante+1
	if(recordeLocal>recordeGeral):
		recordeGeral=recordeLocal
print "Recorde: ",recordeGeral
print "Sequencias preocupantes: ",frequenciaPreocupante," em ", cont
