## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
echo "----- Create 'execdemo1' configuration file, with 'demo1', 'demo2', 'm1', 'm2' module -----"
echo "{'exec':'demo1', 'key': 'value'}" | isa conf -m post -i execdemo1 demo1
echo "{'exec':'demo2', 'key': 'value'}" | isa conf -m post -i execdemo1 demo2
echo "{'exec':'m1', 'key': 'value'}" | isa conf -m post -i execdemo1 m1
echo "{'exec':'m2', 'key': 'value'}" | isa conf -m post -i execdemo1 m2
isa exec execdemo1
#
echo "----- Create 'execdemo2' configuration file, with 'demo1', 'demo2', 'm1', 'm2' module -----"
echo "----- But 'm1' run with 'demo1' module, 'm2' run with 'demo2' module  -----"
echo "{'module': 'demo2', 'exec':'m2', 'key': 'value'}" | isa conf -m post -i execdemo2 m2
echo "{'module': 'demo1', 'exec':'m1', 'key': 'value'}" | isa conf -m post -i execdemo2 m1
echo "{'exec':'demo2', 'key': 'value'}" | isa conf -m post -i execdemo2 demo2
echo "{'exec':'demo1', 'key': 'value'}" | isa conf -m post -i execdemo2 demo1
isa exec execdemo2
#
echo "----- Create 'execdemo3' configuration file, with 'demo1', 'demo2', 'm1', 'm2' module -----"
echo "----- But only run with order 'demo2', 'demo1'  -----"
echo "{'module': 'demo2', 'exec':'m2', 'key': 'value'}" | isa conf -m post -i execdemo3 m2
echo "{'module': 'demo1', 'exec':'m1', 'key': 'value'}" | isa conf -m post -i execdemo3 m1
echo "{'exec':'demo2', 'key': 'value'}" | isa conf -m post -i execdemo3 demo2
echo "{'exec':'demo1', 'key': 'value'}" | isa conf -m post -i execdemo3 demo1
echo "{'flow': ['demo2', 'demo1']}" | isa conf -m post -i execdemo3 global
isa exec execdemo3
