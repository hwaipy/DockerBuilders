version=$(cat ./version)
# echo $version
# docker login -u hwaipy
docker login
docker push hwaipy/ssr-client:$version