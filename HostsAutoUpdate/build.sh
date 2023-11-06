version=$(cat ./version)
# echo $version

docker build -t hwaipy/hostsautoupdate:$version .