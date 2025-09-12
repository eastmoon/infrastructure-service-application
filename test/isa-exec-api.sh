## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
echo "----- Create 'execdapiemo1' configuration file, with 'demo1', 'demo2', 'm1', 'm2' module -----"
curl --silent -X POST -d "{'exec':'demo1', 'key': 'value'}" http://localhost/isa/conf/execdapiemo1/demo1
curl --silent -X POST -d "{'exec':'demo2', 'key': 'value'}" http://localhost/isa/conf/execdapiemo1/demo2
curl --silent -X POST -d "{'exec':'m1', 'key': 'value'}" http://localhost/isa/conf/execdapiemo1/m1
curl --silent -X POST -d "{'exec':'m2', 'key': 'value'}" http://localhost/isa/conf/execdapiemo1/m2
curl -X POST http://localhost/isa/exec/execdapiemo1
#
echo "----- Create 'execdapiemo2' configuration file, with 'demo1', 'demo2', 'm1', 'm2' module -----"
echo "----- But 'm1' run with 'demo1' module, 'm2' run with 'demo2' module  -----"
curl --silent -X POST -d "{'exec':'demo1', 'key': 'value'}" http://localhost/isa/conf/execdapiemo2/demo1
curl --silent -X POST -d "{'exec':'demo2', 'key': 'value'}" http://localhost/isa/conf/execdapiemo2/demo2
curl --silent -X POST -d "{'module': 'demo1', 'exec':'m2', 'key': 'value'}" http://localhost/isa/conf/execdapiemo2/m1
curl --silent -X POST -d "{'module': 'demo2', 'exec':'m2', 'key': 'value'}" http://localhost/isa/conf/execdapiemo2/m2
curl -X POST http://localhost/isa/exec/execdapiemo2
#
echo "----- Create 'execdapiemo3' configuration file, with 'demo1', 'demo2', 'm1', 'm2' module -----"
echo "----- But only run with order 'demo2', 'demo1'  -----"
curl --silent -X POST -d "{'exec':'demo1', 'key': 'value'}" http://localhost/isa/conf/execdapiemo3/demo1
curl --silent -X POST -d "{'exec':'demo2', 'key': 'value'}" http://localhost/isa/conf/execdapiemo3/demo2
curl --silent -X POST -d "{'exec':'m1', 'key': 'value'}" http://localhost/isa/conf/execdapiemo3/m1
curl --silent -X POST -d "{'exec':'m2', 'key': 'value'}" http://localhost/isa/conf/execdapiemo3/m2
curl --silent -X POST -d "{'flow': ['demo2', 'demo1']}" http://localhost/isa/conf/execdapiemo3/global
curl -X POST http://localhost/isa/exec/execdapiemo3
