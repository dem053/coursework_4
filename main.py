import re

from src.hh_class import HeadHunterAPI
from src.sj_class import SuperJobAPI
from src.json_saver_class import JSONSaver
from src.MixingDefServer import MixingDef


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
    print(json_saver.save_vacancies(vacancies))

    while True:
        print(
            'Что делаем дальше?\n 1 - вывести все вакансии на экран\n 2 - отсортировать вакансии по з/п\n 3 - вывести '
            'ТОП вакансий\n 4 - удалить вакансии без з/п\n 5 - удалить вакансию\n 6 - вывести вакансии из диапазона '
            'зарплат\n 7 - поиск вакансий по ключевым словам\n 8 - выход из программы')
        vacancies_tmp = []
        user_answ = input('Дай номер команды :')
        if user_answ == '' or re.sub('[^0-9]+', '', user_answ) == '':
            user_answ = 0
        else:
            user_answ = int(re.sub('[^0-9]+', '', user_answ))
        if user_answ == 1:
            MixingDef.print_vacancies(vacancies)
        elif user_answ == 2:
            vacancies_tmp, answ = MixingDef.sort_vacancies(vacancies)
            print(answ)
        elif user_answ == 3:
            top_n = int(input('Введите количество ТОП вакансий: '))
            vacancies_tmp = MixingDef.get_top_vacancies(vacancies, top_n)
            MixingDef.print_vacancies(vacancies_tmp)
        elif user_answ == 4:
            vacancies_tmp = [v for v in vacancies]
            vacancies_tmp = MixingDef.del_salary_zero(vacancies_tmp)
            print(f'Удалено {len(vacancies) - len(vacancies_tmp)} вакансий')
        elif user_answ == 5:
            user_answ = input("Введите ссылку на вакансию : ")
            vacancies_tmp, answ = MixingDef.del_vacancy_by_id(vacancies, user_answ)
            print(answ)
        elif user_answ == 6:
            user_answ = input('Введите диапазон зарплат (зарплата от - зарплата до руб.) : ')
            vacancies_tmp = MixingDef.get_vacancies_by_salary_str(vacancies, user_answ)
            MixingDef.print_vacancies(vacancies_tmp)
        elif user_answ == 7:
            user_answ = input('Напиши слова, которые ты хочешь найти в описании,\nно помни правило слово пробел слово ')
            if user_answ != '':
                filter_words = user_answ.split(" ")
            vacancies_tmp = MixingDef.filter_vacancies(vacancies, filter_words)
            if vacancies_tmp == []:
                print('Не нашел таких вакансий')
            else:
                print(f'Найдено {len(vacancies_tmp)} вакансий!')
        elif user_answ == 8:
            print("Пока")
            break
        else:
            print('Не знаю такой команды')
        if vacancies_tmp:
            user_answ = input("Сохранить изменения в файл? (да/нет) ")
            if user_answ.lower() == 'да':
                vacancies = [v for v in vacancies_tmp]
                print(json_saver.save_vacancies(vacancies))
        # break


if __name__ == '__main__':
    main()
