from datetime import datetime


def nithil(t1, t2):
    format1 = '%a %d %b %Y %H:%M:%S %z'
    return int(abs((datetime.strptime(t1, format1) - datetime.strptime(t2, format1)).total_seconds()))

if __name__ == '__main__':

    time = int(input())

    for i in range(time):
        t1 = input()
        t2 = input()
        print(nithil(t1, t2))
