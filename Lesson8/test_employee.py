from employeeApi import Employee


api = Employee("https://x-clients-be.onrender.com")

company_id = 3414


def test_get_employees_list():
    body = api.get_employee_list(company_id)
    assert len(body) > 1


def test_add_new_employee():
    fn = 'Peter'
    ln = 'Petrov'
    compId = company_id
    mail = 'api@kio.com'
    phonenum = '88005554545'
    is_active = True
    result = api.create_employee(
        firstname=fn, lastname=ln, companyId=compId,
        email=mail, phone=phonenum, isActive=is_active)
    employee_id = result['id']
    assert employee_id is not None
    # получить сотрудника по id
    new_employee = api.get_employee_by_id(employee_id)
    assert new_employee['id'] == employee_id


def test_change_employee_info():
    fn = 'Smith'
    ln = 'qwe@rty.ru'
    compId = company_id
    mail = 'api@kio.com'
    phonenum = '88005554545'
    is_active = True

    result = api.create_employee(
        firstname=fn, lastname=ln, companyId=compId,
        email=mail, phone=phonenum, isActive=is_active)
    new_id = result['id']

    new_last_name = 'Johns'
    new_mail = 'kdl@nndn.ru'
    new_phonenum = '88005550000'
    changed = api.change_info(
        new_id, new_lastname=new_last_name,
        new_email=new_mail, new_phone=new_phonenum)
    assert changed["id"] == new_id
    assert changed["isActive"] == is_active
