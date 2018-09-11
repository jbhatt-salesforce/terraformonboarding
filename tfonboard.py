#A python3 script to onboard to terraform state management envinronment on top of aws

#Step 1: create a staging directory to run this script in
import argparse
import os
import sys
import shutil

#Step 2: Setup a Dockerfile
#command line argument to gather the terraform github account sshkey.
parser = argparse.ArgumentParser()
parser.add_argument("sshkeypath", help='Path to the ssh key file for the terraform service account e.g. /Users/username/.ssh/id_rsa', type=str)
args = parser.parse_args()
src_private = os.path.expanduser(args.sshkeypath)
src_public = src_private + ".pub"
dst_privatekey = os.getcwd() + "/id_rsa"
dst_publickey = os.getcwd() + "/id_rsa.pub"

#copy the private and public keys from the args.sshkeypath to the current directory
if os.path.exists(src_private):
    print ("Copying private and public key from " + src_private + " to " + dst_privatekey)
    shutil.copy(src_private, dst_privatekey)
    shutil.copy(src_public, dst_publickey)

#Make sure that the Dockerfile exists
if os.path.isfile("Dockerfile"):
    print ("Found the Dockerfile...")
else:
   print ("Either the Dockerfile is missing or not readable")
#create a directory called terraform 
if not os.path.exists("./terraform"):
   print ("Creating terraform directory...")
   os.makedirs("terraform")
else:
   print ("Could not create terraform directory")
#copy main.tf to the terrform directory
if os.path.isfile("main.tf"):
    print ("Copying main.tf file to the terraform directory")
    shutil.copy("main.tf", "terraform/main.tf")
else:
    print ("Could not find main.tf file")

