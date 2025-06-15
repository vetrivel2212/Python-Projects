# 🛍️ Shopping Cart Program

products = {
    1: {"name": "T-shirt", "price": 499},
    2: {"name": "Jeans", "price": 999},
    3: {"name": "Shoes", "price": 1499},
    4: {"name": "Backpack", "price": 799},
    5: {"name": "Cap", "price": 199}
}

cart = {}

def show_products():
    print("\n🛍️ Available Products:")
    for pid, details in products.items():
        print(f"{pid}. {details['name']} - ₹{details['price']}")

def add_to_cart():
    show_products()
    try:
        pid = int(input("Enter product ID to add: "))
        if pid in products:
            qty = int(input("Enter quantity: "))
            if pid in cart:
                cart[pid] += qty
            else:
                cart[pid] = qty
            print(f"✅ {products[pid]['name']} x{qty} added to cart.")
        else:
            print("❌ Invalid Product ID.")
    except ValueError:
        print("❌ Enter valid numbers.")

def remove_from_cart():
    if not cart:
        print("🛒 Your cart is empty.")
        return
    view_cart()
    try:
        pid = int(input("Enter product ID to remove: "))
        if pid in cart:
            del cart[pid]
            print("✅ Product removed from cart.")
        else:
            print("❌ Product not in cart.")
    except ValueError:
        print("❌ Enter valid number.")

def view_cart():
    if not cart:
        print("🛒 Your cart is empty.")
        return
    print("\n🧾 Your Cart:")
    total = 0
    for pid, qty in cart.items():
        name = products[pid]['name']
        price = products[pid]['price']
        subtotal = price * qty
        print(f"{name} x{qty} = ₹{subtotal}")
        total += subtotal
    print(f"💰 Total Amount: ₹{total}")

def clear_cart():
    cart.clear()
    print("🧹 Cart cleared.")

def main():
    while True:
        print("\n==== 🛒 SHOPPING CART MENU ====")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Clear Cart")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            show_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            remove_from_cart()
        elif choice == '4':
            view_cart()
        elif choice == '5':
            clear_cart()
        elif choice == '6':
            print("🛍️ Thank you for shopping! Bye 👋")
            break
        else:
            print("❌ Invalid choice. Enter 1-6.")

if __name__ == "__main__":
    main()
