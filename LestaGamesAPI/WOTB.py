"""
Методы для обращения к информации "Tanks Blitz"
"""

from . import Constants
from . import Application


NAME = "wotblitz"
SERVER = "wotblitz.ru"
API_SERVER = "api.wotblitz.ru"
API_NAME = "wotb"
READABLE = "Tanks Blitz"


class Account:
    def __init__(self, application_id: str) -> None:
        """
        Инициализация методов для работы с Аккаунтом игрока

        :param application_id   ID приложения Lesta Games, с которого будет производится запрос
        """
        self.application_id = application_id
        self.app = Application.App(self.application_id)

        self.class_methods = [method for method in dir(Account) if method.startswith('_') is False]

        self.method_urls = dict()
        for method in self.class_methods:
            self.method_urls[method] = Constants.PATTERN_URL.format(
                server=API_SERVER,
                api_name=API_NAME,
                method_block=__class__.__name__.lower(),
                method_name="list",
                get_params="{get_params}"
            )

    def list(self, search: str, **kwargs) -> dict:
        """
        Метод возвращает часть списка игроков, отфильтрованную по первым символам имени и отсортированную по алфавиту.

        :param search       Строка поиска по имени игрока. Вид поиска и минимальная длина строки поиска зависят от параметра type. При использовании типа поиска exact можно перечислить несколько имён для поиска, разделив их запятыми. Mаксимальная длина: 24.

        Необязательные поля
        :param fields       Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        :param language     Язык локализации.
        :param limit        Количество возвращаемых записей (может вернуться меньше записей, но не больше 100).
        :param type         Тип поиска.

        Подробнее о методе: [lesta.ru](https://developers.lesta.ru/reference/all/wotb/account/list/)
        """

        request_url = self.method_urls["list"].format(get_params=Application.Query(
            application_id=self.application_id, search=search, **kwargs).string)
        return Application.App().execute("GET", request_url)
