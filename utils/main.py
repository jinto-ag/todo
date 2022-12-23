from django.db.models import fields
from base import Field

# Python Objects
def create_variable(name, value, options):pass
def create_function(name, args, kwargs, body, options):pass
def create_class(name, parents, class_varialbles, methods, options):pass
def create_method(class_name, name, options):pass
def create_statement(name, options):pass
def create_block(header, body, options):pass

# Django related
def create_project(name, options):pass
def create_app(name, options):pass
def create_text_file(name, path, options, blank=True):pass
def create_html_file(name, path, options):pass
def create_field(name, class_name, options):pass
def create_form(app_name, form_name, form_fields):pass
def create_model_form(app_name, model, fields: list):pass
def create_model(app_name, model_name, model_fields):pass
def create_url_set(app_name, view_set):pass
def create_url(app_name, view_name, pattern):pass
def create_view_set(app_name, model):pass
def create_view(app_name, name, options):pass


def main():
    pass


if __name__ == "__main__":
    main()
