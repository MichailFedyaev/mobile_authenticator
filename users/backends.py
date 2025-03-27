from django.contrib.auth.backends import ModelBackend
from django.core.cache import cache
from users.models import User


class PhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username and password:
            user = User.objects.filter(phone=username).first()
            if user:
                # Проверяем код из кэша
                cached_code = cache.get(f'phone_confirm_{username}')
                if user.check_code(password) or password == cached_code:
                    # Очищаем код из кэша после успешной аутентификации
                    cache.delete(f'phone_confirm_{username}')
                    return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
