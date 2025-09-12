## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
echo "----- List all configuration file. -----"
isa conf --method list
#
echo "----- Show 'defualt' configuration file all content. -----"
## If configuration not exist, it will show '{}'.
isa conf --method get
#
echo "----- Show 'demo' configuration file all content. -----"
## If configuration not exist, it will show '{}'.
isa conf --method get demo
#
echo "----- Show 'defualt' configuration file 'demo' module tag. -----"
## If 'demo' module tag not exist, it will exception error message.
isa conf --method get default demo
