## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
echo "----- List all configuration file. -----"
curl -X GET http://localhost/isa/conf
#
echo "----- Show 'defualt' configuration file all content. -----"
## If configuration not exist, it will show '{}'.
curl -X GET http://localhost/isa/conf/default
#
echo "----- Show 'defualt' configuration file 'demo' module tag. -----"
## If 'demo' module tag not exist, it will exception error message.
curl -X GET http://localhost/isa/conf/default/demo
