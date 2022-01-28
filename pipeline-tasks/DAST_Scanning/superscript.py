import os
import getopt
import os.path 
import sys
import yaml
	
def yamlconfigfile():

	config_file = ''
	
	argv = sys.argv[1:]
	
	try:
		opts, args = getopt.getopt(argv, "v:c:t:")
		
	except:
        	sys.exit("Incorrect input")
        	
	for opt, arg in opts:
		if opt in ['-c']:
        		config_file = arg
        	
	def loadyamlconfig():
        
        	with open(config_file, "r") as cf:
        	
        		config = yaml.load(cf,Loader=yaml.FullLoader) 
        		
        		if (config['typeofscan']   == 'baseline'):
        			print("Executing baseline scan")
        			baseline_commands = config['target'] + " " + config['options']
        			baseline_exec = "zap-baseline.py -t {0}".format(baseline_commands)
        			os.system(baseline_exec)
        			
        		elif (config['typeofscan']   == 'full'):
        			print("Executing full scan")
        			full_commands = config['target'] + " " + config['options']
        			full_exec = "zap-full-scan.py -t {0}".format(full_commands)
        			os.system(full_exec)
        			
        		elif (config['typeofscan']   == 'api'):
        			print("Executing api scan")
        			api_commands = config['format'] + " " + config['options']
        			api_exec = "zap-api-scan.py -t {0} -f {1}".format(config['target'],api_commands)
        			os.system(api_exec)
        			
        		else:
        			print("Invalid")
        		
	loadyamlconfig()
        
yamlconfigfile()
