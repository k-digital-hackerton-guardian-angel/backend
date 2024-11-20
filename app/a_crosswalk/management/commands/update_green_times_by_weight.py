from django.core.management.base import BaseCommand
from a_crosswalk.models import Crosswalk
from datetime import time

class Command(BaseCommand):
    help = 'Update crosswalk green times based on management numbers with a weight multiplier'

    def add_arguments(self, parser):
        parser.add_argument('weight', type=float, help='Weight multiplier for green time (e.g., 0.3 or 0.5)')

    def handle(self, *args, **options):
        weight = options['weight']
        
        green_time_data = {
            "06-0000016829": [15.27950311, 16],
            "06-0000003514": [14.16149068, 0],
            "06-0000004860": [14.16149068, 16],
            "06-0000004863": [13.41614907, 16],
            "06-0000046683": [13.41614907, 0],
            "06-0000000512": [11.92546584, 1],
            "06-0000004869": [11.55279503, 1],
            "06-0000038785": [11.18012422, 1],
            "06-0000039131": [11.18012422, 1],
            "06-0000039473": [10.43478261, 22],
            "06-0000006441": [9.689440994, 23],
            "06-0000038747": [9.689440994, 23],
            "06-0000006442": [8.944099379, 17],
            "06-0000006506": [8.944099379, 21],
            "06-0000004865": [8.571428571, 16],
            "06-0000006448": [8.571428571, 7],
            "06-0000006449": [8.571428571, 7],
            "06-0000006454": [8.571428571, 20],
            "06-0000031765": [8.198757764, 21],
            "06-0000006272": [7.826086957, 13],
            "06-0000006443": [7.826086957, 23],
            "06-0000006452": [7.826086957, 16],
            "06-0000006453": [7.826086957, 12],
            "06-0000049113": [7.826086957, 18],
            "06-0000019178": [7.453416149, 20],
            "06-0000006158": [5.217391304, 18],
            "06-0000046448": [3.726708075, 18]
        }

        success_count = 0
        not_found_count = 0

        for manage_no, times in green_time_data.items():
            try:
                crosswalk = Crosswalk.objects.get(crslkManageNo=manage_no)
                crosswalk.increaseInGreenTime50 = round(times[0] * weight)
                
                start_hour = times[1]
                end_hour = (times[1] + 1) % 24  # Handle case when time is 23:00
                
                crosswalk.applyTimeFrom = time(hour=start_hour, minute=0)
                crosswalk.applyTimeTo = time(hour=end_hour, minute=0)
                
                crosswalk.save()
                success_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully updated {manage_no} with time {times[0] * weight} "
                        f"and apply time {start_hour}:00-{end_hour}:00"
                    )
                )
            except Crosswalk.DoesNotExist:
                not_found_count += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"Crosswalk with management number {manage_no} not found"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Updated {success_count} crosswalks with weight {weight}. {not_found_count} not found."
            )
        )