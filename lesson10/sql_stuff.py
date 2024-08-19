from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


class sqlStuff:
    __scripts = {
        "get company list": text("select * from company"),
        "get employee list": text("select * from employee"),
        "get company by id": text(
            "select * from company where id = :company_id"
            ),
        "get employee by id": text(
            "select * from employee where id = :employee_id"
            ),
        "max id employee": text("select max(id) from employee"),
        "get employee list by company id": text(
            "select * from employee where company_id = :company_id"
            ),
        "insert company": text(
            "insert into company (\"name\",\
            \"description\") values (:new_name, :new_descr)"
            ),
        "max id company": text("select max(id) from company"),
        "delete company": text("delete from company where id = :id_delete"),
        "delete employee": text("delete from employee where id = :id_delete"),
        "create employee": text(
            "INSERT INTO employee\
                (\"is_active\", \"create_timestamp\",\
                \"change_timestamp\",\"first_name\",\"last_name\",\
                    \"middle_name\",\"phone\",\"email\",\"avatar_url\",\
                        \"company_id\")\
                        values (:is_active,:create_timestamp, \
                            :change_timestamp,:first_name, \
                                :last_name, :middle_name, :phone, :email,\
                                :avatar_url, :company_id)"
            ),
        "edit employee": text(
            "UPDATE employee SET \"is_active\"\
                = :is_active, \"last_name\" = :last_name,\
                    \"phone\" = :phone, \"email\" = :email,\
                        \"avatar_url\" = :avatar_url WHERE \
                            company_id = :company_id"
            )
    }

    def __init__(self, connection_string: str):
        self.db = create_engine(connection_string)

    @allure.step("SQL. Получить список компаний")
    def get_company(self) -> list:
        return self.db.execute(self.__scripts["get company list"]).fetchall()

    @allure.step("SQL. Получить список сотрудников")
    def get_employee(self) -> list:
        return self.db.execute(self.__scripts["get employee list"]).fetchall()

    @allure.step("SQL. Получить компанию по id")
    def get_company_by_id(self, id: str) -> list:
        return self.db.execute(self.__scripts["get company by id"],
                               company_id=id).fetchall()

    @allure.step("SQL. Получить сотрудника по id")
    def get_employee_by_id(self, id: str) -> list:
        return self.db.execute(self.__scripts["get employee by id"],
                               employee_id=id).fetchall()

    @allure.step("SQL. Получить список сотрудников компании с указанным id")
    def get_employee_by_company_id(self, company_id: str) -> list:
        return self.db.execute(self.__scripts[
            "get employee list by company id"
            ], company_id=company_id).fetchall()

    @allure.step("SQL. Получить последнего добавленного сотрудника")
    def get_employee_max_id(self) -> str:
        return self.db.execute(self.__scripts[
            "max id employee"
            ]).fetchall()[0][0]

    @allure.step("SQL. Создать компанию")
    def create_company(self, name: str, description: str):
        self.db.execute(self.__scripts[
            "insert company"
            ], new_name=name, new_descr=description)

    @allure.step("SQL. Удалить компанию")
    def delete_company(self, id: str):
        self.db.execute(self.__scripts[
            "delete company"
            ], id_delete=id)

    @allure.step("SQL. Удалить сотрудника")
    def delete_employee(self, id: str):
        self.db.execute(self.__scripts[
            "delete employee"
            ], id_delete=id)

    @allure.step("SQL. Получить последнюю добавленную компанию")
    def get_max_id_company(self) -> str:
        return self.db.execute(self.__scripts[
            "max id company"
            ]).fetchall()[0][0]

    @allure.step("SQL. Создать сотрудника")
    def create_employee(self, is_active: bool,
                        create_timestamp: object, change_timestamp: object,
                        first_name: str, last_name: str, middle_name: str,
                        phone: str, email: str, avatar_url: str, company_id: str):
        self.db.execute(self.__scripts[
            "create employee"
            ], is_active=is_active, create_timestamp=create_timestamp,
                        change_timestamp=change_timestamp,
                        first_name=first_name,
                        last_name=last_name,
                        middle_name=middle_name,
                        phone=phone,
                        email=email,
                        avatar_url=avatar_url,
                        company_id=company_id)

    @allure.step("SQL. Изменить данные сотрудника")
    def edit_employee(self, is_active: bool,
                      last_name: str, phone: str, email: str,
                      avatar_url: str, company_id: str):
        self.db.execute(self.__scripts["edit employee"],
                        is_active=is_active,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        avatar_url=avatar_url,
                        company_id=company_id)
