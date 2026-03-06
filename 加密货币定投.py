num = float(input("多少U投入到加密货币中？"))
a = 0.7 * num * 0.5
b = 0.3 * num
print(f"Buy BTC and ETH {a}U, USTD {b}U")
BTC = float(input("How many BTC?"))
ETH = float(input("How many ETH?"))
c = BTC * 0.8
d = ETH * 0.8
print(f"Transfer BTC {c}, Transfer ETH {d},2000U 转1600U入冷钱包 剩下留着吃利息。")


