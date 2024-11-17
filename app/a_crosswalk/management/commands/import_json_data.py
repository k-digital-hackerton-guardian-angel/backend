import json
from django.core.management.base import BaseCommand, CommandError
from a_crosswalk.models import Crosswalk, CrosswalkManagement
from django.db import transaction
from datetime import datetime, time

class Command(BaseCommand):
    help = 'Import crosswalk data from JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            success_count = 0
            error_count = 0

            for item in data:
                try:
                    with transaction.atomic():
                        crosswalk_data = item['crosswalk']
                        
                        # Create CrosswalkManagement
                        management = CrosswalkManagement.objects.create(
                            alias=item['management']['alias'],
                            extension_time=item['management'].get('extension_time', '00:05:00'),
                            application_time=item['management'].get('application_time', '00:10:00'),
                            is_active=item['management'].get('is_active', True)
                        )

                        # Create Crosswalk
                        crosswalk = Crosswalk.objects.create(
                            management=management,
                            ctprvnNm=crosswalk_data.get('ctprvnNm', ''),
                            signguNm=crosswalk_data.get('signguNm', ''),
                            roadNm=crosswalk_data.get('roadNm', ''),
                            rdnmadr=crosswalk_data.get('rdnmadr', ''),
                            lnmadr=crosswalk_data.get('lnmadr', ''),
                            crslkManageNo=crosswalk_data.get('crslkManageNo', ''),
                            crslkKnd=crosswalk_data.get('crslkKnd', ''),
                            bcyclCrslkCmbnatYn=crosswalk_data.get('bcyclCrslkCmbnatYn', False),
                            highlandYn=crosswalk_data.get('highlandYn', False),
                            latitude=float(crosswalk_data.get('latitude', 0)),
                            longitude=float(crosswalk_data.get('longitude', 0)),
                            cartrkCo=int(crosswalk_data.get('cartrkCo', 0)),
                            bt=crosswalk_data.get('bt', '00:00:00'),
                            et=crosswalk_data.get('et', '00:00:00'),
                            tfclghtYn=crosswalk_data.get('tfclghtYn', False),
                            fnctngSgngnrYn=crosswalk_data.get('fnctngSgngnrYn', False),
                            sondSgngnrYn=crosswalk_data.get('sondSgngnrYn', False),
                            greenSgngnrTime=crosswalk_data.get('greenSgngnrTime', '00:00:00'),
                            redSgngnrTime=crosswalk_data.get('redSgngnrTime', '00:00:00'),
                            tfcilndYn=crosswalk_data.get('tfcilndYn', False),
                            ftpthLowerYn=crosswalk_data.get('ftpthLowerYn', False),
                            brllBlckYn=crosswalk_data.get('brllBlckYn', False),
                            cnctrLghtFcltyYn=crosswalk_data.get('cnctrLghtFcltyYn', False),
                            institutionNm=crosswalk_data.get('institutionNm', ''),
                            phoneNumber=crosswalk_data.get('phoneNumber', ''),
                            referenceDate=datetime.strptime(
                                crosswalk_data.get('referenceDate', '2024-01-01'),
                                '%Y-%m-%d'
                            ).date(),
                            instt_code=crosswalk_data.get('instt_code', ''),
                            instt_name=crosswalk_data.get('institutionNm', '')
                        )
                        success_count += 1
                        self.stdout.write(
                            self.style.SUCCESS(f"Successfully imported Crosswalk ID: {crosswalk.id}")
                        )

                except Exception as e:
                    error_count += 1
                    self.stderr.write(
                        self.style.ERROR(f"Error importing crosswalk: {str(e)}")
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"\nImport completed. Success: {success_count}, Errors: {error_count}"
                )
            )

        except Exception as e:
            raise CommandError(f"Error reading JSON file: {str(e)}")
