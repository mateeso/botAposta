import hashlib
#x=int("0xhexa", 0)
rexe=hashlib.sha256()
#rexe.update("valor")
server_seed="8d0bb9cf05d33a1960ac3375a5cb6430496bc6f60c62741121b16c0f77515e22"
public_seed="1415382710"
rounde=1461919
roundefinal=1465960
while(rounde<roundefinal):
	chave=server_seed+"-"+public_seed+"-"+str(rounde)
	rexe.update(chave)
	valor="0x"+rexe.hexdigest()
	roll=int(valor[0:8:], 0) % 15
	if(roll==0): saida=0
	elif(roll>=1 and roll<=7): saida=1
	else: saida=2
	print saida
	rounde=rounde+1
