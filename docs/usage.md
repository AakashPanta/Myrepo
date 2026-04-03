# Usage

## Run the project

```bash
python3 -m src.main
```

## Run via CLI

```bash
python3 -m src.cli run
```

## Run with environment overrides

```bash
APP_ENV=production APP_DEBUG=true python3 -m src.cli run
```

## Run tests

```bash
pytest
```

## Expected default output

```text
Mr-Robot project initialized. Version: 8.0.0
Environment: development
Debug: False
```

## Expected override output

```text
Mr-Robot project initialized. Version: 8.0.0
Environment: production
Debug: True
```
