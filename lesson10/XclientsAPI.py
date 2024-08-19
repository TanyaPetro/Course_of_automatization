import requests
import allure


class Api:
    url = "https://x-clients-be.onrender.com"

    def __init__(self, url: str):
        self.url = url

    @allure.step("API. Получить токен")
    def get_token(self, login='raphael', password='cool-but-crude'):
        acc = {'username': login, 'password': password}
        resp = requests.post(self.url + '/auth/login', json=acc)
        self.user_token = resp.json()["userToken"]
        return self.user_token

    @allure.step("API. Создать новую компанию")
    def create_new_company(self, name: str, descr: str) -> str:
        company = {"name": name,
                   "description": descr}
        headers = {}
        headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/company', json=company, headers=headers)
        return resp.json()["id"]

    @allure.step("API. Получить список сотрудников компании с указанным id")
    def get_employee(self, company_id: str) -> dict:
        params = {'company': company_id}
        response = requests.get(self.url + '/employee', params=params)
        return response.json()

    @allure.step("API. Добавить сотрудника")
    def add_employee(self, id: str, company_id: str, first_name: str,
                     last_name: str, middle_name: str, email: str,
                     employee_url: str, phone: str, birthdate: object,
                     is_active: bool) -> dict:
        employee = {
                    "id": id,
                    "firstName": first_name,
                    "lastName": last_name,
                    "middleName": middle_name,
                    "companyId": company_id,
                    "email": email,
                    "url": employee_url,
                    "phone": phone,
                    "birthdate": birthdate,
                    "isActive": is_active
                    }
        if not all([id, first_name, last_name, company_id, is_active]):
            raise ValueError("Заполнены не все обязательные поля")
        headers = {}
        headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',
                             json=employee, headers=headers)
        return resp.json()

    @allure.step("API. Получить сотрудника по id")
    def get_employee_by_id(self, id_get: str) -> dict:
        resp = requests.get(self.url+f"/employee/{id_get.get('id')}")
        return resp.json()

    @allure.step("API. Изменить данные сотрудника сотрудника")
    def edit_employee(self, id: str, edit_lastName: str, edit_email: str,
                      edit_url: str, edit_phone: str, edit_status: bool) -> dict:
        edit_employee = {
                         "lastName": edit_lastName,
                         "email": edit_email,
                         "url": edit_url,
                         "phone": edit_phone,
                         "isActive": edit_status
                        }
        headers = {}
        headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url+f"/employee/{id.get('id')}",
                              json=edit_employee, headers=headers)
        return resp.json()
