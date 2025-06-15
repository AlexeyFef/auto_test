import requests


class ListOfPersons:
    """Класс включающий сценарии по отправке запросов с целью создания списка уникальных персонажей, участвовавших в
        фильмах вместе с заданным персонажем, запись их в файл в алфавитном порядке"""

    base_url = 'https://swapi.dev/api/'  # cоздаём base_url

    def __init__(self, number_of_person):
        self.number_of_person = number_of_person
        self.list_links_of_films = []
        self.name_person = ''

    def create_list_links_of_films(self):
        """Метод для получения списка фильмов, в котором снимался заданный персонаж, включает:
            создание URL для запроса на получение информации о персонаже,
            печать ссылки,
            отправка запроса,
            Проверка статуса-кода ответа,
            запись ссылок на фильмы, в которых снимался персонаж, в список,
            получение и печать имени персонажа,
            печать списка ссылок на фильмы, в которых снимался персонаж"""


        path_for_person = f'people/{self.number_of_person}/'    # путь для поиска списка фильмов определенного персонажа
        get_url = self.base_url + path_for_person
        print(f'Ссылка для получения информации о персонаже № {self.number_of_person}: {get_url}')
        person_response = requests.get(get_url)
        check_person_response = person_response.json()
        assert 200 == person_response.status_code, 'ОШИБКА! Статус-код не совпадает.'  # проверка статуса-кода ответа
        print(f'Статус-код ответа {person_response.status_code} корректен.')

        self.list_links_of_films = check_person_response.get('films')   # получение списка ссылок на фильмы с участием персонажа
        self.name_person = check_person_response.get('name')        # получение имени персонажа

        print(f'JSON ответа {check_person_response}')
        print(f'Имя персонажа: {self.name_person}')
        print(f'Список ссылок на фильмы с участием "{self.name_person}": {self.list_links_of_films}')

        print('\n' + 'Работа метода create_list_links_of_films завершена успешно!' + '\n')


    def create_list_of_persons(self):
        """Метод для получения файла со списком уникальных персонажей, снимавшихся с заданным персонажем:
            создание множества имён,
            в цикле прохождение по списку ссылок на фильмы с нашим персонажем,
            проверка статус-кода ответа,
            получение названия фильма,
            создание и получение списка cсылок на персонажей, участвовавших в фильме,
            в цикле прохождение по списку ссылок на имена персонажей,
            проверка статуса-кода ответа при запросе имени,
            проверка наличия поля name в ответе,
            формирование множества уникальных персонажей,
            формирование файла с именами персонажей,
            вывод информации о количестве персонажей в фильмах"""

        all_names = set()               # создание множества имён персонажей, используем set() для исключения дубликатов

        for link_film in self.list_links_of_films:     # в цикле прохождение по списку ссылок на фильмы с нашим персонажем

            film_response = requests.get(link_film)
            if film_response.status_code != 200:                # проверка статуса-кода ответа при запросе инфо о фильме
                print(f'ОШИБКА! При запросе инфо о фильме по ссылке "{link_film}" статус-код {film_response.status_code} некорректен.')
                continue

            check_film_response = film_response.json()
            title_film = check_film_response.get('title')       #  получение названия фильма
            list_links_of_names = check_film_response.get('characters', [])  # создание и получение списка cсылок на персонажей

            for link_name in list_links_of_names:           # в цикле прохождение по списку ссылок на имена персонажей
                name_response = requests.get(link_name)
                if name_response.status_code != 200:            # проверка статуса-кода ответа при запросе имени
                    print(f'ОШИБКА! При запросе имени персонажа по ссылке "{link_name}" статус-код'
                          f'{name_response.status_code} некорректен.')
                    continue

                check_name_response = name_response.json()
                assert 'name' in check_name_response, f'ОШИБКА: В ответе {check_name_response} нет поля "name".' # проверка
                                                                                    # наличия поля name в ответе
                name = check_name_response.get('name')   # получаем имя персонажа

                if name != self.name_person:            # исключаем самого персонажа из списка
                    all_names.add(name)                 # добавляем имя персонажа во множество

            print(f'В фильме "{title_film}" снималось {len(list_links_of_names)} персонажей.')

        with open('doc/list_names.txt', 'w', encoding='utf-8') as file:  # записываем уникальных персонажей в файл
                                                                            # в алфавитном порядке
            file.write("\n".join(sorted(all_names)))

        print(f'Все уникальные персонажи, в количестве {len(all_names)} персон, снимавшиеся с {self.name_person} в '
              f'{len(self.list_links_of_films)} фильмах, успешно записаны в файл doc/list_names.')

        print('\n' + 'Работа метода create_list_of_persons завершена успешно!')




persons_list = ListOfPersons(4)
persons_list.create_list_links_of_films()
persons_list.create_list_of_persons()