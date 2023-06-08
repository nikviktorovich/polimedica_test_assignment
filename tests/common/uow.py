import university.service.unit_of_work


class FakeUOW(university.service.unit_of_work.UnitOfWork):
    """Тестовая единица работы"""
    def __init__(self, **repos) -> None:
        """Инициализирует тестовую единицу работы
        
        Аргументы:
            repos: Словарь репозиториев вида: 'имя_репозитория': 'репозиторий'
        """
        for repo_name, repo in repos.items():
            setattr(self, repo_name, repo)
    

    def commit(self) -> None:
        """Подтверждает внесенные изменения"""
        pass
    

    def rollback(self) -> None:
        """Откатывает внесенные изменения"""
        pass
    

    def __enter__(self) -> university.service.unit_of_work.UnitOfWork:
        """Инициализирует репозитории при входе в контекст"""
        return self
    

    def __exit__(self, *args, **kwargs) -> None:
        """Заканчивает сессию при выходе из контекста"""
        pass
