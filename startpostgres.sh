sudo docker rm shoreline_db
docker run --name shoreline_db -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 -v /var/local/:/var/lib/postgresql/data/  postgres
docker ps