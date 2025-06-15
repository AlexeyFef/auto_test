import requests



class CreateCheckLocationTest:
    """Класс включающий сценарии по отправке запросов с целью создания локаций, запись их в файл, чтение из файла,
        проверки наличия"""

    base_url = "https://rahulshettyacademy.com"     # cоздаём base_url
    key = '?key=qaclick123'                         # ключ для допуска


    def create_location(self):
        """Тест по созданию локаций и записи их в файл, включает:
            создание URL для POST запроса,
            очищаем файл перед началом записи
            отправку запроса на создание в цикле 5 локаций,
            печать JSON ответа,
            проверка и печать статуса ответа,
            проверка наличия и печать значения place_id,
            запись значений place_id в файл,
            чтение и печать значений place_id из файла"""

        post_resource = '/maps/api/place/add/json'             # путь метода POST для создания локаций
        post_url = self.base_url + post_resource + self.key    # создание URL для POST запроса
        print(f'Ссылка для создания локаций: {post_url}')

        with open('doc/locations.txt', 'w') as file:    # очищаем файл doc/locations.txt пред началом работы
            file.write('')

        for _ in range(5):              # цикл для создания пяти локаций

            json_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }

            result_post = requests.post(post_url, json=json_new_location)   # отправка POST запроса для создания локации
            check_result_post = result_post.json()
            print(result_post.json())

            status = check_result_post.get('status')                    # проверка статуса ответа
            assert status == 'OK', 'ОШИБКА! Поле Status некорректно'
            print('Поле Status корректно.')

            assert 'place_id' in check_result_post, 'ОШИБКА! Локация не создана.'   # проверка наличия place_id
            place_id = check_result_post.get('place_id')
            print('Локация создана и имеет place_id: ' + place_id)

            with open('doc/locations.txt', 'a') as file:    # записываем place_id в файл doc/locations.txt
                file.write(place_id + '\n')

        print('Выводим ниже список созданных place_id:')       # чтение и печать place_id из файла doc/locations.txt
        with open('doc/locations.txt', 'r') as data:
            print(data.read())

        print('Работа метода create_location закончена!', '\n')

    def check_location(self):
        """Тест по проверке созданной локаций из файла, включает:
                    чтение значений place_id из файла,
                    создание цикла для чтения информации о локациях,
                    создание URL для GET запроса,
                    отправку запроса на получение локаций,
                    печать JSON ответа,
                    проверка и печать статуса-кода ответа,
                    проверка наличия и печать значения place_id"""

        get_resource = '/maps/api/place/get/json'  # путь метода GET


        with open('doc/locations.txt', 'r') as data:
            list_place_id = data.readlines()

        for place_id in list_place_id:
            get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id.strip()   # создание URL запроса
            print(f'Ссылка для получения информации о локации: {get_url}')
            result_get = requests.get(get_url)
            check_result_get = result_get.json()
            print(check_result_get)

            print(f'Статус код: {result_get.status_code}')
            assert result_get.status_code == 200, 'ОШИБКА! Статус-код не совпадает.'    # проверка статуса-кода ответа
            print('Статус-код корректен.')

            assert 'location' in check_result_get, 'ОШИБКА! Такой локации не существует.'  # проверка наличия place_id
            print(f'Локация с place_id: {place_id.strip()} существует.')

        print('Работа метода сheck_location закончена!', '\n')


five_location_test = CreateCheckLocationTest()
five_location_test.create_location()
# five_location_test.check_location()
