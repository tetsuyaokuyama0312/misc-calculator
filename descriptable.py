from abc import ABC, abstractmethod


class Descriptable(ABC):
    """
    Interface indicating that it is an descriptable object
    """

    @abstractmethod
    def description(self):
        """
        Returns a description of this object

        :return: a description of this object
        """
        pass
