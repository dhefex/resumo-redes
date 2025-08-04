from pywebio.input import select 
from pywebio.output import put_text
from pywebio import start_server 

def opcao():
	option = select("Escolha a aula:", options=["class1","class2","quit"])
	
	if option == "class1":
		mode = open("class1.txt", "r")
		content = mode.read()
		mode.close()

		put_text("Show content")
		put_text(content)
		
	elif option == "class2":
		mode2 = open("class2.txt", "r")
		content = mode2.read()
		mode2.close()

		put_text("Show content")
		put_text(content)

	elif option == "sair":
		put_text("exit...")





start_server(opcao, port=8086)
