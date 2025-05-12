menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print (menu)
    opcao = input("Escolha uma opção ou aperte s para sair: ")
    
    if opcao == 'd':
        valor_dep = int(input("Digite o valor para depositar: R$"))
        
        if valor_dep < 0:
            print ("Valor inválido")
            
        else:
            saldo += valor_dep
            print (f"Seu saldo atual é R$ {saldo}")
            
