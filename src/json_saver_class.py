import os.path
import json
import pprint

from src.abcClass import Saver


class JSONSaver(Saver):

    def __init__(self, file_name='vacancy'):
        self.file_name = os.path.join('data', file_name)
        if not os.path.exists('data'):
            os.makedirs('data')

    def save_vacancies(self, vacancies):
        """
        Созраняет переданный список в файл JSON
        :param vacancies: список для записи
        :return: файл file_name.json
        """
        # if not os.path.exists('data'):
        #     os.makedirs('data')
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=2, ensure_ascii=False)

    def load_vacancies(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            text = json.load(file)
            return text

    def add_vacancy(self, vacancy):
        """
        добавляет вакансию в файл
        :param vacancy: словарь с данными о вакансии
        :return: новый файл
        """
        with open(self.file_name, 'r', encoding='utf-8') as file:
            l = json.load(file)
        with open(self.file_name, 'w', encoding='utf-8') as file:
            l.append(vacancy)
            json.dump(l, file, indent=2, ensure_ascii=False)
        return

    def del_vacancy(self, vacancy):
        """
        удаляет вакансию из файла
        :param vacancy: словарь с данными о вакансии
        :return: новый файл
        """
        with open(self.file_name, 'r', encoding='utf-8') as file:
            l = json.load(file)
        if vacancy in l:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                l.remove(vacancy)
                json.dump(l, file, indent=2, ensure_ascii=False)
            return f'Вакансия {vacancy["name"]} удалена из файла {self.file_name}'
        else:
            return f'Вакансия {vacancy["name"]} не найдена в файле {self.file_name}'

