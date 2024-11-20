from django.core.management.base import BaseCommand
from a_crosswalk.models import Crosswalk
from datetime import time

class Command(BaseCommand):
    help = 'Update crosswalk green times based on management numbers'

    def handle(self, *args, **options):
        green_time_data = {
            "06-0000006454": [120, 72, 20],
            "06-0000006452": [69.13043, 41.47826, 16],
            "06-0000006442": [61.86335, 37.11801, 17],
            "06-0000006506": [40.99379, 24.59627, 21],
            "06-0000000512": [39.50311, 23.70186, 1],
            "06-0000004869": [38.38509, 23.03106, 1],
            "06-0000039131": [37.26708, 22.36025, 1],
            "06-0000006453": [31.86335, 19.11801, 12],
            "06-0000006448": [29.44099, 17.6646, 7],
            "06-0000003514": [22.73292, 13.63975, 0],
            "06-0000006449": [19.37888, 11.62733, 7],
            "06-0000038785": [18.26087, 10.95652, 1],
            "06-0000039473": [17.14286, 10.28571, 22],
            "06-0000046683": [14.16149, 8.496894, 0],
            "06-0000031765": [13.78882, 8.273292, 21],
            "06-0000019178": [12.67081, 7.602484, 20],
            "06-0000038747": [10.43478, 6.26087, 23],
            "06-0000006441": [10.43478, 6.26087, 23],
            "06-0000006443": [8.571429, 5.142857, 23],
            "06-0000006272": [8.571429, 5.142857, 13],
            "06-0000016829": [7.639752, 4.583851, 16],
            "06-0000004860": [7.080745, 4.248447, 16],
            "06-0000004863": [6.708075, 4.024845, 16],
            "06-0000004865": [4.285714, 2.571429, 16],
            "06-0000049113": [3.913043, 2.347826, 18],
            "06-0000006158": [2.608696, 1.565217, 18],
            "06-0000046448": [1.863354, 1.118012, 18]
        }

        success_count = 0
        not_found_count = 0

        for manage_no, times in green_time_data.items():
            try:
                crosswalk = Crosswalk.objects.get(crslkManageNo=manage_no)
                crosswalk.increaseInGreenTime30 = round(times[0])
                crosswalk.increaseInGreenTime50 = round(times[1])
                
                # Set apply times based on the last value
                start_hour = times[2]
                end_hour = (times[2] + 1) % 24  # Handle case when time is 23:00
                
                crosswalk.applyTimeFrom = time(hour=start_hour, minute=0)
                crosswalk.applyTimeTo = time(hour=end_hour, minute=0)
                
                crosswalk.save()
                success_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully updated {manage_no} with times {times[0]}, {times[1]} "
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
                f"Updated {success_count} crosswalks. {not_found_count} not found."
            )
        )