import os.path
import json
import pprint
import re

from src.abcClass import Saver
from src.MixingDefServer import MixingDefServer


class JSONSaver(Saver, MixingDefServer):

    def __init__(self, file_name='vacancy'):
        self.file_name = os.path.join('data', file_name + '.json')
        if not os.path.exists('data'):
            os.makedirs('data')

    def save_vacancies(self, vacancies):
        """
        Созраняет переданный список в файл JSON
        :param vacancies: список для записи
        :return: файл file_name.json
        """
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=2, ensure_ascii=False)

    def load_vacancies(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            return vacancies

    def add_vacancy(self, vacancy):
        """
        добавляет вакансию в файл
        :param vacancy: словарь с данными о вакансии
        :return: новый файл
        """
        l = self.load_vacancies()
        l.append(vacancy)
        self.save_vacancies(l)
        return f'Вакансия {vacancy["name"]} добавлена в файле {self.file_name}'

    def del_vacancy(self, vacancy):
        """
        удаляет вакансию из файла
        :param vacancy: словарь с данными о вакансии
        :return: новый файл
        """
        l = self.load_vacancies()
        if vacancy in l:
            l.remove(vacancy)
            self.save_vacancies(l)
            return f'Вакансия {vacancy["name"]} удалена из файла {self.file_name}'
        else:
            return f'Вакансия {vacancy["name"]} не найдена в файле {self.file_name}'

    def delete_zero_salary(self):
        """ удаляет вакансии без зарплаты из файла"""
        l = self.load_vacancies()
        result = self.del_salary_zero(l)
        self.save_vacancies(result)
        return result

    def get_vacancies_by_salary(self, user_text):
        text = user_text.split('-')
        part1 = str(text[0])
        part2 = str(text[1])
        salary_from = int(re.sub('[^0-9]+', '', part1))
        print(salary_from)
        salary_to = int(re.sub('[^0-9]+', '', part2))
        print(salary_to)
        currency = re.sub('[^a-zA-Zа-яА-ЯёЁ]+', "", part2)
        print(currency)
        if currency.lower() == 'руб' or currency.lower() == 'рублей' or currency.lower() == 'he':
            currency = 'RUR'
        l = self.load_vacancies()
        result = self.mix_get_vacancies_by_salary(l, salary_from, salary_to, currency)
        # self.save_vacancies(result)
        return result





