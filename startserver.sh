docker stop djangorestserver
docker rm djangorestserver
docker pull gaurav28/farmerapp:latest
docker run --name djangorestserver -p 8000:8000 gaurav28/farmerapp:latest
docker ps