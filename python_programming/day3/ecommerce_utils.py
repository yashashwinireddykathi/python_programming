def apply_discount(price,discount_percent):
    dprice=price-(price*discount_percent/100)
    return dprice
def add(price,gst_percent=18):
    gstp=price+(price*gst_percent/100)
    return gstp
def generate_invoice(cart,discount_percent=0,gst_percent=18):
    print("---INVOICE---")
    subtotal = 0
    for item, price in cart.items():
        print(f"{item:}: ₹{price}")
        subtotal += price
    print("---------------------------")
    print(f"Subtotal: ₹{subtotal}")
    subtotal_after_discount = apply_discount(subtotal, discount_percent)
    print(f"After {discount_percent}% discount: ₹{subtotal_after_discount:.2f}")
    total = add(subtotal_after_discount, gst_percent)
    print(f"After {gst_percent}% GST: ₹{total:.2f}")
    print("---------------------------")
    print("Thank You for shopping with us")