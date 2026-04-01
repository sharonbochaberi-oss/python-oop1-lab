class Coffee:
    """Represents a coffee sold at the bookstore."""

    def __init__(self, size, price):
        """
        Initialize a Coffee object.

        Args:
            size (str): Size of the coffee ('Small', 'Medium', 'Large')
            price (float): Price of the coffee
        """
        self.size = size  # validated by setter
        self.price = price

    @property
    def size(self):
        """Return the size of the coffee."""
        return self._size

    @size.setter
    def size(self, value):
        """Ensure size is valid, print warning if not."""
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """
        Simulate tipping for the coffee.
        Prints a message and increases the price by 1.
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1