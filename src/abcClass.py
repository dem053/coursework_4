from abc import ABC, abstractmethod


class GetVacancy(ABC):
    """
    ААбстрактный класс для работы с API сайтов с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, vacancy_title: str) -> list:
        """
        Получает список вакансий с сайта
        """
        pass

    # @staticmethod
    # @abstractmethod
    # def organize_vacancy_info(vacancy_data: list) -> list:
    #     """Организует данные о вакансиях в определённом виде"""
    #     pass
 # @property
 #    def currency(self):
 #        return self.__currency
 #
 #    @currency.setter
 #    def currency(self, currency_):
 #        if currency_.lower() == 'rub':
 #            self.__currency = 'RUR'
 #        else:
 #            self.__currency = currency_