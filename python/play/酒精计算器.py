
def get_ratio(number,totalNumber):
    value = number / totalNumber
    value = eval(format(value,'.2f'))
    return value

def main():
    print("酒精混合度数计算器\n")

    while True:
        tweight = 0

        print("\n开始录入基酒度数")
        content = input("请输入基酒度数(浮点数)：")
        content = eval(content)

        print("\n开始录入基酒重力")
        cweight = input("请输入基酒重力：")
        tweight = tweight + int(cweight)

        print("\n开始录入配酒重力")
        while True:
            weight = input("\n请输入配料重力（按q退出）：")
            if weight == 'q':
                break
            tweight = tweight + int(weight)

        r = get_ratio(int(cweight),tweight)
        r = r * content * 100
        r = format(r,'.2f')
        print("\n酒精度数：" + r + "%")
        print("摄入量：" + str(tweight))

main()
input()

