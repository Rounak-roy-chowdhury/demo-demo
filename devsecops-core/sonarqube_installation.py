import os
#below commands for installing helm
cmdA =('curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3')
cmdB =('chmod 700 get_helm.sh')
cmdC =('./get_helm.sh')
os.system(cmdA)
os.system(cmdB)
os.system(cmdC)

#below commands for installing sonarqube
cmd1 = ('kubectl create namespace sonarqube')
cmd2 = ('helm repo add oteemocharts https://oteemo.github.io/charts')
cmd3 = ('helm install sonar oteemocharts/sonarqube --version 9.2.4 --namespace sonarqube --values sonarqube-values.yaml')
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
