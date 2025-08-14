# programa com entradas para pessoa colocar medidas de paredes, num menu contínuo 
# e quando atingir a necessidade, o usuario pode clicar em sair e os calculos começam. 
# exibe medidas de todas as paredes e o total final da soma e do gasto de tinta.
# armazena as superficies em memorias separadas

# print("Digite abaixo as medidas das superfícies a serem calculadas. \n Digite: 0 para obter o resultado.")

# altura = float(input("Digite a altura da parede: "))
# largura = float(input("Digite a largura da parede: "))
# area = altura * largura
# tinta = area / 2

# print(f"A área da sua parede é {area}cm². Você necessita de {tinta} litros de tinta.")
# Você necessita de {tinta} litros de tinta."


menu = 0
area_total = []


while menu != 4:

  print("\n \
    1- Adicionar medidas\n \
    2- Adicionar próxima medida\n \
    3- Calcular total de tinta necessária\n \
    4- Encerrar sistema")
  
  menu = input("\nInsira a opção desejada:  \n")

  if menu == "":
    menu = 0

  if menu == "1":
    altura = float(input("Digite a altura da parede: "))
    largura = float(input("Digite a largura da parede: "))
    area = altura * largura  
    print(f"A área da sua parede é {area}cm².")

  if int(menu) == 2:
        served = next_client(priority_queue, general_queue)
        if served:
            print(f"Paciente atendido: {served}")
        else:
            print("Não existem pacientes aguardando atendimento.\n")    


  if menu == "3":
    tinta = area / 2
    print(f"A área da sua parede é {area}cm². Você necessita de {tinta} litros de tinta.")


  elif menu == 4:
    print("\nPrograma encerrado. Até a próxima!")
    break


menu == +1