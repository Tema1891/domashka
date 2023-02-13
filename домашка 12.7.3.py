money = int(input('Сумма желаемого депозита : '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
procent = list(per_cent.values())

bankТКБ = round(procent[0]/100*money)
bankСКБ = round(procent[1]/100*money)
bankВТБ = round(procent[2]/100*money)
bankСБЕР = round(procent[3]/100*money)
deposit = [bankТКБ,bankСКБ,bankВТБ,bankСБЕР]
print('Возможный доход :', deposit)
deposit.sort()
print('Максимально возможная сумма :',max(deposit))