prices = {
    "Pepsi": 170000,
    "Coca": 175000,
    "Mirinda": 125000,
    "Xá xị": 115000,
    "Fanta trái cây": 165000,
    "Sting": 165000
}
quantities = {}
for item in prices:
    quantity = int(input(f"Nhập số lượng {item}: "))
    quantities[item] = quantity

def cal_total_amount(prices, quantities):
    total_amount = 0
    for item in prices:
        total_amount += prices[item] * quantities[item]
    return total_amount;
def cal_discount(total_amount):
    if total_amount > 500000:
        return total_amount * 0.05
    return 0
def main():
    total_amount = cal_total_amount(prices, quantities)
    discount = cal_discount(total_amount)
    final =  total_amount - discount
    for item in prices:
        price = prices[item]
        quantity = quantities[item]
        total_price = price * quantity
        print(f"{item}: {quantity} thùng x {price:,} đồng = {total_price:,} đồng")
    print(f"Tổng tiền: {total_amount:,} đồng")
    print(f"Giảm giá: {discount:,} đồng")
    print(f"Tổng cộng: {final:,} đồng")
if __name__ == "__main__":
    main()