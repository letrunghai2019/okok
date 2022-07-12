<div align=center>
 
# 🚀 NaSaKi: V1.0 🚀

</p>
 
# Info
- [x] Open Source
- [x] Powerful
- [x] Simple
- [x] Methods for Layer 4 and 7
- [x] Bypass (Cloudflare, OVH, NFO,...)  


# Setup

git clone https://github.com/hoaan1995/ZxCDDoS/
cd ZxCDDoS/
npm i requests
npm i https-proxy-agent
npm i crypto-random-string
npm i events
npm i fs
npm i net
npm i cloudscraper
npm i request
npm i hcaptcha-solver
npm i randomstring
npm i cluster
npm i cloudflare-bypasser
pip3 install -r requirements.txt
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install ./google-chrome-stable_current_amd64.deb
iptables -t mangle -A PREROUTING -s 243.45.216.58-j DROP
iptables -A INPUT -p udp -m length --length 49 -j DROP
iptables -A INPUT -p udp -i eth0 ! -s 0.0.0.0/0 --dport 39356 -j DROP
iptables -A OUTPUT -p udp --dport 5353 -j DROP
ulimit -n 999999
chmod 777 *
python3 c2.py
```