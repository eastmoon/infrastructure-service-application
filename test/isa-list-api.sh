## Declare alias
## Execute script
#
echo "----- List all modules short introduction. -----"
curl -X GET http://localhost/isa/list
#
echo "----- Show 'demo1' module decription. -----"
## It will call '/usr/local/modules/demo1.py' and run desc() function.
curl -X GET http://localhost/isa/list/demo1
#
echo "----- Show 'demo2' module decription. -----"
## It will call '/usr/local/modules/demo2/main.py', but can not find desc() function, than exception error message.
curl -X GET http://localhost/isa/list/demo2
#
echo "----- Show 'demoX' module decription. -----"
## It will exception error message, because 'demoX' not exist.
curl -X GET http://localhost/isa/list/demoX
