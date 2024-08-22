import requests


class Employee:

    def __init__(self, url):
        self.url = url

    # получение списка сотрудников компании
    def get_employee_list(self, company_id):
        resp = requests.get(self.url + '/employee' + str(company_id))
        return resp.json()

    # авторизация
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    # добавление нового сотрудника

    def create_employee(self, firstname, lastname,
                        companyId, email, phone, isActive):
        employee = {
            'firstName': firstname,
            'lastName': lastname,
            'companyId': companyId,
            'email': email,
            'phone': phone,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',
                             json=employee, headers=my_headers)
        return resp.json()
    # получение сотрудника по id

    def get_employee_by_id(self, employee_id):
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()
    # изменение информации о сотруднике

    def change_info(
            self, employee_id, new_lastname,
            new_email, new_phone):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        new_employee = {
            "lastName": new_lastname,
            "email": new_email,
            "phone": new_phone
            }
        resp = requests.patch(self.url + '/employee/' + str(employee_id),
                              headers=my_headers, json=new_employee)
        return resp.json()
