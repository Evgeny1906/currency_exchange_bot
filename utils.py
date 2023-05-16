import requests
import json
from config import keys
class ConvertionExeption(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def converter(amount: str, quote: str, base: str ):
        if quote == base:
            raise ConvertionExeption(f'Нельзя переводить {quote} в {base}!')
        try:
            quote_tiker = keys[quote.lower()]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')
        try:
            base_tiker = keys[base.lower()]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Некоректное количество {amount}')
        conv = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={base_tiker}&from={quote_tiker}&amount={amount}",
            {"apikey": "SI2SpTWlVkf4kK9pW8PzBHSRzKT3Pfeb"})
        result = json.loads(conv.text)
        text = f"Дата: {result['date']} \n 1{quote_tiker}={result['info']['rate']}{base_tiker} \n Общий результат-{result['result']}"

        return text
