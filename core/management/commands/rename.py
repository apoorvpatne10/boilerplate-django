import os
from django.core.management import BaseCommand

project_name = 'prac'


class Command(BaseCommand):
    help = "Renames the django project"

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str,
                            help="The new django project name")

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # logic to rename the project
        files_to_rename = [
            f'{project_name}/settings/base.py',
            f'{project_name}/wsgi.py',
            'manage.py']
        folder_to_rename = f'{project_name}'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(f'{project_name}', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS(
            f'Project has been renamed to {new_project_name}'))
