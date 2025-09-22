## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
#
echo "----- Write 'test_instance_status' configuration 'case1' module. -----"
isa conf --method post -i test_module case1 << EOF
{
  'module': 'simple_module',
  'value': 5678
}
EOF
#
echo "----- Write 'test_instance_status' configuration 'case2' module. -----"
isa conf --method post -i test_module case2 << EOF
{
  'module': 'simple_module',
  'value': 1234
}
EOF
#
isa conf --method get test_module
isa exec test_module
