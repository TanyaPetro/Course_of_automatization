from XclientsAPI import Api
from sql_stuff import sqlStuff
import datetime


db_connection_string = "postgresql://x_clients_user:\
    95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-\
        a.frankfurt-postgres.render.com/x_clients_db_fxd0"
sql = sqlStuff(db_connection_string)
url = "https://x-clients-be.onrender.com"
api = Api(url)


def test_create_new_employee():
    name = "Hogwarts"
    descr = "School of Witchcraft and Wizardry"
    sql.create_company(name, descr)
    company_id = sql.get_max_id_company()
    employee_list = sql.get_employee_by_company_id(company_id)
    api.add_employee(
        id="474",
        first_name="Harry",
        last_name="Potter",
        middle_name="James",
        company_id=company_id,
        email="hp@hogwarts.gb",
        employee_url="http://hogwarts.gb",
        phone="89991313666",
        birthdate='1980-07-01',
        is_active=True
    )
    employee_id = sql.get_employee_max_id()
    employee_updated_list = sql.get_employee_by_company_id(company_id)
    assert len(employee_list) < len(employee_updated_list)
    assert sql.get_company_by_id(company_id)[0]["name"] == "Hogwarts"
    assert sql.get_company_by_id(company_id)[0]
    ["description"] == "School of Witchcraft and Wizardry"
    assert sql.get_employee_by_id(employee_id)[0]["first_name"] == "Harry"
    assert sql.get_employee_by_id(employee_id)[0]["last_name"] == "Potter"
    assert sql.get_employee_by_id(employee_id)[0]["middle_name"] == "James"
    # assert sql.get_employee_by_id(employee_id)
    # [0]["email"] == "hp@hogwarts.gb"
    assert sql.get_employee_by_id(employee_id)[0]
    ["avatar_url"] == "http://hogwarts.gb"
    assert sql.get_employee_by_id(employee_id)[0]["phone"] == "89991313666"
    assert sql.get_employee_by_id(employee_id)[0]
    ["birthdate"] == datetime.date(1980, 7, 1)
    assert sql.get_employee_by_id(employee_id)[0]["is_active"] is True
    sql.delete_employee(employee_id)
    sql.delete_company(company_id)


def test_edit_employee():
    name = "TheBurrow"
    descr = "Home"
    sql.create_company(name, descr)
    company_id = sql.get_max_id_company()
    employee = api.add_employee(
        id="4242",
        first_name="Arthur",
        last_name="Weasle",
        middle_name="Septimus",
        company_id=company_id,
        email="Arthur@weasly.gb",
        employee_url="http://weasly.gb",
        phone="89990909009",
        birthdate='1955-02-06',
        is_active=True
    )
    api.edit_employee(
        id=employee,
        edit_lastName="Weasley",
        edit_email="Arthur@weasley.gb",
        edit_url="http://weasley.gb",
        edit_phone="89990909090",
        edit_status=False
    )
    updated_employee = sql.get_employee_max_id()
    assert sql.get_company_by_id(company_id)[0]["name"] == "TheBurrow"
    assert sql.get_company_by_id(company_id)[0]["description"] == "Home"
    assert sql.get_employee_by_id(updated_employee)[0]
    ["last_name"] == "Weasley"
    assert sql.get_employee_by_id(updated_employee)[0]
    ["email"] == "Arthur@weasley.gb"
    assert sql.get_employee_by_id(updated_employee)[0]
    ["birthdate"] == datetime.date(1955, 2, 6)
    assert sql.get_employee_by_id(updated_employee)[0]["is_active"] is False
    sql.delete_employee(updated_employee)
    sql.delete_company(company_id)
