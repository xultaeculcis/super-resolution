az login --tenant 2fc4759d-c9f0-495f-a1b2-96245e1c8035
az acr login --name aipocregistry
docker build -t sr .
docker tag sr aipocregistry.azurecr.io/sr-app
docker push aipocregistry.azurecr.io/sr-app