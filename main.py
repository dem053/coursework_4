import pprint
import re
import json

from src.vacancies_class import Vacancy
from src.hh_class import HeadHunterAPI
from src.sj_class import SuperJobAPI
from src.json_saver_class import JSONSaver


def main():
    vacancies = []
    platforms = ["HeadHunter", "SuperJob"]
    print(f'Могу помочь с поиском вакансий на сайтах:')
    for i in range(len(platforms)):
        print(f'{i + 1} - {platforms[i]}')
    num_platform = input('Введи номера сайтов где будем искать вакансии\nчерез пробел: ').split(" ")
    key_word = input('Введите поисковый запрос: ')
    for num in num_platform:
        if num == '1':
            hh = HeadHunterAPI(113, 0, 5)
            hh_vacancies = hh.get_vacancies(key_word)
            vacancies = vacancies + hh_vacancies
        if num == '2':
            sj = SuperJobAPI(0, 5)
            sj_vacancies = sj.get_vacancies(key_word)
            vacancies = vacancies + sj_vacancies
            json_saver = JSONSaver()
    print(f'Найдено и сохранено в файл "{json_saver.file_name}" {len(vacancies)} вакансий')
    print('Что делаем дальше?\n 1 - вывести все вакансии на экран\n 2 - отсортировать вакансии по з/п\n 3 - вывести ТОП вакансий\n 4 - удалить вакансии без з/п\n 6 - определенную вакансию\n end - выход из программы')
    # for v in vacancies:
    #     print(v)
    #     print('-----------------------------------------------------------\n')

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()


if __name__ == '__main__':
    main()
