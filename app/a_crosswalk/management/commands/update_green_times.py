from django.core.management.base import BaseCommand
from a_crosswalk.models import Crosswalk

class Command(BaseCommand):
    help = 'Update crosswalk green times based on management numbers'

    def handle(self, *args, **options):
        green_time_data = {
            "06-0000006454": [120, 72],
            "06-0000006452": [69.13043, 41.47826],
            "06-0000006442": [61.86335, 37.11801],
            "06-0000006506": [40.99379, 24.59627],
            "06-0000000512": [39.50311, 23.70186],
            "06-0000004869": [38.38509, 23.03106],
            "06-0000039131": [37.26708, 22.36025],
            "06-0000006453": [31.86335, 19.11801],
            "06-0000006448": [29.44099, 17.6646],
            "06-0000003514": [22.73292, 13.63975],
            "06-0000006449": [19.37888, 11.62733],
            "06-0000038785": [18.26087, 10.95652],
            "06-0000039473": [17.14286, 10.28571],
            "06-0000046683": [14.16149, 8.496894],
            "06-0000031765": [13.78882, 8.273292],
            "06-0000019178": [12.67081, 7.602484],
            "06-0000038747": [10.43478, 6.26087],
            "06-0000006441": [10.43478, 6.26087],
            "06-0000006443": [8.571429, 5.142857],
            "06-0000006272": [8.571429, 5.142857],
            "06-0000016829": [7.639752, 4.583851],
            "06-0000004860": [7.080745, 4.248447],
            "06-0000004863": [6.708075, 4.024845],
            "06-0000004865": [4.285714, 2.571429],
            "06-0000049113": [3.913043, 2.347826],
            "06-0000006158": [2.608696, 1.565217],
            "06-0000046448": [1.863354, 1.118012]
        }

        success_count = 0
        not_found_count = 0

        for manage_no, times in green_time_data.items():
            try:
                crosswalk = Crosswalk.objects.get(crslkManageNo=manage_no)
                crosswalk.increaseInGreenTime30 = round(times[0])
                crosswalk.increaseInGreenTime50 = round(times[1])
                crosswalk.save()
                success_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully updated {manage_no} with times {times[0]}, {times[1]}"
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