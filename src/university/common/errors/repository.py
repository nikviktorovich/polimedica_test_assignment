class RepositoryError(Exception):
    """Родительский класс для всех ошибок репозитория объектов"""


class EntityNotFoundError(RepositoryError):
    """Выбрасывается, когда объект не найден в репозитории объектов"""
