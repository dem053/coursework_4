class Vacancy:
    """
    Класс вакансий
    : param name -- название вакансии
    : param source -- источник
    : param v_url -- ссылка
    : param employer -- работодатель
    : param requirement -- описание
    : param salary_from -- з/п от
    : param salary_to -- з/п до
    : param car -- валюта з/п
    """

    def __init__(self, name: str, source: str, v_url: str, employer: str, requirement: str, salary_from=None,
                 salary_to=None, currency_=None):
        self.name = name
        self.source = source
        self.v_url = v_url
        self.employer = employer
        self.requirement = requirement
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.cur = currency_

    @property
    def salary_from(self):
        return self._salary_from

    @salary_from.setter
    def salary_from(self, value):
        if value:
            self._salary_from = int(float(value))
        else:
            self._salary_from = 0

    @property
    def salary_to(self):
        return self._salary_to

    @salary_to.setter
    def salary_to(self, value):
        if value:
            self._salary_to = int(float(value))
        else:
            self._salary_to = 0

    @property
    def cur(self):
        return self.__cur

    @cur.setter
    def cur(self, currency_):
        if currency_ is None:
            self.__cur = "валюта не указана"
        elif currency_.lower() == 'rub':
            self.__cur = 'RUR'
        else:
            self.__cur = currency_

    def __str__(self):
        return (
            f'Вакансия: {self.name}\n'
            f'{self.v_url}\n'
            f'Работодатель: {self.employer}\n'
            f'Зарплата: {self.get_salary()}\n'
            f'Описание: {self.requirement}\n'
        )

    def get_salary(self):
        if self.cur == 'RUR':
            txt_currency = 'руб.'
        elif self.cur is None:
            txt_currency = ''
        else:
            txt_currency = self.cur
        if self.salary_from != 0 and self.salary_to != 0:
            return f'{self.salary_from}{txt_currency} - {self.salary_to}{txt_currency}'
        elif self.salary_from != 0 and self.salary_to == 0:
            return f'от {self.salary_from}{txt_currency}'
        elif self.salary_from == 0 and self.salary_to != 0:
            return f'до {self.salary_to}{txt_currency}'
        else:
            return 'зарплата не указана'

    def vacancy_dict(self):
        return {'name': self.name, 'source': self.source, 'v_url': self.v_url, 'employer': self.employer,
                'requirement': self.requirement, 'salary_from': self._salary_from, 'salary_to': self._salary_to,
                'currency': self.cur}

    def max_salary(self):
        """
        метод возвращающий максимальное значение между salary_from и salary_to
        используется для сравнения вакансий
        :return: max (salary_from и salary_to)
        """
        return max(self.salary_to, self.salary_from)

    def __lt__(self, other):
        if self.cur != other.cur:
            raise TypeError ('пока не умею сравнивать разные валюты')
        else:
            return self.max_salary() < other.max_salary()

    def __le__(self, other):
        if self.cur != other.cur:
            raise TypeError ('пока не умею сравнивать разные валюты')
        else:
            return self.max_salary() <= other.max_salary()

    def __gt__(self, other):
        if self.cur != other.cur:
            raise TypeError ('пока не умею сравнивать разные валюты')
        else:
            return self.max_salary() > other.max_salary()

    def __ge__(self, other):
        if self.cur != other.cur:
            raise TypeError ('пока не умею сравнивать разные валюты')
        else:
            return self.max_salary() >= other.max_salary()

    @classmethod
    def get_vac_from_dict(cls, user_dict):
        """
        конструктор экземпляра по словарю
        :param user_dict: словарь
        :return: экземпляр класса
        """
        return cls(user_dict['name'], user_dict['source'], user_dict['v_url'], user_dict['employer'], user_dict['requirement'], user_dict['salary_from'], user_dict['salary_to'], user_dict['currency'])
