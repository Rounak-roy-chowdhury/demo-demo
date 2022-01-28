import os

#starboard cli
os.system('sudo curl -LO  https://github.com/aquasecurity/starboard/releases/download/v0.14.1/starboard_linux_x86_64.tar.gz')
os.system('tar -zxvf starboard_linux_x86_64.tar.gz')
os.system ('sudo mv starboard /usr/local/bin/starboard')
os.system ('sudo starboard install')

#starboard operator
os.system('kubectl apply -f https://raw.githubusercontent.com/aquasecurity/starboard/v0.14.1/deploy/crd/vulnerabilityreports.crd.yaml -f https://raw.githubusercontent.com/aquasecurity/starboard/v0.14.1/deploy/crd/configauditreports.crd.yaml -f https://raw.githubusercontent.com/aquasecurity/starboard/v0.14.1/deploy/crd/clusterconfigauditreports.crd.yaml -f https://raw.githubusercontent.com/aquasecurity/starboard/v0.14.1/deploy/crd/ciskubebenchreports.crd.yaml')
os.system('kubectl apply -f https://raw.githubusercontent.com/aquasecurity/starboard/v0.14.1/deploy/static/01-starboard-operator.ns.yaml -f https://raw.githubusercontent.com/aquasecurity/starboard/v0.14.1/deploy/static/02-starboard-operator.rbac.yaml')
os.system('kubectl apply -f https://raw.githubusercontent.com/aquasecurity/starboard/v0.14.1/deploy/static/03-starboard-operator.config.yaml')
os.system('kubectl apply -f https://raw.githubusercontent.com/aquasecurity/starboard/v0.14.1/deploy/static/04-starboard-operator.deployment.yaml')

#octant
os.system('sudo curl -LO https://github.com/vmware-tanzu/octant/releases/download/v0.25.0/octant_0.25.0_Linux-64bit.deb')
os.system('sudo dpkg -i octant_0.25.0_Linux-64bit.deb')

#starboard-octant-plugin
os.system('sudo curl -LO  https://github.com/aquasecurity/starboard-octant-plugin/releases/download/v0.12.0/starboard-octant-plugin_linux_x86_64.tar.gz')
os.system('tar -zxvf starboard-octant-plugin_linux_x86_64.tar.gz')
os.mkdir('.config/octant')
os.mkdir('.config/octant/plugins')
os.system('sudo mv starboard-octant-plugin .config/octant/plugins')

