export PROJECT_NAME='py-music'
if [[ $(docker ps -a | grep $PROJECT_NAME | awk {'print $1'}) ]]; then
    echo "Killing containers for $PROJECT_NAME"
    docker kill $(docker ps -a | grep $PROJECT_NAME | awk {'print $1'})
fi
docker build -t $PROJECT_NAME .
docker run --rm -p 5000:5000 -it $PROJECT_NAME 

