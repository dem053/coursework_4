from abc import ABC

from src.abcClass import GetVacancy
from src.vacancies_class import Vacancy
import requests
import os


class SuperJobAPI(GetVacancy, ABC):
    sj_url = "https://api.superjob.ru/2.0/vacancies"
    API_KEY = os.getenv('SJ_API_KEY')
    headers = {'X-Api-App-Id': API_KEY}

    def __init__(self, page=0, count=100):
        """
        конструктор
        :param page -- количество страниц
        :param count -- количество вакансий
        """
        self.page = page
        self.count = count

    def __str__(self):
        return "api.superjob.ru"

    def get_vacancies(self, key_word: str) -> list:
        """
        выполняет поиск вакансий по ключевым словам key_word
        достает из полученных вакансий необходимые поля по "штампу" класса Vacancy
        возвращает список словарей
        """
        params = {
            'keyword': key_word,
            'page': self.page,
            'count': self.count}
        response = requests.get(self.sj_url, headers=self.headers, params=params)
        vacancies = response.json()['objects']
        result = []
        for v in vacancies:
            name = v['profession']
            source = 'SuperJob'
            v_url = v['link']
            employer = v['firm_name']
            requirement = v['candidat'].strip().replace('\n', '')
            salary_from = v['payment_from']
            salary_to = v['payment_to']
            currency = v['currency']
            vacancy = Vacancy(name, source, v_url, employer, requirement, salary_from, salary_to, currency)
            result.append(vacancy.vacancy_dict())
        return result
