## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
echo "----- Write key-value JSON string into 'default' configuration 'legacy' module. -----"
curl --silent -X POST -d"{'key1': 'value1', 'key2': [1, 2, 3]}" http://localhost/isa/conf/default/legacy
curl -X GET http://localhost/isa/conf/default/legacy
#
echo "----- Delet 'default' configuration 'legacy' module. -----"
curl -X DELETE http://localhost/isa/conf/default/legacy
curl -X GET http://localhost/isa/conf/default/legacy
