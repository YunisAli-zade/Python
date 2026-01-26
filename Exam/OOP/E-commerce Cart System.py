def solution():
    # Import Enum from enum module
    from enum import Enum

    # Create ItemCategory Enum class
    class ItemCategory(Enum):
        ELECTRONICS = "Electronics"
        CLOTHING = "Clothing"
        FOOD = "Food"
        BOOKS = "Books"

    # Base Cart class
    class Cart:
        def __init__(self, cart_id: str):
            # Initialize __items to empty list
            self.__items = []
            # Store cart_id as protected attribute
            self._cart_id = cart_id
            # Set cart_type to "Standard"
            self.cart_type = "Standard"
            # Set total to 0.0
            self.total = 0.0
        def __validate_price(self, price: float) -> bool:
            # Check if price <= 0
            if price <= 0:
                # Raise ValueError
                raise ValueError("Price must be positive")
            # Return True if valid
            return True

        def add_item(self, category, price: float) -> bool:
            # Validate price
            self.__validate_price(price)
            # Add item to __items
            self.__items.append({"category": category, "price": price})
            # Add price to total
            self.total += price
            # Return True
            return True

        def get_total(self) -> float:
            # Return total
            return self.total

        def get_items(self, category=None):
            # If category is None, return all items
            if category is None:
                return self.__items
            # Otherwise filter by category
            return [item for item in self.__items if item["category"] == category]

    # PremiumCart inherits from Cart
    class PremiumCart(Cart):
        def __init__(self, cart_id: str, discount_rate: float):
            # Call parent constructor
            super().__init__(cart_id)
            # Store discount_rate as private attribute
            self.__discount_rate = discount_rate
            # Set cart_type to "Premium"
            self.cart_type = "Premium"

        def get_discounted_total(self) -> float:
            # Return total * (1 - __discount_rate)
            return self.total * (1 - self.__discount_rate)

        def add_item(self, category, price: float) -> bool:
            # Check if price >= 5
            if price < 5:
                # Raise ValueError
                raise ValueError("Premium cart requires minimum $5 items")
            # Call parent's add_item
            return super().add_item(category, price)

    # Return tuple
    return (ItemCategory, Cart, PremiumCart)
