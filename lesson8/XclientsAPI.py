import requests


class Api:
    url = "https://x-clients-be.onrender.com"

    def __init__(self, url):
        self.url = url

    def get_token(self, login='raphael', password='cool-but-crude'):
        acc = {'username': login, 'password': password}
        resp = requests.post(self.url + '/auth/login', json=acc)
        self.user_token = resp.json()["userToken"]
        return self.user_token

    def create_new_company(self, name, descr):
        company = {"name": name,
                   "description": descr}
        headers = {}
        headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/company', json=company, headers=headers)
        return resp.json()["id"]

    def get_employee(self, company_id):
        params = {'company': company_id}
        response = requests.get(self.url + '/employee', params=params)
        return response.json()

    def add_employee(self, id, company_id, first_name, last_name, middle_name,
                     email, employee_url, phone, birthdate, is_active):
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
        if company_id is None:
            company_id = self.create_new_company()
        if not all([id, first_name, last_name, company_id, is_active]):
            raise ValueError("Заполнены не все обязательные поля")
        headers = {}
        headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',
                             json=employee, headers=headers)
        return resp.json()

    def get_employee_by_id(self, id_get):
        resp = requests.get(self.url+f"/employee/{id_get.get('id')}")
        return resp.json()

    def edit_employee(self, id, edit_lastName, edit_email,
                      edit_url, edit_phone, edit_status):
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
