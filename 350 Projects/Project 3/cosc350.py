class Queue:
    """
    A queue is a container that organizes data
    using a first-in, first-out discipline
    """

    def __init__(self):
        """
        Initialize a new queue to be empty
        """
        self.items = []

    def is_empty(self):
        """
        Determine whether this queue is empty
        :return: True if this queue contains no items,
                 False otherwise
        """
        return self.items == []

    def enqueue(self, item):
        """
        Add an item to this queue
        :param item: any object
        :return: None
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Remove the oldest item from this queue
        :return: The oldest item in this queue after it
                 has been removed
        """
        return self.items.pop()

    def size(self):
        """
        Queue size
        :return: the number of items in this queue
        """
        return len(self.items)
