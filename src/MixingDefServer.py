import re

from src.vacancies_class import Vacancy


class MixingDef:
    """
    функции для классов работы со списком вакансий
    param: vacancies - list - список вакансий
    result - list - список вакансий
    """

    @staticmethod
    def del_salary_zero(vacancies_temp):
        """ получает список вакансий и удаляет вакансии без указания з/п"""
        for v in vacancies_temp:
            if v['salary_to'] == 0 and v['salary_from'] == 0:
                vacancies_temp.remove(v)
        return vacancies_temp

    @staticmethod
    def get_vacancies_by_salary(vacancies, salary_from, salary_to, currency):
        """ выборка вакансий по з/п от salary_to до salary_from"""

        result = []
        for v in vacancies:
            if v['currency'].lower() == currency.lower():
                if salary_from <= max(v['salary_to'], v['salary_from']) <= salary_to:
                    result.append(v)
        return result

    @staticmethod
    def filter_vacancies(vacancies: list, filter_words: list):
        """
        выборка вакансий по ключевым словам
        :param vacancies: список вакансий
        :param filter_words: ключевые слова
        :return: список вакансий в описании которых есть хоть одно ключевое слово
        """
        result = []
        if not filter_words:
            return result
        for v in vacancies:
            for word in filter_words:
                if v['requirement']:
                    if str(word).lower() in v['requirement'].lower():
                        result.append(v)
                        break
        return result

    @staticmethod
    def sort_vacancies(vacancies: list):
        """
        каждому экзепляру присваевается атрибут max_salary
        result отсортированный (от большей к меньшей) список по атрибуту max_salary
        """
        for i in range(len(vacancies)):
            vacancies[i]['max_salary'] = max(vacancies[i]['salary_from'], vacancies[i]['salary_to'])
        return sorted(vacancies, key=lambda x: x['max_salary'], reverse=True), f'Вакансии отсортированы'

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        """ возвращает список top_n крупнейших по з/п вакансий"""
        sort_vacancies, ans = MixingDef.sort_vacancies(vacancies)
        if top_n >= len(sort_vacancies):
            return sort_vacancies
        return sort_vacancies[0:top_n]

    @staticmethod
    def get_vacancies_by_salary_str(vacancies, user_text: str):
        """
        выборка вакансий в диапазоне зарплат заданной в строке 'xxxx - xxxxx руб.'
        :param vacancies: список вакансий
        :param user_text: диапазан зарплат и валюта
        :return:
        """
        text = user_text.split('-')
        part1 = str(text[0])
        part2 = str(text[1])
        salary_from = int(re.sub('[^0-9]+', '', part1))
        salary_to = int(re.sub('[^0-9]+', '', part2))
        currency = re.sub('[^a-zA-Zа-яА-ЯёЁ]+', "", part2)
        if currency.lower() == 'руб' or currency.lower() == 'рублей' or currency.lower() == 'he':
            currency = 'RUR'
        result = MixingDef.get_vacancies_by_salary(vacancies, salary_from, salary_to, currency)
        return result

    @staticmethod
    def print_vacancies(vacancies):
        print('---------------------------------------------------------------------------')
        for v in vacancies:
            vacancy = Vacancy.get_vac_from_dict(v)
            print(vacancy)
            print('---------------------------------------------------------------------------')

    @staticmethod
    def del_vacancy_by_id(vacancies_tmp, v_url):
        for v in vacancies_tmp:
            if v['v_url'] == v_url:
                vacancies_tmp.remove(v)
        return vacancies_tmp, f'Удалена вакансия {v_url}'
