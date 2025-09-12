## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
echo "----- Check and list infrastructure environment status. -----"
isa infra
#
echo "----- Show all infrastructure container information. -----"
isa infra ps
#
echo "----- Show all infrastructure container resource usage statistics. -----"
isa infra stats
#
echo "----- Stop all infrastructure container, but not include isa manager service. -----"
isa infra stop
#
echo "----- Start all infrastructure container. -----"
isa infra start
#
echo "----- Restart 'Nginx' infrastructure container. -----"
isa infra restart nginx
