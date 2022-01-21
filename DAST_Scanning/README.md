
## CLOSETSERVER - DAST AUTOMATION



### OBJECTIVE

This documentation provides a step-by-step guidance as to how to build a docker image from the provided Dockerfile and run the required DAST scan on the desired target with the help of a yaml config file.
	
	
	
### BUILDING THE DOCKER IMAGE
	
1. Through the CLI, navigate into the directory which contains the Dockerfile.

2. Using the `cat Dockerfile` command, check the contents of the file. Ensure that the Dockerfile uses the correct path to *superscript.py*.

3. Execute the following command to build a docker image from the provided Dockerfile: `sudo docker build -t imagename:imagetag .`
   
   For example, *imagename:imagetag* could be *closetserverimage:v2.0*
   
   Since you are inside the directory containing the required Dockerfile, use `.` in the command as it points to the current path for the Dockerfile.
	   
4. The docker image will be successfully built and tagged.


### YAML CONFIG FILE

To run the required DAST scan, a yaml config file is necessary. The file should contain the following keys;

* typeofscan - it specifies the type of DAST scanning required on a particular target, and can be either *baseline*, *full* or *api*
* target - it is the target URL or API definition on which the DAST scanning would take place
* format(only for api scan) - it indicates the format of API, such as *openapi*, *soap* or *graphql*
* options - any optional parameters which the user would want to specify

Below are the contents of the yaml config file *api.yaml* used here as an example;

`typeofscan: "api"`

`target: "https://www.example.com/graphql"`

`format: "graphql"`

`options: ""`


### EXECUTING THE DAST SCAN

The required DAST scan can be run on the desired target with the help of the yaml config file through the following command on the CLI:
`sudo docker run -v ~/Desktop/zaproxy/docker/csidast:/tmp/csi -t closetserverimage:v1.3 python closetserver/superscript.py -c /tmp/csi/config.yaml`

The components of the command are explained below;

`-v ~/Desktop/zaproxy/docker/csidast:/tmp/csi` - Mounting the directory containing the yaml config file*

`-t closetserverimage:v1.3` - Docker image built previously being used for the DAST scan*

`python closetserver/superscript.py` - Python script "superscript.py" residing within closetserver/ of the image, which would initiate the DAST scan

`-c /tmp/csi/config.yaml` - Specifying the path of the required yaml config file within the mounted directory*

> *user should make changes accordingly

*Note: closetserverimage:v1.3 is the current usable docker image*
