## Declare alias
isa() {
  bash isa ${@}
}
## Execute script
# Create demo file
cat << EOF > /tmp/demo-conf.json
{
  "global": {
    "debug": "yes",
    "verbose": "no",
    "debugging": {
      "detailed": "no",
      "header": "debugging started"
    }
  },
  "output": {
    "file": "yes"
  },
  "employee": [1, 2, 3, 4]
}
EOF
cat << EOF > /tmp/demo-conf.yaml
## global definitions
global:
  debug: yes
  verbose: no
  debugging:
    detailed: no
    header: "debugging started"

## output
output:
   file: "yes"

## empty
employee:
  - Jacky
  - Danny
  - James
EOF
cat << EOF > /tmp/demo-conf.txt
## global definitions
global:
  debug: yes
  verbose: no
  debugging:
    detailed: no
    header: "debugging started"
EOF
#
echo "----- Write JSON file content into 'default' configuration 'demoJSONFile' module. -----"
isa conf --method post -f /tmp/demo-conf.json default demoJSONFile
isa conf --method get default demoJSONFile
echo "----- Write JSON file content into 'default' configuration 'demoYAMLFile' module. -----"
isa conf --method post -f /tmp/demo-conf.yaml default demoYAMLFile
isa conf --method get default demoYAMLFile
echo "----- Write Text file content into 'default' configuration 'demoTEXTFile' module. It will error because text is not valid format.-----"
isa conf --method post -f /tmp/demo-conf.txt default demoTEXTFile
