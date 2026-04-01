class Book:
    """Represents a book in the bookstore."""

    def __init__(self, title, page_count):
        """
        Initialize a Book object.

        Args:
            title (str): Title of the book
            page_count (int): Number of pages in the book
        """
        self.title = title
        self.page_count = page_count  # validated by setter

    @property
    def page_count(self):
        """Return the number of pages."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Ensure page_count is an integer, print warning if not."""
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Simulate turning a page in the book."""
        print("Flipping the page...wow, you read fast!")