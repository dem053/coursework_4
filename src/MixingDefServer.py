class MixingDefServer:
    """
    функции для классов работы с файлами
    """

    @staticmethod
    def del_salary_zero(vacancies):
        """ получает список вакансий и удаляет вакансии без указания з/п"""

        for v in vacancies:
            if v['salary_to'] == 0 and v['salary_from'] == 0:
                vacancies.remove(v)
        return vacancies

    @staticmethod
    def mix_get_vacancies_by_salary(vacancies, salary_from, salary_to, currency):
        """ выборка вакансий по зп от salary_to до salary_from"""

        result = []
        for v in vacancies:
            if v['currency'].lower() == currency.lower():
                if salary_from <= max(v['salary_to'], v['salary_from']) <= salary_to:
                    result.append(v)
        return result
