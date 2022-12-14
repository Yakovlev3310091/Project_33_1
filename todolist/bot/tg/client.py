import requests

from bot.tg.dc import GetUpdatesResponse, SendMessageResponse, get_updates_schema, send_message_schema


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str):
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        response = requests.get(self.get_url(f"getUpdates?offset={offset}&timeout={timeout}"))
        json_data = response.json()

        for result in json_data['result']:
            if not result.get('message', None):
                json_data['result'].remove(result)

        for result in json_data['result']:
            result['message']['from_'] = result['message'].pop('from')

        result = get_updates_schema().load(json_data)
        return result

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        response = requests.get(self.get_url(f"sendMessage?chat_id={chat_id}&text={text}"))
        json_data = response.json()
        json_data['result']['from_'] = json_data['result'].pop('from')
        result = send_message_schema().load(json_data)
        return result