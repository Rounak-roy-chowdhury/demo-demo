import os

#Run the following command to install Tekton Pipelines and its dependencies:
cmd1 = 'kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml'
os.system(cmd1)

#Below commands are for installing and pluging in tekton cli into kubectl
cmd2 = 'curl -LO https://github.com/tektoncd/cli/releases/download/v0.21.0/tkn_0.21.0_Linux_x86_64.tar.gz'
os.system(cmd2)
cmd3 = 'sudo tar xvzf tkn_0.21.0_Linux_x86_64.tar.gz -C /usr/local/bin/ tkn'
os.system(cmd3)
cmd4 = 'ln -s /usr/local/bin/tkn /usr/local/bin/kubectl-tkn'
os.system(cmd4)
cmd5 = 'kubectl plugin list'
os.system(cmd5)

