import matplotlib.pyplot as plt
import sys
#esse eh um dia q chega a 121 vezes sem sair dado
arq=open("saida1.txt", "r")
#a ideia eh:
#o valor ganho a cada aposta deve cobrir as anteriores e faturar 13 cents
#logo:
#14*aposta=somaApostasAnteriores+13
#aposta=somaApostasAnteriores+13
aposta=1
somaApts=0
caixa=int(sys.argv[1])
data=[0]*4050
data2=[0]*4050
i=0
freqAzar=0

for line in arq:
	valor=int(line)	
	if(valor==0):
		caixa=caixa+14*aposta
		aposta=1
		somaApts=0
		freqAzar=0
		print caixa," GANHOU"
	else:
		caixa=caixa-aposta
		somaApts=somaApts+aposta
#esse 13 pode ser alterado pra ficar melhor
		aposta=(13+somaApts)/14
		freqAzar=freqAzar+1
		print caixa,"\t",freqAzar
		if(caixa<=0):
			print "AI MEU CU"
			break
	data[i]=caixa
	data2[i]=freqAzar
	i=i+1
plt.plot(data, color="green")
plt.plot(data2, color="blue")
plt.xlim(0,i-1)
plt.show()
arq.close()
