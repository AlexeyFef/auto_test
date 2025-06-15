import requests



class DeleteCheckLocationTest:
    """Класс, включающий сценарии по отправке запросов с целью чтения из файла, удаления определенных локаций,
        проверки наличия локаций, записи в новый файл"""

    base_url = "https://rahulshettyacademy.com"     # cоздаём base_url
    key = '?key=qaclick123'                         # ключ для допуска


    def delete_location_test(self):
        """Тест по удалению определенных локаций из файла, включает:
            создание URL для DELETE запроса,
            печать ссылки для удаления локаций,
            чтение place_id из файла,
            печать JSON для удаления локации,
            печать номера и place_id удаляемой локации,
            отправку запроса на удаление 2 и 4 локации в цикле,
            проверка и печать статуса ответа,
            проверка наличия удаленной локации с помощью метода GET,
            проверка и печать сообщения об отсутствующей локации"""

        delete_resource = '/maps/api/place/delete/json'             # путь метода DELETE для удаления локаций
        delete_url = self.base_url + delete_resource + self.key    # создание URL для DELETE запроса
        get_resource = '/maps/api/place/get/json'                  # путь метода GET для получения информации о локации

        print(f'Ссылка для удаления локаций: {delete_url}')

        with open('doc/locations.txt', 'r') as data:
            list_place_id = data.readlines()

        for i, place_id in enumerate(list_place_id):
            if i in (1, 3):                                 # Удаляем 2-ю и 4-ю локации (если считать с 0, то это №№ 1, 3)
                place_id = place_id.strip()
                delete_location_body = {"place_id": place_id} # создание JSON для DELETE запроса для определенной локации
                print(f'JSON для удаления локации № {i+1}: {delete_location_body}')
                print(f'Удаление локации № {i+1}, имеющей place id: {place_id}')
                result_delete = requests.delete(delete_url, json=delete_location_body)  # отправляем запрос на удаление локации
                check_result_delete = result_delete.json()

                status = check_result_delete.get('status')      # проверка статуса ответа
                print(f'Статус ответа: {status}')
                assert status == 'OK', 'ОШИБКА! Поле Status некорректно'
                print('Поле Status корректно.')

                get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id  # создание URL для
                                                                                             # проверочного GET запроса
                result_get = requests.get(get_url)
                check_result_get = result_get.json()
                message = check_result_get.get('msg')

                assert message == "Get operation failed, looks like place_id  doesn't exists", 'ОШИБКА! Сообщение не совпадает.'  # проверка сообщения в ответе
                print(f'Сообщение: "{message}" корректно. Локация успешна удалена.', '\n')


        print('Работа метода delete_location закончена!', '\n')


    def check_location_and_create_new_file_test(self):
        """Тест по проверке существующих локаций в файле и записи их в новый файл, включает:
                    очиcтку нового файла перед началом записи,
                    чтение значений place_id из файла,
                    создание цикла для чтения информации о локациях,
                    создание URL для GET запроса,
                    отправку запроса на получение информации о локации,
                    выбор существующих локаций,
                    печать статуса-кода ответа и place_id существующей локации,
                    запись в новый файл"""

        get_resource = '/maps/api/place/get/json'  # путь метода GET

        with open('doc/locations_new.txt', 'w') as file:  # очищаем файл doc/locations_new.txt пред началом работы
            file.write('')

        with open('doc/locations.txt', 'r') as data:
            list_place_id = data.readlines()

        for place_id in list_place_id:
            place_id = place_id.strip()
            get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id  # создание URL запроса
            result_get = requests.get(get_url)

            if result_get.status_code == 200:                 # проверяем статус ответа
                with open('doc/locations_new.txt', 'a') as file:  # записываем place_id в файл doc/locations_new.txt
                    file.write(place_id + '\n')
                print(f'Статус-код: {result_get.status_code}. Локация с place_id: "{place_id}" существует и добавлена '
                      f'в новый файл.')


        print('Работа метода check_location_and_create_new_file закончена!', '\n')



new_file_location_test = DeleteCheckLocationTest()
new_file_location_test.delete_location_test()
new_file_location_test.check_location_and_create_new_file_test()