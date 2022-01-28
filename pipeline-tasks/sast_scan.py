import os
import time

#commands for exposing the cluster IP
cmd1=('export NODE_PORT=$(kubectl get --namespace sonarqube -o jsonpath="{.spec.ports[0].nodePort}" services sonar-sonarqube)')
cmd2= ('export NODE_IP=$(kubectl get nodes --namespace sonarqube -o jsonpath="{.items[0].status.addresses[0].address}")')
os.system(cmd1)
os.system(cmd2)

#command for changing the port number
cmd3 = ('kubectl patch service sonar-sonarqube -n sonarqube --type=\'json\' --patch=\'[{\"op\": \"replace\", \"path\": \"/spec/ports/0/nodePort\", \"value\":31111}]\'')
os.system(cmd3)

#time.sleep(30)

#commands to apply the tekton tasks for git clone & sonarqube scanning
os.chdir('sonarqube_sast_automation')
os.system('kubectl apply -f git-clone-task.yaml')
os.system('kubectl apply -f sonarqube-scanner-task.yaml')
os.system('kubectl apply -f sonarqube_pv.yaml')
os.system('kubectl apply -f sonarqube_pvc.yaml')
os.system('kubectl apply -f sonarqube-pipeline.yaml')
os.system('kubectl apply -f sonarqube-pipelinerun.yaml')




