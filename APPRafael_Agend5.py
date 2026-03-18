print('<<<<<<<<<<<<<<<<<<<<<<CONSUMO MENSAL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
aparelho = input('Informe o aparelho a ser consultado: ')
aparelho_walts = float(input('Informe a potência do aparelho em walts (W): '))
tempo_diario = float(input('Informe o tempo médio de uso diário em horas: '))
consumo_mensal = (aparelho_walts * tempo_diario * 30) / 1000
valor_fixo = float(0.75)
custo_estimado = consumo_mensal * valor_fixo

print(f'AparelhO {aparelho}')
print(f'Consumo estimado {consumo_mensal} KWh/mês')
print(f'O custo estimado vai ser no valor de R${custo_estimado: .2f} mensal')