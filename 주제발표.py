from function import *
print('='*50)
print('경우의 수 계산기 제작자:박규현')
print('='*50)
while True:
    print('뽑는 순서를 고려할까요?')
    mode=input('[y/n] ')
    if mode=='y':
        print('n개 중 m개를 뽑습니다. n값과 m값을 입력해주세요.')
        try:
            n=int(input('n: '))
            m=int(input('m: '))
        except:
            print('장난치지 마요... 다시!\n')
            continue
        result='%d개 중 %d개를 뽑고 순서를 생각하는 경우의 수는 %d가지 입니다.' %(n, m, perm(n,m))
        print(result)
        break
    elif mode=='n':
        print('n개 중 m개를 뽑습니다. n값과 m값을 입력해주세요.')
        try:
            n=int(input('n: '))
            m=int(input('m: '))
        except:
            print('장난치지 마요... 다시!\n')
            continue
        result='%d개 중 %d개를 뽑고 순서를 생각하지 않는 경우의 수는 %d가지 입니다.' %(n, m, com(n,m))
        print(result)
        break
    else:
        print('다시 시도해주세요!\n')
        continue
input()
