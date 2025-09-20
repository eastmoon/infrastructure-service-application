## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
#
echo "----- Write 'test_instance_status' configuration 'case1' module. -----"
isa conf --method post -i test_instance_status case1 << EOF
{
  'module': 'test_instance_status'
}
EOF
#
echo "----- Write 'test_instance_status' configuration 'case2' module. -----"
isa conf --method post -i test_instance_status case2 << EOF
{
  'module': 'test_instance_status'
}
EOF
#
isa conf --method get test_instance_status
isa exec test_instance_status
