ch = "HELLO   WORE, IT'S CALLED              MELEK"
i = 0
while ch.find("  ") != -1:
    i += 1
    m1 = ch[ : ch.find("  ")]
    m2 = ch[ch.find("  ")+1 : ]
    ch = m1 + m2
    print("i="+ str(i) + ", " + ch)
print(ch, ch.find("  "))

