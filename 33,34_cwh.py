#Program to illustrate dictionaries in python
# item_prices={
#     10:300,
#     20:255,
#     30:200,
#     50:500
# }
# item=int(int(input("Enter Item no .")))
# if item in item_prices.keys():
#     print(f"The price of this item is Rs{item_prices[item]}")
# else:
#     print("Please enter valid item number")
#Go through documentation time to time
ep1={22:80,11:55,18:69}
ep2={16:67,19:77}
ep1.update(ep2)
print(ep1)

