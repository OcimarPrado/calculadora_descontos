print('======================================')
print(' Bem-vindo à Loja do Ocimar Prado!')
print('======================================')
print('Simule aqui o desconto conforme o valor total:')
print('- Até R$ 2.500,00 → sem desconto')
print('- De R$ 2.500,00 a R$ 6.000,00 → 4% de desconto')
print('- De R$ 6.000,00 a R$ 10.000,00 → 7% de desconto')
print('- Acima de R$ 10.000,00 → 11% de desconto')
print('--------------------------------------\n')

valor = float(input('Entre com o valor unitário do produto (R$): '))
qtdd = int(input('Entre com a quantidade desejada: '))
total = valor * qtdd

if total < 2500:
    desc = 0
    desconto_pct = 0
elif 2500 <= total < 6000:
    desc = total * 0.04
    desconto_pct = 4
elif 6000 <= total < 10000:
    desc = total * 0.07
    desconto_pct = 7
else:
    desc = total * 0.11
    desconto_pct = 11

total_com_desconto = total - desc

print(f'\nDesconto aplicado: {desconto_pct}%')
print(f'Valor SEM desconto: R${total:.2f}')
print(f'Valor COM desconto: R${total_com_desconto:.2f}')
