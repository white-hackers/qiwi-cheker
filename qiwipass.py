import pyqiwi

with open('qiwi.txt', 'r') as qiwi:
    for qiwi in qiwi:
        qiwi = qiwi.split(":")
        try:
            wallet = pyqiwi.Wallet(token=qiwi[2], number=qiwi[0])
            print(f'Номер {qiwi[0]} имеет на балансе: {wallet.balance()}')
        except Exception as e:
            pass