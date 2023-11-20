# Forms Aggregator
___

## Before build app
___

You should create files dev.env and .env in the base directory and set next keys:

```
MONGO_ROOT_USER=#YOUR VALUE# // User Name for mongodb
DB_PASSWORD=#YOUR VALUE# // Password for mongodb
```

## For Unix like systems
___

Production mod run:
```
make run 
```

Development mod run:
```
make run-dev
```

Test Production mod run:
```
make test
```

Test Development mod run:
```
make test-dev
```

## For Windows
___

Production mod run:
```
docker-compose -f ./docker-compose.yml --env-file ./.env build
docker-compose -f ./docker-compose.yml --env-file ./.env up --remove-orphans -d
```

Development mod run:
```
docker-compose -f ./docker-compose.dev.yml --env-file ./dev.env build
docker-compose -f ./docker-compose.dev.yml --env-file ./dev.env up --remove-orphans -d
```

Test Production mod run:
```
docker exec forms-aggregator pytest
```

Test Development mod run:
```
docker exec forms-aggregator-dev pytest
```
