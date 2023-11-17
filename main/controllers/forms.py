import json

from flask import request, abort, Response, Blueprint

from main.logger import appLogger
from main.database import db
from main.models.field import Field
from main.models.form import Form
from main.repository.forms_repository import FormsMongoRepository
from main.services.forms_service import FormsService

forms_print = Blueprint('forms_api', __name__)

forms_repository = FormsMongoRepository()

forms_repository.set_db(db)
forms_service = FormsService(repos=forms_repository)

EXAMPLE_REQUEST = {
    'f_name1': 'FIELD_TYPE',
    'f_name2': 'FIELD_TYPE'
}


@forms_print.route('/get_form', methods=['POST'])
def get_form():
    """
    Endpoint for get exist form
    :return:
    """

    if request.method == 'POST':
        appLogger.info('/get_form', 'POST', 'get_form', request.json)

        if len(request.json) == 0:
            return Response(json.dumps(EXAMPLE_REQUEST), status=404,  mimetype='application/json')

        fields = forms_service.create_fields_list(init_data=request.json)

        form = forms_service.find_forms(fields=fields)

        if form is not None:
            max_len_form = max(form, key=len, default={})
            appLogger.info('find forms', max_len_form)
            return Response(max_len_form['name'], status=200, mimetype='application/json')

        appLogger.info('forms not found', form)
        return Response(json.dumps(EXAMPLE_REQUEST), status=404, mimetype='application/json')

    return abort(404)


@forms_print.route('/create_form', methods=['POST'])
def create_form():
    if request.method == 'POST':
        appLogger.info('/create_form', 'POST', 'create_form', request.json)

        if 'name' not in request.json:
            return Response("form must have name", status=400, mimetype='application/json')

        if len(request.json) < 2:
            return Response("form must have more 1 field", status=400, mimetype='application/json')

        fields = [Field(name=field_name, type=field_type) for field_name, field_type in request.json.items()]
        form = Form(name=request.json['name'], fields=fields)
        form_id = forms_service.create_form(form=form)

        return Response(f'{form_id}', status=201, mimetype='application/json')

    return abort(404)
