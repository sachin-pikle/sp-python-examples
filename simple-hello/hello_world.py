def main():
    print("Hello, World!")

    ## Debug quickly using f strings
    user_id = "User One"
    order_total = 78.99
    discount_applied = 10
    print(f"{user_id=}, {order_total=}, {discount_applied=}")

    ## Eliminate temporary variables with expressions in f strings
    print(f"Discount amount: {order_total * discount_applied / 100}")
    print(f"Username: {user_id.upper()}")
    limit = 50
    used = 49
    print(f"Items remaining: {max(limit - used, 0)}")

if __name__ == "__main__":
    main()
