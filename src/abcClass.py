from abc import ABC, abstractmethod


class GetVacancy(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, vacancy_title: str) -> list:
        """
        Получает список вакансий с сайта
        """
        pass


class Saver(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях.
    """

    @abstractmethod
    def save_vacancies(self, vacancies):
        """
        записывает вакансии в файл
        :param vacancies: список вакансий
        :return:
        """
        pass

    @abstractmethod
    def load_vacancies(self):
        """
        читает вакансии из файла
        :param file_name: имя файла
        :return: список с вакансиями
        """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        добавляет вакансию в файл
        :param vacancy: словарь с данными о вакансии
        :return: новый файл
        """
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        """
        удаляет вакансию из файла
        :param vacancy: словарь с данными о вакансии
        :return: новый файл
        """
        pass
