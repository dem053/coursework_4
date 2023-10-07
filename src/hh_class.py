from abc import ABC

from src.abcClass import GetVacancy
from src.vacancies_class import Vacancy
import requests


class HeadHunterAPI(GetVacancy, ABC):
    hh_url = "https://api.hh.ru/vacancies"

    def __init__(self, area=113, page=0, per_page=100):
        """ конструктор
        :param area -- область поиска
        :param page -- количество страниц
        :param per_page -- количество вакансий"""

        self.area = area
        self.page = page
        self.per_page = per_page

    def __str__(self):
        return "api.hh.ru"

    def get_vacancies(self, key_word: str) -> list:
        """
        выполняет поиск вакансий по ключевым словам key_word
        достает из полученных вакансий необходимые поля по "штампу" класса Vacancy
        возвращает список словарей
        """
        params = {
            'text': key_word,
            'area': self.area,
            'page': self.page,
            'per_page': self.per_page
        }
        response = requests.get(self.hh_url, params=params)
        vacancies = response.json()['items']
        result = []
        for v in vacancies:
            name = v['name']
            source = 'HeadHunter'
            v_url = v['alternate_url']
            employer = v['employer']['name']
            requirement = v['snippet']['requirement']
            if requirement:
                requirement = v['snippet']['requirement'].replace('<highlighttext>', '').replace('</highlighttext>', '')
            if v['salary'] is not None:
                salary_from = v['salary']['from']
                salary_to = v['salary']['to']
                currency = v['salary']['currency']
            else:
                salary_from = 0
                salary_to = 0
                currency = None
            vacancy = Vacancy(name, source, v_url, employer, requirement, salary_from, salary_to, currency)
            result.append(vacancy.vacancy_dict())
        return result
