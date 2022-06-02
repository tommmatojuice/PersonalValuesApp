class Card:
    """
    Class describes the structure of a card
    """
    def __init__(self, card_id, title, path):
        """
        Initializing a card:

        :param card_id: card ID
        :param title: card title
        :param path: path to card in resources
        """
        self.id = card_id
        self.title = title
        self.path = path
