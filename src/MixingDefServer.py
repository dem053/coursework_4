import pprint


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

    @staticmethod
    def mix_filter_vacancies(vacancies: list, filter_words: list):
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
                if str(word).lower() in v['requirement'].lower():
                    result.append(v)
                    break
        return result

    @staticmethod
    def sort_vacancies(vacancies: list):
        for i in range(len(vacancies)):
            vacancies[i]['max_salary'] = max(vacancies[i]['salary_from'], vacancies[i]['salary_to'])
        return sorted(vacancies, key=lambda x: x['max_salary'], reverse=True)

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        if top_n >= len(vacancies):
            return MixingDefServer.sort_vacancies(vacancies)
        return MixingDefServer.sort_vacancies(vacancies)[0:top_n]

        




