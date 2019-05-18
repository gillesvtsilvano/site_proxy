# Comandos para instalacao do Shiny Server

sudo apt update
sudo apt install r-base
sudo su - -c "R -e \"install.package('shiny', repos='https://cran.rstudio.com/')\""
sudo apt install gdebi-core
wget wget https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-1.5.9.923-amd64.deb
sudo gdebi shiny-server-1.5.9.923-adm64.deb

