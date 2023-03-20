version=$(cat ./version)
# echo $version

docker build -t hwaipy/ssr-client:$version .