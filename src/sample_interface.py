class SampleInterface:
    """
    This is a sample interface.
    """
    def __init__(self) -> None:
        self.data = None

    def sample_module(self) -> None:
        """ This is a sample module."""
        self.data = {
            "name": "John"
        }
        return self.data
