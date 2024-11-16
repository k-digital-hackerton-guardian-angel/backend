# app/a_crosswalk/management/commands/import_crosswalks.py

import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from a_crosswalk.models import Crosswalk, CrosswalkManagement

class Command(BaseCommand):
    help = 'Import crosswalk data from an Excel file into the database.'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='The path to the Excel file to import.')

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']
        
        try:
            # Read the Excel file
            df = pd.read_excel(excel_file)
        except Exception as e:
            raise CommandError(f"Error reading Excel file: {e}")
        
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            try:
                # Create or get the CrosswalkManagement instance
                management, created = CrosswalkManagement.objects.get_or_create(
                    alias=row.get('alias', f"Alias_{index}"),
                    defaults={
                        'extension_time': row['extension_time'],
                        'application_time': row['application_time'],
                        'is_active': row.get('is_active', True)
                    }
                )

                # Create the Crosswalk instance
                crosswalk = Crosswalk.objects.create(
                    ctprvnNm=row['ctprvnNm'],
                    signguNm=row['signguNm'],
                    roadNm=row['roadNm'],
                    rdnmadr=row['rdnmadr'],
                    lnmadr=row['lnmadr'],
                    crslkManageNo=row['crslkManageNo'],
                    crslkKnd=row['crslkKnd'],
                    bcyclCrslkCmbnatYn=row['bcyclCrslkCmbnatYn'],
                    highlandYn=row['highlandYn'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    cartrkCo=row['cartrkCo'],
                    bt=row['bt'],
                    et=row['et'],
                    tfclghtYn=row['tfclghtYn'],
                    fnctngSgngnrYn=row['fnctngSgngnrYn'],
                    sondSgngnrYn=row['sondSgngnrYn'],
                    greenSgngnrTime=row['greenSgngnrTime'],
                    redSgngnrTime=row['redSgngnrTime'],
                    tfcilndYn=row['tfcilndYn'],
                    ftpthLowerYn=row['ftpthLowerYn'],
                    brllBlckYn=row['brllBlckYn'],
                    cnctrLghtFcltyYn=row['cnctrLghtFcltyYn'],
                    institutionNm=row['institutionNm'],
                    phoneNumber=row['phoneNumber'],
                    referenceDate=row['referenceDate'],
                    instt_code=row['instt_code'],
                    management=management
                )

                self.stdout.write(self.style.SUCCESS(f"Successfully imported Crosswalk ID: {crosswalk.id}"))

            except Exception as e:
                self.stderr.write(f"Error importing row {index}: {e}")