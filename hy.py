name=input("姓名:")
print('嗨!',name)
a = int(input('今天有沒有下雨? 0：無，1：有'))
if a == 1:
    print('留在家裡吧!')
b = float(input('今天氣溫攝氏幾度?'))
b = b * 9 / 5 + 32
print('華氏:', b, '度')