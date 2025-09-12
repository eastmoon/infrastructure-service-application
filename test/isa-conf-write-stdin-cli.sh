## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
echo "----- Write array with 'echo' STDIN into 'default' configuration 'demo' module. -----"
echo "['echo','essage']" | isa conf --method post -i default demo
isa conf --method get
#
echo "----- Write key-value object with 'echo' STDIN into 'demo' configuration 'demo' module. -----"
echo "{'echo': 'essage'}" | isa conf --method post -i demo demo
isa conf --method get demo
#
echo "----- Write multi-line key-value object with EOF STDIN into 'default' configuration 'demoEOF' module. -----"
isa conf --method post -i default demoEOF << EOF
{
  'eof': 'string',
  'hello': 'world'
}
EOF
isa conf --method get
#
echo "----- Write multi-line array object with EOF STDIN into 'demo' configuration 'demoEOF' module. -----"
isa conf --method post -i demo demoEOF << EOF
[
  {'key': 'value'},
  {'hello': world}
]
EOF
isa conf --method get demo
