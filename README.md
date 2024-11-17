```
git clone https://github.com/k-digital-hackerton-guardian-angel/backend.git
```

```
cd backend
```

```
poetry install
```

```
poetry shell
```

```
cd app
```

```
python manage.py runserver
```




### json데이터 임포트
```
python manage.py excel_to_json data/crosswalk-initial-data.xls data/crosswalk-data.json
```

```
docker-compose exec web python manage.py excel_to_json data/crosswalk-initial-data.xls data/crosswalk-data.json
```





활용 api
CSV 전국횡단보도표준데이터
https://www.data.go.kr/data/15028201/standard.do