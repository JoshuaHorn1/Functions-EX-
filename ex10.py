def calc_get(net_price):
    return net_price * 1.15


# main
num_ = int(input("Enter your amount ($): "))
print(f"${calc_get(num_):.2f}")
