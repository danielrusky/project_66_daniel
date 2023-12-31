Описание задач
1 Реализуйте интерфейс заполнения рассылок, то есть CRUD-механизм для управления рассылками. 2 Реализуйте скрипт рассылки, который работает как из командой строки, так и по расписанию. 3 Добавьте настройки конфигурации для периодического запуска задачи.

Сущности системы
1 Клиент сервиса: -контактный email, -ФИО, -комментарий.

2 Рассылка (настройки): -время рассылки; -периодичность: раз в день, раз в неделю, раз в месяц; -статус рассылки: завершена, создана, запущена.

3 Сообщение для рассылки: -тема письма, -тело письма.

4 Логи рассылки: -дата и время последней попытки; -статус попытки; -ответ почтового сервера, если он был.

Не забудьте про связи между сущностями. Вы можете расширять модели для сущностей в произвольном количестве полей либо добавлять вспомогательные модели.

Логика работы системы
После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания, то должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки, и запущена отправка для всех этих клиентов.
Если создается рассылка со временем старта в будущем, то отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
По ходу отправки сообщений должна собираться статистика (см. описание сущности «сообщение» и «логи» выше) по каждому сообщению для последующего формирования отчетов.
Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.
‍Рекомендации
Реализовать интерфейс можно с помощью UI kit Bootstrap.
Для работы с периодическими задачами можно использовать либо crontab-задачи в чистом виде, либо изучить дополнительно библиотеку: https://pypi.org/project/django-crontab/
