# todo: make sure to add a library that copy the mac filtered automatically
def input_mac() -> str:
    ch = input("Enter a mac address: ")
    return ch

def filter_mac(ch:str) -> str:
    ch1 = ""
    for i in ch:
        if "0" <= i <= "9" or "A" <= i.upper() <= "Z":
            ch1 += i
    return ch1

ch = input_mac()
ch = filter_mac(ch)
print(f"Filtered mac is : {ch}")
