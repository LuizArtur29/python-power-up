lista_nomes = ["lira", "jorge", "gi", "renan"]
lista_nomes.append("julia")
print(lista_nomes)

primeiro_item = lista_nomes[0]
print(primeiro_item)


mensagem = {"role": "user", "content": "Coe galera"}

texto_mensagem = mensagem["role"]
print(texto_mensagem)

lista_mensagens = [
    {"role": "user", "content": "Coe galera"}, 
    {"role": "assistant", "content": "Resposta da IA"}, 
    {"role": "user", "content": "Tamo junto"}
    ]

lista_mensagens.append(
    {"role": "assistant", "content": "Eu desisto de você"}
)

print(lista_mensagens)

for nome in lista_nomes:
    print(nome)

for mensagem in lista_mensagens:
    print(mensagem)