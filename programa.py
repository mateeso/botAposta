import pyautogui, sys, time
from random import randint

#posicao do seu dinheiro na tela
xgrana=778
ygrana=460

#array que vai armazenar as posicoes dos 2 botoes win2x
xbotao=range(2)
ybotao=range(2)
#posicao do primeiro botoao win2x
xbotao[0]=488
ybotao[0]=640
#posicao do segundo botao win2x
xbotao[1]=976
ybotao[1]=640
#posicao do terminal, de preferencia no canto da tela
xterminal=1243
yterminal=154
#posicao de um campo vazio simplesmente para poder desmarcar os caracteres selecionados
xvazio=761
yvazio=167
#posicao botoes de aposta
#botao clear
xbotaoClear=420
ybotaoClear=550
#botao +0.01
xbotao001=494
ybotao001=550
#botao de dobrar a aposta
xbotao2x=971
ybotao2x=550

#LISTA DE FUNCOES
#funcao que retorna o valor da carteira
def valorCarteira():
#clica no vazio para desmarcar qualquer item selecionado
	pyautogui.click(x=xvazio, y=yvazio, clicks=1)
#3 cliques no lugar onde esta falando o dinheiro da carteira para selecionar
	pyautogui.click(x=xgrana, y=ygrana, clicks=3)
#executa ctrl+c
	pyautogui.hotkey('ctrl', 'c')
#clica no vazio dnv por precaucao
	pyautogui.click(x=xvazio, y=yvazio, clicks=1)	
#clica no terminal para poder inserir os dados copiados
	pyautogui.click(x=xterminal, y=yterminal, clicks=1)	
#no terminal o comando para colar eh shift+ctrl+v
	pyautogui.hotkey('shift', 'ctrl', 'v')
#da enter para enviar a entrada para o buffer
	pyautogui.press('enter')
#le o buffer do teclado e passa a saida para a variavel carteira
	carteira=raw_input()
	carteira=carteira.replace(',','.')
#como os dados serao a linha inteira, por ex: Balance: 0.00, e so queremos
#os dados a partir do 9 caractere, vamos selecionar somente a partir dele
#e converter o valor para o tipo ponto flutuante (float) que eh o tipo dos numeros decimais
	carteira=float(carteira[9::])
	return carteira
def limpa():
#funcao para clicar no botao clear
	pyautogui.click(x=xbotaoClear, y=ybotaoClear, clicks=1)
def colocar001():
#funcao para clicar no botao para add + 0.01 reais
	pyautogui.click(x=xbotaoClear, y=ybotaoClear, clicks=1)
	pyautogui.click(x=xbotao001, y=ybotao001, clicks=1)
def dobra():
#funcao para clicar no botao para dobrar a aposta
	pyautogui.click(x=xbotao2x, y=ybotao2x, clicks=1)
def apostar():
#funcao para clicar em um dos botoes para apostar
#os botoes sao selecionados randomicamente
	num=randint(0, 100) % 2
	pyautogui.click(x=xbotao[num], y=ybotao[num], clicks=1)

print('Press Ctrl-C to quit.')

try:
#indica q as variaveis x e y serao as cordenadas reais do mouse
	x, y = pyautogui.position()
#armazena o valor 0.0 na variavel que vai guardar o valor inicial da carteira
#simplesmente para iniciar o processo
	carteira0=0.0
#loop infinito
	while True:
#pega o valor da carteira e passa para a variavel carteira
		carteira=valorCarteira()
#se o valor for 0, o processo eh morto
		if(carteira==0.0):
			print("Nao tem porra nenhuma no caixa.\n")
			break
#se nao e caso o valor da carteira seja diferente do valor inicial
#executa outro bloco. isso eh para identificar quando houve o fim de uma aposta
		elif(carteira != carteira0):
#se o valor da carteira atual for mairo q o inicial, ou seja, se vc ganhou
#limpa as apostas e aposta +0.01
			if(carteira > carteira0):
				limpa()
				colocar001()
				apostar()
#se for menor, dobra a aposta
			elif(carteira < carteira0):
				dobra()
				apostar()
#atualiza o valor da carteira inicial, que sera comparado futuramente
#para ver se houve alteracao
		carteira0=carteira
#deixa o programa pausado por 1 segundo para n arrebentar sua cpu
		time.sleep(1)
#procedimento de saida do programa
except KeyboardInterrupt:
		print '\n'
