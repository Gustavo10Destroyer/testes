import random

def ask(pergunta, respostas, configuracoes):
	print(pergunta)

	for resposta in respostas:
		print(resposta["text"])

	resposta = input(configuracoes["input"])

	if resposta:
		try:
			resposta = int(resposta)

			print("Você respondeu: "+respostas[resposta - 1]["text"])
			if respostas[resposta - 1]["on"]:
				respostas[resposta - 1]["on"]()

			else:
				return respostas[resposta - 1]
		except Exception:
			print(configuracoes["respostaInvalida"])
			return ask(pergunta, respostas, configuracoes)
	else:
		if configuracoes["obrigatorio"]:
			print(configuracoes["respostaObrigatoria"])
			return ask(pergunta, respostas, configuracoes)
		else:
			resposta = random.randint(0, len(respostas) - 1)
			print("Você respondeu: "+respostas[resposta]["text"])

			if respostas[resposta]["on"]:
				respostas[resposta]["on"]()