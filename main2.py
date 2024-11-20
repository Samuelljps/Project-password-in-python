# Criar um sistema de celular que acabou de ser comprado.


# 1 - o sistema deve cadastrar o pin inicial 
# 2 - após o cadastro do pin, deve pedir cadastro de senha
# 3 - e só após a validação, que o usuario tera acesso ao sistema do celular
# Expecificações:  na confirmacao do pin quero while
# ===============================================================================================




#O while verifica a condição antes de cada iteração(REPETIÇÃO).
print("====CELULAR NOVO====")
while True:
    pin = input("Cadastre uma PIN inicial, contendo apenas números: ")

    if pin.isdigit(): # A função "".isdigit" é usado para restringir ao usuario a inputar apenas strings com numeros inteiros.
        #se o codigo estiver dentro do parametro dado pela função .isdigit 
        print("PIN cadastrado com sucesso!") #o programa ira printar essa mensagem.
        break #e ira parar com o uso do break
    else: #caso não siga a função dada pelo .isdigit o codigo ira retornar a mensagem que o usuario deve usar apenas numero para inputar.
        print("Use apenas números para o PIN. Tente novamente.")

while True:
    senha = input("Digite uma senha diferente do PIN podendo ter letras e numero: ")
    if pin != senha:
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("A senha deve ser diferente do PIN escolhido anteriormente. Tente novamente: ")
        

 #=======================================================================================================
tentativas = 0
for tentativas in range(3):
    senha_cadastrada = input("Informe a senha cadastrada: ")
    if senha_cadastrada != senha:
        print("Acesso negado!")
    else:
        print("Acesso permitido!")
        break
else:
    print("Acesso bloqueado.")




