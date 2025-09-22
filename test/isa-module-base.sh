## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
#
#
echo "----- Write 'test_instance_status' configuration 'case' module. -----"
isa conf --method post -i test_module_base case << EOF
{
  'module': 'base_module',
  'container': { 'name': 'nginx', 'port': 80 },
  'authorize' : 'setting target container authorize.',
  'secure' : 'setting target container secure.',
  'command' : [
      {'msg': 'Copy location file to conf.d folder.', 'cmd': 'template', 'data': { 'file': 'demo.loc', 'to': 'conf.d/demo.loc', 'keys' : {'VALUE': '`date +%s`'}}},
      {'msg': 'Restart service.', 'cmd': 'restart'},
      {'msg': 'Sleep and wait.', 'cmd': 'sleep', 'time': 1},
      {'msg': 'Call API with new location file.', 'cmd': 'api', 'data': { 'url': '/value', 'method': 'GET'}},
      {'msg': 'Call API with outside server.', 'cmd': 'api', 'data': { 'url': 'https://jsonplaceholder.typicode.com/users', 'method': 'get'}},
      {'msg': 'Call Docker exec command.', 'cmd': 'exec', 'data': 'ls -al'},
      {'msg': 'Do other function', 'cmd': 'other-command', 'data': 'do something'}
  ],
  'other' : 'setting target with module other function',
  'nomatch' : 'unknown content, can not match to any function'
}
EOF
#
isa conf --method get test_module_base
isa exec test_module_base
