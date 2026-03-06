a = float(input("Please tell me the VOO value: "))
b = float(input("Please tell me the QQQ value: "))
c = float(input("Please tell me the SMH value: "))
d = float(input("Please tell me the SGOV value: "))
e = float(input("Please tell me the IBIT value: "))
f = float(input("Please tell me the BOTZ value: "))
x = a + b + c + d + e

if ((a/x) <= 0.45 and (a/x) >= 0.35) and ((b/x) <= 0.3 and (b/x) >= 0.2) and ((c/x) <= 0.15 and (c/x) >= 0.05) and ((d/x) <= 0.15 and (d/x) >= 0.05) and  ((e/x) <= 0.15 and (e/x) >= 0.05) and ((f/x) <= 0.1 and (f/x) >= 0):
    print("All is good. This year u don't need to adjust!")
else:
    if (a/x) > 0.45:
        a1 = a - 0.4 * x
        print(f"VOO sells {a1}")
    elif (a/x) < 0.35:
        a1 = 0.4 * x - a
        print(f"VOO buys {a1}")
    else:
        print(f"VOO is ok.")
    if (b/x) > 0.3:
        b1 = a - 0.3 * x
        print(f"QQQ sells {b1}")
    elif (b/x) < 0.2:
        b1 = 0.3 * x - b
        print(f"QQQ buys {a1}")
    else:
        print(f"QQQ is ok.")

    if (c/x) > 0.15:
        c1 = c - 0.1 * x
        print(f"SHM sells {c1}")
    elif (c/x) < 0.05:
        c1 = 0.1 * x - c
        print(f"SHM buys {c1}")
    else:
        print(f"SHM is ok.")
    if (d/x) > 0.15:
        d1 = d- 0.1 * x
        print(f"SGOV sells {d1}")
    elif (d/x) < 0.05:
        d1 = 0.1 * x - d
        print(f"SGOV buys {d1}")
    else:
        print(f"SGOV is ok.")
    if (e / x) > 0.15:
        e1 = e - 0.1 * x
        print(f"IBIT sells {e1}")
    elif (e / x) < 0.05:
        e1 = 0.1 * x - e
        print(f"IBIT buys {e1}")
    else:
        print(f"IBIT is ok.")
    if (f/x) > 0.1:
        f1 = f - 0.05 * x
        print(f"BOTZ sells {f1}")
    elif  (f/x) < 0:
        f1 = 0.05 * x - f
        print(f"BOTZ buys {f1}")
    else:
        print(f"BOTZ is ok.")