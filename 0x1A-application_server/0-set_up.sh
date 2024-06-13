#!/bin/bash

# Update package list and install python3, pip3, and net-tools
sudo apt update
sudo apt install -y python3 python3-pip net-tools

# Install Flask using pip3
pip3 install Flask

#clone the repository
git clone https://github.com/origotdaskill/AirBnB_clone_v2.git

# Navigate to the cloned repository
cd ~/AirBnB_clone_v2

# Run the Flask application
python3 -m web_flask.0-hello_route
