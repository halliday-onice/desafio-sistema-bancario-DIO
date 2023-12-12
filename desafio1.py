menu = " """""

 [d] depositar
 [s] sacar
 [e] extrato
 [q] sair


" """""

saldo = 0
limite = 5000
extrato = " "
num_saques = 0
LIMITE_SAQUES = 3


while True:
      print("Digite a operacao desejada")
      opcao = input()

      if opcao == "d":
            valor = float(input("informe o valor do deposito: "))

            if valor  > 0:
                  saldo += valor
                  extrato = f"Deposito de: R${valor:.2} realizado com sucesso\n"
            else:
                  print("Operacao invalida porque saldo eh menor que zero")
      if opcao == "s":
            valor = float(input("informe o valor do saque: "))
            # precisa existir tres verificacoes: i) ver se excedeu saque
            # ii) ver se excedeu limite
            # iii) ver se excedeu os saques
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = num_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                  print("Saldo insuficiente")
            elif excedeu_limite:
                  print("O valor do saque excede o limte")
            elif excedeu_saques:
                  print("Numero de saques maximo excedido")
            
            elif valor > 0:
                  saldo -= valor
                  extrato += f"Saque R$ {valor:.2f}\n"
                  num_saques += 1
            else:
                  print("Valor invalido")
      elif opcao == "e":
            print("\n ================ EXTRATO =================\n")
            print("Nao foram realizados movimentacoes" if not extrato else extrato)
            print(f"Saldo: R$ {saldo: .2f}\n")
            print("=====================================")
      elif opcao == "q":
            break
      else:
            print("Operacao Invalida")
      
            
