import requests


class CreateJokeCategoryTest:
    """Класс включающий сценарии по отправке запросов, с целью получения шуток с Чаком Норрисом по полученной от юзера
        категории"""

    base_url = "https://api.chucknorris.io/jokes/"  # cоздаём base_url
    list_categories = []  # создание пустого списка категорий
    user_category = input(
        'Введите категорию шутки на английском языке и нажмите ВВОД: ').lower()  # запрашиваем категорию шутки

    def test_get_categories(self):
        """Тест по проверке наличия введенной категории шуток, включает:
            создание URL для запроса на получение списка категорий,
            печать URL запроса,
            отправку запроса,
            проверка на наличие введенной категории в списке категорий,
            проверка и печать статус-кода ответа для запроса на получение списка категорий."""

        path_get_categories = 'categories'
        url_get_category = self.base_url + path_get_categories  # cоздаём URL для запроса списка категорий

        result = requests.get(url_get_category)
        check_categories = result.json()
        self.list_categories = check_categories

        while self.user_category not in self.list_categories:
            print("ОШИБКА! Вы ввели несуществующую категорию!")
            self.user_category = input('Введите категорию заново: ').lower()

        print('Вы ввели существующую категорию.')

        assert result.status_code == 200, 'ОШИБКА: Статус-код не совпадает'
        print(f'Статус-код списка категорий корректный: {result.status_code}')

    def test_get_joke_by_user_category(self):
        """Тест по получению шутки для введенной юзером категории, включает:
            создание и печать URL для запроса на получение шутки из заданной категории,
            отправку запроса на получение шутки,
            печать JSON из ответа,
            печать категории и соответствующей шутки,
            проверка категории шутки, введенной юзером и категории шутки, полученной от сервера,
            проверка статус-кода ответа."""

        path_get_joke_by_categories = f'random?category={self.user_category}'
        url_get_joke_by_category = self.base_url + path_get_joke_by_categories  # cоздаем URL для запроса шутки заданной категории
        print(f'URL для получения шутки: {url_get_joke_by_category}')

        result = requests.get(url_get_joke_by_category)
        check_joke = result.json()
        print(check_joke)

        joke_by_category = check_joke.get('value')
        print(f'Шутка из категории "{self.user_category}": {joke_by_category}')

        check_joke_category = check_joke.get('categories')
        assert check_joke_category[0] == self.user_category, (
            'ОШИБКА: Категория шутки, введенная юзером, не совпадает с '
            'категорией шутки, полученной от сервера!')
        print(f'Категория шутки, введенная юзером "{self.user_category}", совпадает с категорией шутки, '
              f'полученной от сервера "{check_joke_category[0]}".')

        print(f'Статус-код для полученной шутки: {result.status_code}')
        assert result.status_code == 200, 'ОШИБКА: Статус-код не совпадает!'
        print('Статус-код корректен!')


new_joke_by_category = CreateJokeCategoryTest()
new_joke_by_category.test_get_categories()
new_joke_by_category.test_get_joke_by_user_category()
