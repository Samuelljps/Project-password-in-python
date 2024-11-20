# Criar um sistema de celular que acabou de ser comprado.


# 1 - o sistema deve cadastrar o pin inicial 
# 2 - após o cadastro do pin, deve pedir cadastro de senha
# 3 - e só após a validação, que o usuario tera acesso ao sistema do celular
# Expecificações:  na confirmacao do pin quero while
# ===============================================================================================




#O while verifica a condição antes de cada iteração(REPETIÇÃO).
print("====CELULAR NOVO====")
while True:
    pin = input("Cadastre um PIN inicial, contendo apenas números: ")

    # Verificar se todos os caracteres no PIN são números
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    eh_numero = True

    for caractere in pin:
        if caractere not in numeros:
            eh_numero = False
            break  # Não precisamos verificar mais nada se um caractere já for inválido

    if eh_numero:
        print("PIN cadastrado com sucesso!")
        break
    else:
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
for tentativas in range(4):
    senha_cadastrada = input("Informe a senha cadastrada: ")
    if senha_cadastrada != senha:

        if tentativas ==0:
            print("Acesso negado, tentativas(1/3)")
            
        if tentativas ==1:
            print("Acesso negado, tentativas(2/3)")
        if tentativas ==2:
            print("Acesso negado, tentativas(3/3)")
            
        if tentativas ==3: 
            print("Acesso bloqueado! Numero de tentativas excedido.")

    else:
        print("Acesso permitido!")
        break
