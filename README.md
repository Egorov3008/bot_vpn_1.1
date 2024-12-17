# 🚀 SoloBot

**SoloBot** — ваш идеальный помощник для управления API 3x-UI VPN на протоколе VLESS.  

Три версии — море возможностей:
  - v1.4 — бот для продажи ключей vless:

![Основные окна](preview.jpg)
  - v2.3.1 — стабильная версия подписок вместо ключей с кнопками автодобавления в приложение:

![Основные окна](preview_v_2.jpg)
  - v3.0.4_beta — полноценные подписки с выбором серверов из клиентского приложения (не в боте):



Если вам не хватает функций — направьте их в issue, мы реализуем

## 📋 Оглавление
1. [Описание](#описание)
2. [Стек технологий](#стек-технологий)
3. [Установка](#установка)
4. [Конфигурация](#конфигурация)
5. [Запуск](#запуск)
6. [Контакты](#контакты)

---

## 📖 Описание

SoloBot реализует множество функций, включая:


- **Выдача ключей на пробный период**.
- **Выдача ключей на длительные периоды** (1 месяц, 3 месяца, полгода, год).
- **Продление ключей** на указанные периоды.
- Полный контроль клиента над своими ключами:
  - Удаление ключей.
  - Продление ключей.
  - Просмотр информации о ключе (сервер, оставшееся время, сам ключ).
- **Смена локации** (перемещение ключа между серверами).
- Поддержка нескольких ключей для одного клиента (несколько устройств).
- **Реферальная программа** с пригласительной ссылкой.
- Доступ к **инструкциям**.
- **Пополнение баланса**:
    * через Юкасса (самозанятость и ИП)
    * через freekassa (Физические Лица)
    * Криптовалюта (Thanks [izzzzzi](https://github.com/izzzzzi))  
- Периодические **бэкапы базы данных клиентов**.
- Уведомления:
  - Произвольные сообщения через админку.
  - Уведомления о неиспользованных пробниках.
  - Уведомления о истекающих ключах (за сутки, за 6 часов и в момент истечения).
- **Чат поддержки** и канал для связи.
- **Автоматическое продление ключа** при наличии достаточного баланса.
- **Удобная админка прямо в боте**
- **мультисерверность** добавляй сервера в конфиг, и они автоматически будут в боте


---

## 💻 Стек технологий

Проект использует следующие технологии:

- **Python** версии 3.8 или выше.
- **Git** для клонирования репозитория.
- **Virtualenv** для создания виртуального окружения (рекомендуется).
- **PostgreSQL** для хранения данных.
- **Nginx** для работы с вебхуками.
- **aiogram** (версия 3.13) для взаимодействия с Telegram API.
- **youkassa** для обработки платежей.
- **aiohttp** для API запросов к панелям.

Проект полностью асинхронный, что обеспечивает высокую скорость работы.

---

## ⚙️ Установка

### 1️⃣ Шаг 1: Клонирование репозитория

Клонируйте репозиторий и перейдите в его директорию:

```bash
git clone https://github.com/Vladless/Solo_bot.git
cd solo_bot
```

### 2️⃣ Шаг 2: Создание и активация виртуального окружения

```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Шаг 3: Установка зависимостей

```
pip install -r requirements.txt
```

### 🛠️ Конфигурация

Для правильной работы вам нужно:

* установить и запустить postgresql, создать пользователя для работы с базой данных и выдать ему права
* Настроить ваш сервер на работу с ботом, выпустить SSL сертификат для домена
* Настроить вебхуки и пути до них в NGINX

* Создать файл config.py в корневой папке проекта с вашими данными:

```

API_TOKEN = токен вашего бота телеграм

ADMIN_USERNAME = логин от вашей панели x-ray
ADMIN_PASSWORD = пароль от вашей панели x-ray
ADD_CLIENT_URL = f"{API_URL}/panel/api/inbounds/addClient"
GET_INBOUNDS_URL = f"{API_URL}/panel/api/inbounds/list/"
AUTH_URL = f"{API_URL}/login/"
DATABASE_URL = путь к вашей базе данных, имеет вид "postgresql://{user}:{password}@{Ip-adress}:{port}/{имя базы данных}"
ADMIN_ID = ID телеграм профиля администратора
CHANNEL_URL = ссылка на ваш телеграм канал
YOOKASSA_SECRET_KEY = ваш ключ юкассы
YOOKASSA_SHOP_ID = ваш шопайди
WEBHOOK_HOST = адрес вашего сервера для вебхуков
WEBHOOK_PATH = '/webhook/' 
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
SUPPORT_CHAT_URL = ваша ссылка на поддержку 

```
**Мы высылаем детальный гайд и недостающие файлы в боте**

**Все описания в одном файле!** Удобно настроить бот под свой сервис изменив информацию и цены в одном месте

### 🚀 Запуск

введите команду из виртуального окружения

```
python main.py
```
### 🔗 SoloBot в Telegram и Полная версия

Попробуйте SoloBot прямо сейчас в Telegram [по этой ссылке](https://t.me/SoloNetVPN_bot).

Вы также можете поддержать автора или купить полную версию бота с сопровождением по установке в поддержке бота!
Полная пошаговая инстуркция по запуску бота предоставляется в поддержке бота