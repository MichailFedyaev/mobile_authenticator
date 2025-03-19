# Mobile Authenticator

Система авторизации по номеру телефона с реферальной системой.

## Описание

Проект представляет собой систему авторизации пользователей по номеру телефона с поддержкой реферальной системы. 
Пользователи могут регистрироваться, авторизовываться и использовать инвайт-коды для приглашения других пользователей.

## Функциональность

- Авторизация по номеру телефона с подтверждением через SMS
- Реферальная система с инвайт-кодами
- API для всех операций
- Веб-интерфейс для тестирования

## Требования

- Python 3.8+
- PostgreSQL
- Redis (для кэширования)
- SMS Aero API ключ

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/MichailFedyaev/mobile_authenticator.git
cd mobile_authenticator
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
.venv\Scripts\activate  # для Windows
```


4. Создайте файл .env на основе .env_sample и заполните необходимые переменные:
```bash
cp .env_sample .env
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Запустите сервер:
```bash
python manage.py runserver
```

## API Endpoints

### Регистрация и авторизация

#### POST /api/register/
Регистрация нового пользователя или запрос кода подтверждения для существующего.

**Request:**
```json
{
    "phone": "+79001234567",
    "invited_by": "ABC123"  
}
```

**Response:**
```json
{
    "message": "Код отправлен"
}
```

#### POST /api/verify-code/
Подтверждение кода авторизации.

**Request:**
```json
{
    "phone": "+79001234567",
    "code": "1234"
}
```

**Response:**
```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

### Профиль пользователя

#### GET /api/profile/
Получение информации о текущем пользователе.

**Response:**
```json
{
    "id": 1,
    "phone": "+79001234567",
    "invite_code": "ABC123",
    "invited_by_user": {
        "id": 2,
        "phone": "+79007654321",
        "invite_code": "XYZ789"
    },
    "created_at": "2024-03-12T12:00:00Z",
    "invited_users": [
        {
            "id": 3,
            "phone": "+79009876543"
        }
    ]
}
```

## Тестирование

Для запуска тестов выполните:
```bash
python manage.py test
```

## Документация API

Подробная документация API доступна по адресу `/api/docs/` после запуска сервера.

## Postman Collection

Postman коллекция для тестирования API доступна в файле `mobile_authenticator.postman_collection.json`. 