version=$(cat ./version)
# echo $version

docker build -t hwaipy/codeserver:$version .