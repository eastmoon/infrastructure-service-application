## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
echo "----- Write array with 'echo' STDIN into 'default' configuration 'legacy' module. -----"
echo "['it','will', 'remove']" | isa conf --method post -i default legacy
isa conf --method get default legacy
#
echo "----- Delet 'default' configuration 'legacy' module. -----"
isa conf --method del default legacy
isa conf --method get default legacy
