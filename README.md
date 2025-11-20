# Repo to share MlOps files

## airflow_mlflow folder for MLOps.Inception materials.
Обратите внимание, что docker-compose-windows.yml не монтирует вольюмы в ваши папки.

Если вы запустили docker-compose up  и контейнеры поднялись, но при этом зайти в Airflow вы не можете
ТО: сначала остановим контейнеры ctrl+c  и ...
1. ослабляем права из под супер пользователя: sudo chmod -R 777 /opt
2. задаем окружение: echo -e "AIRFLOW_UID=$(id -u)" > .env
3. удаляем: docker-compose down --volumes --remove-orphans
4. создаем папки вручную: mkdir logs dags plugins
5. И снова запускаем: docker-compose up
