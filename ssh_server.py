# ssh
#Create
jupyter notebook --generate-config

#change
jupyter notebook password
Enter password: ****
Verify password: ****

server@server$ source activate phy
server@server$ jupyter notebook --no-browser --port=8889 

client@client$ ssh -N -f -L localhost:8000:localhost:8889 user@IPSERVER
client@client$ firefox http://localhost:8000
