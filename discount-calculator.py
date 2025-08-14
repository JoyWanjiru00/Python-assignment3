def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the final price after applying a discount.
    If discount is less than 20%, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# User input
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    if final_price != original_price:
        print(f"Final price after discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
