import requests


def currency_with_max_rate():
    """Returns the name of the currency with the maximum exchange rate
    """
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']

    return max(response.values(), key=lambda v: v['Value'])['Name']


class Rate:
    def __init__(self, format_='value'):
        self.format = format_

    def exchange_rates(self):
        """Returns the service response with information about currencies in the form:
        {
            "AUD": {
                "ID": "R01010",
                "NumCode": "036",
                "CharCode": "AUD",
                "Nominal": 1,
                "Name": "Австралийский доллар",
                "Value": 53.2166,
                "Previous": 54.0499
            },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        """Returns information about currency in two forms:
        1. Full information about the currency for self.format = 'full':
        {
            "ID": "R01239",
            "NumCode": "978",
            "CharCode": "EUR",
            "Nominal": 1,
            "Name": "Евро",
            "Value": 88.3712,
            "Previous": 90.2023
        }
        2. Currency value for the current date for self.format = 'value',
        if self.diff = False:
        90.2023

        or the difference(formatted 0.0000) between the current exchange rate and the previous one,
        if self.diff = True:
        -1.8311
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            elif self.format == 'value':
                if self.diff:
                    return response[currency]['Value'] - response[currency]['Previous']
                else:
                    return response[currency]['Value']

        return 'Error'

    def eur(self, diff=False):
        """Returns euro exchange rate on the current date in the format self.format"""
        self.diff = diff
        return self.make_format('EUR')

    def usd(self, diff=False):
        self.diff = diff
        """Returns dollar exchange rate on the current date in the format self.format"""
        return self.make_format('USD')


def main():
    print(f'Валюта с максимальным значением курса: {currency_with_max_rate()}')

    r_1 = Rate('full')
    print(r_1.usd())

    r_2 = Rate()  # default format_='value'
    value_usd = r_2.usd()
    diff = r_2.usd(True)
    print(f'Текущий курс доллара: {value_usd}, изменение курса: {diff:.4f}')

    value_eur = r_2.eur()
    print(f'Текущий курс евро: {value_eur}')


main()
