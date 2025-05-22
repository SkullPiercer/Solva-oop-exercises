def test_user_greet_method(create_users):
    for user in create_users:
        assert user.greet() == (
            f'Привет, меня зовут {user.name.capitalize()} '
            f'и мне {user.age} лет.'
        ), 'Обратите внимание, имя человека должно быть с большой буквы!'


def test_user_class_name(create_users):
    for user in create_users:
        assert type(user).__name__ == 'User', 'Не меняйте название класса!'
