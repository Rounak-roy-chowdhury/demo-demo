import os
os.system("mkdir build_push_files")

#cloning the repo where all the yaml files of tekton task, which will clone a git repo build its docker image and push it to dockerhub, are pre-uploaded 

cmd1 = ('git clone https://github.com/Rounak-roy-chowdhury/tekton_build_push.git build_push_files')
os.system(cmd1)
cmd2 = ('kubectl apply -f build_push_files')
os.system(cmd2)

