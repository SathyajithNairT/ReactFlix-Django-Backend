import json 
from django.core.management.base import BaseCommand
from flix_backend.models import ShowDataModel


class Command(BaseCommand):
    help = 'This loads data from JSON file into ShowDataModel with customized fields.'

    grouping = ''

    def add_arguments(self, parser):
        parser.add_argument('file_path', type= str, help= 'The file path of the JSON to load.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path) as jsonfile:
            data = json.load(jsonfile)

            objects = []
            for item in data:
                item.pop('id', None)

                item['grouping'] = self.grouping

                objects.append(ShowDataModel(**item))

        
        ShowDataModel.objects.bulk_create(objects)
        self.stdout.write(self.style.SUCCESS('Data successfully loaded with custom modification.'))