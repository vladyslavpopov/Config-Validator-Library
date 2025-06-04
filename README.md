# Config Validator

Простий та гнучкий інструмент для валідації конфігураційних файлів у форматах JSON, YAML та TOML. Дозволяє визначати схеми валідації, перевіряти типи даних, обов'язкові поля, діапазони значень та інші правила.

Виконали студенти групи ІМ-33:

Бондар Ярослав, Владислав Попов

---

## Особливості

Підтримка JSON, YAML та TOML файлів  
Валідація типів даних (`str`, `int`, `bool`, `list`, `dict` тощо)  
Перевірка обов'язкових полів  
Валідація діапазонів значень (`min`/`max`)  
Перевірка за регулярними виразами (`regex`)  
Кастомні валідатори  
Умовні поля ("якщо поле X має значення Y, то поле Z обов'язкове")  
Детальні повідомлення про помилки  

---

## Встановлення

```bash
git clone https://github.com/vladyslavpopov/Config-Validator-Library
cd config-validator
pip install -e .
```

---

## Використання

### 1. Як бібліотека Python

#### Простий приклад ([schema_example.py](schema_example.py)):

```python
from config_validator import Schema, parse_config, validate

# Визначення схеми
schema = Schema()
schema.add_field("database.host", str, required=True)
schema.add_field("database.port", int, min_value=1024, max_value=65535)
schema.add_field("debug", bool, required=False)

# Валідація
config = parse_config("config.json")
validate(config, schema)
print("Конфігурація валідна!")
```

#### Розширений приклад ([advanced_example.py](advanced_example.py)):

```python
schema = Schema()
schema.add_field("app.name", str, regex=r"^[a-zA-Z0-9_]+$")
schema.add_field("app.port", int, min_value=1024, max_value=65535)

# Кастомний валідатор
def is_odd_port(port: int) -> bool:
    return port % 2 == 1

schema.add_validator("app.port", is_odd_port)
```

---

---

## Приклади конфігурацій

### 1. `basic_config.json`
```json
{
  "database": {
    "host": "localhost",
    "port": 5432
  },
  "debug": false
}
```

### 2. `complex_config.yaml`
```yaml
app:
  name: "MyApp"
  ports: [8080, 9001]
database:
  primary:
    host: "db.example.com"
```

### 3. `advanced_config.toml`
```toml
[app]
name = "MyApp"
port = 8081
hosts = ["example.com"]
```

---

## Формат схеми валідації

Схему можна задавати:
- **У коді Python** (через клас `Schema`)
- **У зовнішньому файлі** (YAML/JSON)

### Приклад схеми (`schema.yaml`):

```yaml
fields:
  app.name:
    type: str
    required: true
  app.port:
    type: int
    min: 1024
    max: 65535
  database.host:
    type: str
    regex: "^[a-z0-9.-]+$"
```

---

## Обробка помилок

Приклад виводу при помилці:
```bash
❌ Validation failed: Unsupported file format. Use JSON, YAML, or TOML.
```

Типи помилок:
- `MissingFieldError` – відсутнє обов'язкове поле
- `ValidationError` – невідповідність типу/діапазону/патерну
- `InvalidFileFormatError` – непідтримуваний формат файлу

---

---

## Розробка

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/your-repo/config-validator.git
   ```

2. Встановіть залежності:
   ```bash
   pip install -e ".[dev]"
   ```

3. Запустіть тести:
   ```bash
   pytest tests/
   ```
