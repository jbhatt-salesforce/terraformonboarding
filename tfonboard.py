#A python3 script to onboard to terraform state management envinronment on top of aws

#Step 1: create a staging directory to run this script in
import argparse
import os
import sys
import shutil

#Step 2: Setup a Dockerfile
#command line argument to gather the terraform github account sshkey and pgp key.
parser = argparse.ArgumentParser()
parser.add_argument("sshkeypath", help='Path to the ssh key file for the terraform service account e.g. /Users/username/.ssh/id_rsa', type=str)
parser.add_argument("--pgpkeypath", help='Path to the base64 encoded *binary* PGP key.', type=str)
parser.add_argument("--keybaseuname", help='Keybase username', type=str)
parser.add_argument("teamname", help='Your team name', type=str)

#If neither of the two optional args, pgpkeypath or keybaseuname is provided, exit the program
args = parser.parse_args()
if not (args.pgpkeypath or args.keybaseuname):
    print ("Must provide either pgpkeypath or keybaseuname. Try -h for more info.")
    sys.exit(0)

#expand the path if needed
src_privatekey = os.path.expanduser(args.sshkeypath)
src_publickey = src_privatekey + ".pub"
dst_privatekey = os.getcwd() + "/id_rsa"
dst_publickey = os.getcwd() + "/id_rsa.pub"

#copy the private and public keys from the args.sshkeypath to the current directory
if os.path.exists(src_privatekey):
    print ("Copying private and public key from " + src_privatekey + " to " + dst_privatekey)
    shutil.copy(src_privatekey, dst_privatekey)
    shutil.copy(src_publickey, dst_publickey)
    with open(dst_publickey, 'r') as pubsshkeyfile:
       pubsshkeydata=pubsshkeyfile.read().replace('\n', '')
       print ("Your public ssh key is: " + pubsshkeydata + "\n")

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

#copy pgp key file to the current folder
if args.pgpkeypath:
   src_pgpkey = os.path.expanduser(args.pgpkeypath)
   dst_pgpkey = os.getcwd()+'/pgpkey.asc'
   if os.path.exists(src_pgpkey):
      #print("Copying pgpkey from " + src_pgpkey + " to " + dst_pgpkey)
      #shutil.copy(src_pgpkey, dst_pgpkey)
      with open(src_pgpkey, 'r') as pgpfile:
         pgpkeydata=pgpfile.read().replace('\n', '')
         print("Your pgp key: " + pgpkeydata + "\n")

#if keybase is provided load that into a variable
if args.keybaseuname:
    print ("Your keybase username is: " + args.keybaseuname) 
    keybase_username = args.keybaseuname

#open and read main.tf template
#with open("main.tf", 'rw') as maintffile:
    
