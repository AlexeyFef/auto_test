import requests


class CreateJokeTestCategory:
    """Класс включающий сценарии по отправке запросов, с целью получения шуток с Чаком Норрисом по всем категориям"""


    base_url = "https://api.chucknorris.io/jokes/"      # cоздаем base_url
    list_categories = []                                # создание пустого списка категорий


    def test_get_categories(self):
        """Тест по получению всех категорий шуток, включает:
            отправку запроса, проверка статус-кода ответа,
            проверка на непустой список с категориями,
            печать списка категорий,
            запись списка категорий в переменную для дальнейшего использования в коде,
            печать количества категорий."""

        path_get_categories = 'categories'
        url_get_category = self.base_url + path_get_categories      # cоздаем URL для запроса списка категорий

        result = requests.get(url_get_category)

        print(f'Статус код для списка категорий: {result.status_code}')
        assert result.status_code == 200, 'ОШИБКА, Статус-код не совпадает'
        print('Статус код корректен!')

        check_categories = result.json()
        assert check_categories, "Ответ содержит пустой список!"
        print('Список с категориями получен!')
        print(f'Список категорий: {check_categories}')

        self.list_categories = check_categories
        print(f'Количество категорий: {len(self.list_categories)}')


    def test_get_joke_by_categories(self, name_assert):
        """Тест по получению шуток для каждой категории, включает:
            отправку запроса на получение шутки в цикле для каждой категории и подсчёт шуток,
            печать категории и соответствующей шутки,
            проверка наличия определенного слова в шутке,
            проверка статус-кода ответа,
            печать проверочного слова,
            проверка и печать количества категорий и шуток."""

        number_of_jokes = 0     # считаем количество шуток

        for category in self.list_categories:
            path_get_joke_by_categories = f'random?category={category}'
            url_get_joke_by_category = self.base_url + path_get_joke_by_categories  # cоздаем URL для запроса шуток

            result = requests.get(url_get_joke_by_category)
            check_joke = result.json()
            joke_by_category = check_joke.get('value')
            print(f'Шутка в категории "{category}": {joke_by_category}')
            assert name_assert in joke_by_category, 'ОШИБКА, Проверочное слово отсутствует'
            number_of_jokes += 1

        print(f'Статус код для шутки: {result.status_code}')
        assert result.status_code == 200, 'ОШИБКА, Статус-код не совпадает'
        print('Статус код корректен!')

        print(f'Проверочное слово "{name_assert}" присутствует в шутках.')

        assert len(self.list_categories) == number_of_jokes, 'ОШИБКА, Количество категорий и шуток не совпадает'
        print(f'Количество категорий и шуток совпадает и равно {number_of_jokes}.')



new_joke_by_category = CreateJokeTestCategory()
new_joke_by_category.test_get_categories()
new_joke_by_category.test_get_joke_by_categories("Chuck")