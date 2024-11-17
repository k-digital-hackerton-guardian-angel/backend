import pandas as pd
import json
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, time

class Command(BaseCommand):
    help = 'Convert Excel file to JSON format'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')
        parser.add_argument('json_file', type=str, help='Path to output JSON file')

    def convert_to_time(self, value):
        try:
            if pd.isna(value):
                return None
            total_minutes = int(float(value)) % (24 * 60)
            hours = total_minutes // 60
            minutes = total_minutes % 60
            return time(hour=hours, minute=minutes).strftime('%H:%M:%S')
        except (ValueError, TypeError):
            return None

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']
        json_file = kwargs['json_file']

        try:
            # Read Excel file and print columns for debugging
            df = pd.read_excel(excel_file, skiprows=1)
            self.stdout.write(f"Available columns in Excel: {df.columns.tolist()}")

            # Column mapping with Korean names
            column_mapping = {
                '시도명': 'ctprvnNm',
                '시군구명': 'signguNm',
                '도로명': 'roadNm',
                '소재지도로명주소': 'rdnmadr',
                '소재지지번주소': 'lnmadr',
                '횡단보도관리번호': 'crslkManageNo',
                '횡단보도종류': 'crslkKnd',
                '자전거횡단도겸용여부': 'bcyclCrslkCmbnatYn',
                '고원식적용여부': 'highlandYn',
                '위도': 'latitude',
                '경도': 'longitude',
                '차로수': 'cartrkCo',
                '횡단보도폭': 'bt',
                '횡단보도연장': 'et',
                '보행자신호등유무': 'tfclghtYn',
                '보행자작동신호기유무': 'fnctngSgngnrYn',
                '음향신호기설치여부': 'sondSgngnrYn',
                '녹색신호시간': 'greenSgngnrTime',
                '적색신호시간': 'redSgngnrTime',
                '교통섬유무': 'tfcilndYn',
                '보도턱낮춤여부': 'ftpthLowerYn',
                '점자블록유무': 'brllBlckYn',
                '집중조명시설유무': 'cnctrLghtFcltyYn',
                '관리기관명': 'institutionNm',
                '관리기관전화번호': 'phoneNumber',
                '데이터기준일자': 'referenceDate',
                '제공기관코드': 'instt_code'
            }

            # Check which columns are actually present
            available_columns = {}
            for kr_col, en_col in column_mapping.items():
                if kr_col in df.columns:
                    available_columns[kr_col] = en_col
                else:
                    self.stdout.write(f"Warning: Column '{kr_col}' not found in Excel file")

            # Rename only the columns that exist
            df = df.rename(columns=available_columns)

            # Convert boolean columns (only if they exist)
            boolean_columns = [
                'bcyclCrslkCmbnatYn', 'highlandYn', 'tfclghtYn',
                'fnctngSgngnrYn', 'sondSgngnrYn', 'tfcilndYn',
                'ftpthLowerYn', 'brllBlckYn', 'cnctrLghtFcltyYn'
            ]
            for col in boolean_columns:
                if col in df.columns:
                    df[col] = df[col].map({'Y': True, 'N': False})

            # Convert numeric values (only if they exist)
            numeric_columns = ['cartrkCo', 'latitude', 'longitude']
            for col in numeric_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            # Convert time fields (only if they exist)
            time_columns = ['bt', 'et', 'greenSgngnrTime', 'redSgngnrTime']
            for col in time_columns:
                if col in df.columns:
                    df[col] = df[col].apply(self.convert_to_time)

            # Convert date (only if it exists)
            if 'referenceDate' in df.columns:
                df['referenceDate'] = pd.to_datetime(df['referenceDate']).dt.strftime('%Y-%m-%d')

            # Create JSON structure
            json_data = []
            for index, row in df.iterrows():
                # Create management data
                management_data = {
                    "alias": f"Crosswalk_{index}" if 'crslkManageNo' not in row else f"Crosswalk_{row['crslkManageNo']}",
                    "extension_time": "00:05:00",
                    "application_time": "00:10:00",
                    "is_active": True
                }

                # Create crosswalk data (only include columns that exist)
                crosswalk_data = {}
                for col in df.columns:
                    value = row[col]
                    if pd.notnull(value):
                        crosswalk_data[col] = value

                combined_data = {
                    "management": management_data,
                    "crosswalk": crosswalk_data
                }
                
                json_data.append(combined_data)

            # Write to JSON file
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)

            self.stdout.write(
                self.style.SUCCESS(f'Successfully converted Excel to JSON: {json_file}')
            )

        except Exception as e:
            import traceback
            self.stderr.write(self.style.ERROR(f"Error converting Excel to JSON: {str(e)}"))
            self.stderr.write(self.style.ERROR(traceback.format_exc()))
            raise CommandError(f"Error converting Excel to JSON: {str(e)}")