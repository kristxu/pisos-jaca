name: Pisos Jaca - Alertas

on:
  schedule:
    - cron: "*/30 * * * *"  # cada 30 minutos
  workflow_dispatch:

jobs:
  bot:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Instalar dependencias
        run: |
          pip install requests

      - name: Ejecutar sistema de alertas
        env:
          TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
        run: |
          python bot.py
