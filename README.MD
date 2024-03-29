# Микросервис для электронного магазина
Модель/cущности:
```
Товар - отвечает за товар на складе, например - телефон такой-то марки от такого-то производителя.
Поля:
идентификатор (ID)
название
описание
параметры: массив пар ключ/значение
```
Сущности хранятся в MongoDB на localhost:27017

REST API методы:
```
Создать новый товар
Получить список названий товаров, с возможностью фильтрации по:
a) названию
b) выбранному параметру и его значению
Получить детали товара по ID
```
Методы принимают JSON на входе и отдают JSON на выходе.


# Основа
```
    Python==3.8
    MongoDB==4.4.2
```
# Требования
```
pip install -r requirements.txt
```
## Запуск приложения
```
python main.py
```

## Пример curl команд
- Создать товар
```
curl -X POST "http://0.0.0.0:8000/create" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"product\":{\"name\":\"Iphone11\",\"description\":\"Phone from Apple\",\"options\":{\"os\":\"Ios\",\"year\":\"2018\"}}}"
```
В базе появится запись вида
```
{
  "product": {
    "name": "Iphone11",
    "description": "Phone from Apple",
    "options": {
      "os": "Ios",
      "year": "2018"
    }
  }
}
```

- Найти все товары
```
curl -X GET "http://0.0.0.0:8000/retrieve_productname_by_name" -H  "accept: application/json"
```
Запрос вернет названия товаров
```
[
  "Iphone12",
  "Iphone11"
]
```
- Фильтр по имени
```
curl -X GET "http://0.0.0.0:8000/retrieve_productname_by_name?name=Iphone11" -H  "accept: application/json"
```
Запрос отфильтрует названия товаров
```
[
  "Iphone11"
]
```
- Поиск по параметру
```
curl -X POST "http://0.0.0.0:8000/retrieve_productname_by_options" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"os\":\"Ios\",\"year\":\"2018\"}"
```
```
[
  "Iphone11"
]
```

- Если нужны все данные о продукте по названию.
```
curl -X GET "http://0.0.0.0:8000/retrieve_product_by_name?name=Iphone11" -H  "accept: application/json"
```
Запрос вернёт массив всех продуктов с таким названием и полную информацию о них
```
[
  {
    "_id": {
      "$oid": "5fba464789101a405e215110"
    },
    "name": "Iphone11",
    "description": "Phone from Apple",
    "options": {
      "os": "Ios",
      "year": "2018"
    }
  },
  {
    "_id": {
      "$oid": "5fba4671e2285a1eabfd685b"
    },
    "name": "Iphone11",
    "description": "Phone from Apple",
    "options": {
      "os": "Ios",
      "year": "2019"
    }
  }]
```


- Поиск товара по ID
```
curl -X GET "http://0.0.0.0:8000/retrieve_product_by_id?_id=5fba4671e2285a1eabfd685b" -H  "accept: application/json"
```
Если ID в MongoDB = 5fba4671e2285a1eabfd685b
```
{
    "_id": {
      "$oid": "5fba4671e2285a1eabfd685b"
    },
    "name": "Iphone11",
    "description": "Phone from Apple",
    "options": {
      "os": "Ios",
      "year": "2019"
    }
  }
```
