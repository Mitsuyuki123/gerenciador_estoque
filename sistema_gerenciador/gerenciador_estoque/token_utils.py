from django.conf import settings

from itsdangerous import URLSafeTimedSerializer


def gerar_token(user_id):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    return serializer.dumps(user_id, salt=settings.SECRET_KEY)


def verificar_token(token, max_age=3600):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    try:
        user_id = serializer.loads(token, salt=settings.SECRET_KEY, max_age=max_age)
        return user_id
    except Exception:
        return None
