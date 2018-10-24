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

#ou pode ser da seguinte forma:

#Apos criar o arquivo de configuração e definir a senha:

cd. jupyter #entra na pasta que possui o arquivo de configuração

nano jupyter_notebook_config.py

#adicionar essas linhas

c.NotebookApp.port = 10111
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
