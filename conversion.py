from forex_python.converter import CurrencyRates, CurrencyCodes

codes = CurrencyCodes()
rates = CurrencyRates()


class Conversion:
    """Creates all necessary information for conversion between two currencies"""

    def __init__(self, curr_from, curr_to):
        """Calls forex_python methods to create all information about currencies"""

        self.curr_from = curr_from if self.__valid_code__(
            curr_from) else None
        self.curr_to = curr_to if self.__valid_code__(
            curr_to) else None
        self.rate = self.__get_rate__() if self.curr_from and self.curr_to else 0

    def __valid_code__(self, code):
        """Checks provided code with forex_python to make sure it represents a valid currency"""

        if codes.get_currency_name(code):
            return True
        else:
            return False

    def __get_rate__(self):
        """Gets exchange rate of two currencies"""

        rate = rates.get_rate(self.curr_from, self.curr_to)

        return rate

    def __get_symbol__(self):
        """Gets currency symbol from the curr_to property and forex_python"""

        symbol = codes.get_symbol(self.curr_to)

        return symbol

    def convert_amount(self, amount):
        """Converts a value using self.rate exchange rate"""

        converted = round((int(amount) * self.rate), 2)
        num_with_symbol = self.__get_symbol__() + str(converted)

        return num_with_symbol
