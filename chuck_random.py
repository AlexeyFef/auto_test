import requests


class CreateJokeTest:
    """Класс включающий сценарии по отправке запросов, с целью получения шуток с Чаком Норрисом"""

    base_url = "https://api.chucknorris.io/jokes/random"

    def test_create_random_joke(self):
        """Тест по получению рандомной шутки, включает: отправку запроса, проверка на статус-код, печать шутки."""

        result = requests.get(self.base_url)
        print(f'Статус код = {result.status_code}')
        assert result.status_code == 200, 'ОШИБКА, Статус-код не совпадает'
        print('Статус код корректен!')

        check_joke = result.json()
        joke_value = check_joke.get('value')
        print(f'Шутка: {joke_value}')

    def test_create_random_joke_category_positive(self):
        """Тест по получению рандомной шутки по определенной категории, включает:
            отправку запроса, проверка на статус-код, проверка на соответствие категории,
            проверку на содержание имени Chuck в теле шутки, печать шутки."""

        category = 'food'
        path_random_joke = f'?category={category}'
        url_random_joke_category = self.base_url + path_random_joke
        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус код = {result.status_code}')

        assert 200 == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print('Статус код корректен!')

        check_joke = result.json()
        joke_value = check_joke.get('value')
        print(f'Шутка: {joke_value}')

        joke_category = check_joke.get('categories')
        print(f'Категория: {joke_category[0]}')
        assert joke_category[0] == category, 'ОШИБКА, Категория не совпадает'
        print('Категория корректна')

        name_assert = 'Chuck'
        assert name_assert in joke_value, 'ОШИБКА, Проверочное слово отсутствует'
        print(f'Проверочное слово "{name_assert}" присутствует')
        print("Тест прошел успешно")


    def test_create_random_joke_category_negative(self, category, expected_status_code):
        """Тест по получению рандомной шутки по несуществующей категории, включает:
            отправку запроса, проверка на статус-код, проверка на соответствие категории"""

        path_random_joke = f'?category={category}'
        url_random_joke_category = self.base_url + path_random_joke
        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус код = {result.status_code}')

        assert expected_status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print('Статус код корректен!')

        check_joke = result.json()
        error = check_joke.get('error')
        assert error == 'Not Found', 'ОШИБКА, Поле Error некорректно'
        print('Поле Error корректно')




new_joke = CreateJokeTest()
#new_joke.test_create_random_joke()
#new_joke.test_create_random_joke_category_positive()
new_joke.test_create_random_joke_category_negative('spor', 404)
new_joke.test_create_random_joke_category_negative('abc', 404)
new_joke.test_create_random_joke_category_negative('', 404)


# url = "https://dog.ceo/api/breed/hound/images"
# response = requests.get(url)
# fields = response.json()
# messages = fields.get('message', [])
# count_hound_english = sum(1 for img in messages if 'hound-english' in img)
# number_message = len(messages)
# print(count_hound_english)
# print(number_message)

