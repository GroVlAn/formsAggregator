from main.models.field import Field
from main.models.form import Form

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}


def test_repository_create_form(forms_repository):
    mock_data_forms = [
        {
            'name': 'Form Callback',
            'user_name': 'text',
            'user_phone': 'phone'
        },
        {
            'name': 'Form registration for service',
            'user_name': 'text',
            'user_phone': 'phone',
            'date': 'date'
        },
        {
            'name': 'Form registration',
            'user_name': 'text',
            'last_name': 'text',
            'first_name': 'text',
            'user_phone': 'phone',
            'user_email': 'email',
            'password': 'text',
        },
    ]

    for data in mock_data_forms:
        fields = [Field(name=field_name, type=field_type) for field_name, field_type in data.items()]
        form = Form(name=data['name'], fields=fields)
        form_id = forms_repository.create_form(form)

        assert form_id


def test_service_find_form(forms_service):

    fields_for_found = [
        Field(name='user_name', type='text'),
        Field(name='user_phone', type='phone')
    ]

    fields_for_not_found = [
        Field(name='user_name', type='text'),
        Field(name='password', type='text')
    ]

    forms_found = forms_service.find_forms(fields=fields_for_found)
    forms_not_found = forms_service.find_forms(fields=fields_for_not_found)

    assert len(forms_found) > 0
    assert len(forms_not_found) == 0


def test_service_create_form(forms_service):

    fields = [
        Field(name='user_name', type='text'),
        Field(name='user_phone', type='phone'),
        Field(name='date_service', type='date')
    ]
    new_form = Form(name='Form Service', fields=fields)

    form_id = forms_service.create_form(form=new_form)

    assert len(form_id) > 0


def test_get_form_not_found(client):
    mock_data = {
        "user_name": "Vlad",
        "password": '12345'
    }

    response = client.post('/get_form', json=mock_data)

    assert response.status_code == 404


def test_get_form_found(client):
    mock_data = {
        'user_name': 'Vlad',
        'user_phone': '+79205553535'
    }

    response = client.post('/get_form', json=mock_data, headers=headers)

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Form Callback'


def test_create_form(client):
    mock_data = {
        'name': 'Form sign in',
        'user_name': 'text',
        'password': 'text',
        'again_password': 'text'
    }

    response = client.post('/create_form', json=mock_data)

    assert response.status_code == 201
