import sys
import chat

config = {
	"input": "> ",
	"obrigatorio": True,
	"respostaInvalida": "Escolha algo válido!",
	"respostaObrigatoria": "Escolha algo válido!"
}

def fight():
	print("Você deu um soco no monstro! [7 de dano]")
	ask()

def run():
	print("Você fugiu! [+0 xp]")
	ask()

def saveAndExit():
	print("Salvando...")
	sys.exit()

def ask():
	respostas = [{"text": "Lutar", "on": fight}, {"text": "Fugir", "on": run}, {"text": "Sair do jogo", "on": saveAndExit}]
	chat.ask("O que você quer fazer?", respostas, config)

ask()