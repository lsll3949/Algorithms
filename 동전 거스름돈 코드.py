def coin_change(don):
    coin = [500, 100, 50, 10, 5, 1]
    count = 0
    for i in range(len(coin)):
        count = don // coin[i]
        don = don % coin[i]
        if count != 0:
            print('{:3}원짜리 동전: {:2}개'.format(coin[i], count))
            
change = input('거스름돈을 입력하시오: ')
coin_change(int(change))