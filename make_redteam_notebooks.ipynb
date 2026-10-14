#!/usr/bin/env python3
"""
make_redteam_notebooks.py
Rebuilds the full Colab red-team notebook suite from scratch.
Cells are reproduced verbatim. Run in Colab (auto-downloads zip) or locally.
"""
import json, os, sys, zipfile, pathlib, shutil

OUT = pathlib.Path("colab_redteam_notebooks")
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

# ---------- helpers ----------
def _src(text):
    text = text.strip("\n")
    lines = text.split("\n")
    return [l + "\n" for l in lines[:-1]] + [lines[-1]]

def code(text):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": _src(text)}

def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": _src(text)}

def write_nb(name, cells):
    nb = {
        "nbformat": 4,
        "nbformat_minor": 0,
        "metadata": {
            "colab": {"provenance": [], "toc_visible": True},
            "kernelspec": {"name": "python3", "display_name": "Python 3"},
            "language_info": {"name": "python"},
        },
        "cells": cells,
    }
    (OUT / name).write_text(json.dumps(nb, indent=1))
    return len(cells)

# ============================================================
# BASE — prepended to EVERY notebook
# ============================================================
BASE = [
md("# 🧱 BASE (shared setup) — run these first, in order"),

code(r"""# Which GPU did you actually get? Decide the model from this.
!nvidia-smi
import torch, psutil
p = torch.cuda.get_device_properties(0)
print(f"GPU: {p.name} | VRAM {p.total_memory/1e9:.1f} GB | RAM {psutil.virtual_memory().total/1e9:.1f} GB")
!df -h /content | tail -1"""),

code(r"""from google.colab import drive
drive.mount('/content/drive')
import os
CACHE = '/content/drive/MyDrive/redteam'
os.makedirs(CACHE, exist_ok=True)
print("cache:", CACHE)"""),

code(r"""%%bash
apt-get -qq update
apt-get -qq install -y docker.io git curl wget jq unzip tmux nodejs npm python3-venv python3-pip net-tools iputils-ping dnsutils
# Colab blocks Docker's iptables hooks -> disable them
dockerd --iptables=false --ip6tables=false --bridge=none >/var/log/dockerd.log 2>&1 &
for i in $(seq 1 30); do docker info >/dev/null 2>&1 && break; sleep 2; done
docker info | grep -E "Server Version|Storage Driver"
echo "docker ready" """),

code(r"""%%bash
curl -fsSL https://ollama.com/install.sh | sh || true
command -v ollama || { curl -L https://ollama.com/download/ollama-linux-amd64.tgz | tar -xz -C /usr; }
nohup ollama serve >/var/log/ollama.log 2>&1 &
for i in $(seq 1 40); do curl -s localhost:11434/api/version >/dev/null && break; sleep 2; done
curl -s localhost:11434/api/version && echo " <- ollama up" """),

code(r"""%%bash
# ---- pick ONE, uncomment ----
# 24 GB L4 (likely your card) — best agent brain for the size
ollama pull hf.co/bartowski/Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF:Q4_K_M
# 16 GB T4:
# ollama pull gpt-oss:20b
# 40 GB A100:
# ollama pull hf.co/bartowski/Llama-3.3-70B-Instruct-abliterated-GGUF:Q4_K_M
# 80-96 GB H100 / G4:
# ollama pull hf.co/bartowski/gpt-oss-120b-GGUF:MXFP4
ollama list"""),

code(r"""%%bash
# HexStrike = 150+ tools behind one MCP endpoint
git clone --depth 1 https://github.com/0x4m4/hexstrike-ai /content/hexstrike
cd /content/hexstrike
[ -f install.sh ] && bash install.sh >/var/log/hexstrike_install.log 2>&1 || true
python3 -m venv .venv && .venv/bin/pip -q install -r requirements.txt
nohup .venv/bin/python hexstrike_server.py --port 8888 >/var/log/hexstrike.log 2>&1 &
for i in $(seq 1 60); do curl -sf localhost:8888/health >/dev/null && break; sleep 3; done
echo "hexstrike:"; curl -s localhost:8888/health; echo

# Kali toolbox container the agent can shell into
docker pull -q kalilinux/kali-rolling
docker run -d --name redteam --network host kalilinux/kali-rolling sleep infinity
docker exec redteam bash -lc 'apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -qq install -y kali-tools-top10 metasploit-framework >/dev/null 2>&1; echo toolbox-ready' """),

code(r"""%%bash
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O /usr/local/bin/cloudflared
chmod +x /usr/local/bin/cloudflared
nohup cloudflared tunnel --url http://localhost:8888 >/var/log/cf.log 2>&1 &
sleep 15
echo "HexStrike URL:"; grep -o 'https://[a-z0-9-]*\.trycloudflare\.com' /var/log/cf.log | head -1"""),
]

# ============================================================
# NOTEBOOK 01 — Web Application Offensive
# ============================================================
NB01 = [
md("# 📓 Notebook 01 — Web Application Offensive\n\nSQLi, XSS, SSRF, IDOR, JWT, auth bypass, LFI/RFI, deserialization, API abuse.\nTargets: Juice Shop, DVWA, WebGoat, bWAPP, crAPI, VAmPI."),

code(r"""%%bash
# --- install Go for ProjectDiscovery tooling ---
if ! command -v go >/dev/null; then
  curl -fsSL https://go.dev/dl/go1.23.5.linux-amd64.tar.gz -o /tmp/go.tgz
  rm -rf /usr/local/go && tar -C /usr/local -xzf /tmp/go.tgz
  echo 'export PATH=$PATH:/usr/local/go/bin' >> /etc/profile.d/go.sh
fi
export PATH=$PATH:/usr/local/go/bin
go version"""),

code(r"""%%bash
export PATH=$PATH:/usr/local/go/bin:/root/go/bin
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/ffuf/ffuf/v2@latest
go install -v github.com/hahwul/dalfox/v2@latest
/root/go/bin/nuclei -update-templates -silent"""),

code(r"""%%bash
apt-get -qq install -y sqlmap nikto whatweb wafw00f gobuster feroxbuster
pip -q install arjun commix 2>/dev/null || true
git clone --depth 1 https://github.com/ticarpi/jwt_tool /content/jwt_tool
git clone --depth 1 https://github.com/s0md3v/Arjun /content/arjun 2>/dev/null || true
docker pull -q zaproxy/zap-stable
docker run -d --name zap --network host zaproxy/zap-stable zap.sh -daemon -host 0.0.0.0 -port 8090 -config api.disablekey=true
echo "tools ready" """),

code(r"""%%bash
# --- spin the labs (all --network host, distinct ports) ---
docker run -d --name juice   --network host bkimminich/juice-shop
docker run -d --name dvwa    --network host vulnerables/web-dvwa
docker run -d --name webgoat --network host webgoat/webgoat
docker run -d --name bwap    --network host raesene/bwapp
docker run -d --name vampi   --network host erev0s/vampi
sleep 30
for p in 3000 80 8080; do curl -s -o /dev/null -w "port $p -> %{http_code}\n" http://localhost:$p; done"""),

code(r"""# --- one-shot recon sweep the agent can riff on ---
target = "http://localhost:3000"   # Juice Shop
!httpx -u {target} -title -tech-detect -status-code -silent
!whatweb {target}
!wafw00f {target}
!nuclei -u {target} -severity low,medium,high,critical -silent | head -40"""),
]

# ============================================================
# NOTEBOOK 02 — Network, Infra & Active Directory
# ============================================================
NB02 = [
md("# 📓 Notebook 02 — Network, Infra & Active Directory\n\nHost discovery, service enum, SMB/NetBIOS, credential attacks, lateral movement, exploit delivery."),

code(r"""%%bash
apt-get -qq install -y nmap masscan arp-scan hydra john hashcat enum4linux-ng smbmap nbtscan whois
pip -q install netexec 2>/dev/null || pip -q install crackmapexec
pip -q install impacket
docker pull -q tleemcjr/metasploitable2
git clone --depth 1 https://github.com/vulhub/vulhub /content/vulhub
echo "net tools ready" """),

code(r"""%%bash
# --- targets ---
docker run -d --name metasploitable2 --network host tleemcjr/metasploitable2
# SMB share host
docker run -d --name smb --network host dperson/samba -p -u "user;pass" -s "share;/tmp;yes;no;no;user"
# vulnerable FTP (vsftpd 2.3.4 backdoor)
docker run -d --name ftp --network host fauria/vsftpd
sleep 20
nmap -sV -T4 localhost -p 21,22,23,80,139,445,3306,5432,8080 | tail -30"""),

code(r"""%%bash
# --- local exploit framework ---
docker exec redteam bash -lc 'msfconsole -q -x "version; exit"' | head -5
docker exec redteam bash -lc 'which nmap sqlmap hydra netexec responder' 2>/dev/null || true"""),

code(r"""# --- example agent tasks ---
!nmap -sV -sC -p- -T4 localhost | tee /content/nmap_full.txt | tail -40
!enum4linux-ng -A localhost || true
!smbmap -H localhost -u user -p pass || true
!hydra -l user -P /usr/share/wordlists/rockyou.txt ssh://localhost -t 4 -f || true"""),
]

# ============================================================
# NOTEBOOK 03 — Mobile
# ============================================================
NB03 = [
md("# 📓 Notebook 03 — Mobile (Android / iOS)\n\nStatic APK analysis, hardcoded secrets, root/SSL-pinning bypass, exported components, dynamic instrumentation."),

code(r"""%%bash
apt-get -qq install -y default-jdk android-tools-adb apktool aapt unzip
pip -q install frida-tools objection apkleaks 2>/dev/null || true
# jadx
JADX=1.5.0
wget -q https://github.com/skylot/jadx/releases/download/v${JADX}/jadx-${JADX}.zip -O /tmp/jadx.zip
unzip -q -o /tmp/jadx.zip -d /opt/jadx && ln -sf /opt/jadx/bin/jadx /usr/local/bin/jadx
# MobSF (web UI on :8000)
docker pull -q opensecurity/mobile-security-framework-mobsf
echo "mobile tools ready" """),

code(r"""%%bash
mkdir -p /content/apks && cd /content/apks
git clone --depth 1 https://github.com/payatu/diva-android .
git clone --depth 1 https://github.com/satishpatnayak/AndroGoat AndroGoat 2>/dev/null || true
find /content/apks -name "*.apk" | head"""),

code(r"""%%bash
docker run -d --name mobsf --network host opensecurity/mobile-security-framework-mobsf
sleep 25
echo "MobSF -> http://localhost:8000  (user: mobsf / pass: mobsf)"
curl -s -o /dev/null -w "mobsf:%{http_code}\n" http://localhost:8000"""),

code(r"""# --- static analysis without a device ---
apk = "/content/apks/diva-beta.apk"     # adjust to whatever you cloned
!jadx -d /content/diva_src {apk}
!apktool d -f -o /content/diva_apktool {apk}
!grep -rEi "api[_-]?key|secret|password|token" /content/diva_src | head -20
!strings {apk} | grep -Ei "http|firebase|amazonaws" | sort -u | head"""),

code(r"""%%bash
# on the VM
nohup frida-server >/dev/null 2>&1 &   # or push frida-server to device
echo "adb devices"; adb devices || true
echo "frida-ps -U"; frida-ps -U 2>/dev/null | head || true"""),
]

# ============================================================
# NOTEBOOK 04 — Databases
# ============================================================
NB04 = [
md("# 📓 Notebook 04 — Databases\n\nSQLi beyond sqlmap defaults, NoSQL injection, unauthenticated Redis/Mongo, MSSQL xp_cmdshell, credential cracking."),

code(r"""%%bash
apt-get -qq install -y mysql-client postgresql-client redis-tools
pip -q install pymongo pymysql psycopg2-binary redis sqlmap
git clone --depth 1 https://github.com/codingo/NoSQLMap /content/nosqlmap
git clone --depth 1 https://github.com/quentinhardy/odat /content/odat
echo "db tools ready" """),

code(r"""%%bash
# --- vulnerable-by-config targets ---
docker run -d --name mysql --network host -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=vuln mysql:8
docker run -d --name pgsql --network host -e POSTGRES_PASSWORD=postgres postgres:16
docker run -d --name mongo --network host mongo:7
docker run -d --name redis --network host redis:7
# MSSQL (SA / weak pw)
docker run -d --name mssql --network host -e ACCEPT_EULA=Y -e MSSQL_SA_PASSWORD='Password123!' mcr.microsoft.com/mssql/server:2022-latest
sleep 45
nmap -sV localhost -p 3306,5432,27017,6379,1433 | tail -20"""),

code(r"""# --- example attacks ---
!redis-cli -h localhost INFO server | head
!redis-cli -h localhost CONFIG GET dir
!mysql -h 127.0.0.1 -uroot -proot -e "SELECT version();" vuln
!sqlmap -u "http://localhost:3000/rest/products/search?q=1" --batch --level=3 --risk=2 --dbs"""),
]

# ============================================================
# NOTEBOOK 05 — Cloud, Container & Kubernetes
# ============================================================
NB05 = [
md("# 📓 Notebook 05 — Cloud, Container & Kubernetes\n\nContainer escape checks, image CVEs, IaC misconfig, secret scanning, K8s RBAC abuse, CI/CD secret theft."),

code(r"""%%bash
apt-get -qq install -y kubectl
pip -q install checkov prowler detect-secrets
# trivy
wget -q https://github.com/aquasecurity/trivy/releases/latest/download/trivy_0.58.0_Linux-64bit.tar.gz -O /tmp/t.tgz
tar -xzf /tmp/t.tgz -C /usr/local/bin trivy
# kube-hunter + kube-bench + secret scanners
pip -q install kube-hunter
wget -q https://github.com/aquasecurity/kube-bench/releases/latest/download/kube-bench_0.10.5_linux_amd64.tar.gz -O /tmp/kb.tgz && tar -xzf /tmp/kb.tgz -C /usr/local/bin kube-bench || true
wget -q https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks_8.21.2_linux_x64.tar.gz -O /tmp/gl.tgz && tar -xzf /tmp/gl.tgz -C /usr/local/bin gitleaks || true
echo "cloud tools ready" """),

code(r"""%%bash
# --- local k8s (k3s, no systemd) ---
curl -sfL https://get.k3s.io | INSTALL_K3S_SKIP_START=true sh - 2>/dev/null || true
nohup k3s server --disable traefik >/var/log/k3s.log 2>&1 &
sleep 45
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
kubectl get nodes 2>&1 | head"""),

code(r"""%%bash
# --- targets ---
docker run -d --name wrongsecrets --network host jeroenwillemsen/wrongsecrets
docker run -d --name vulnerable-nginx --network host nginxdemos/hello
sleep 15
echo "wrongsecrets -> http://localhost:8080"
curl -s -o /dev/null -w "wrongsecrets:%{http_code}\n" http://localhost:8080"""),

code(r"""# --- example attacks ---
!trivy image --severity HIGH,CRITICAL bkimminich/juice-shop | head -40
!trivy fs --scanners vuln,secret,misconfig /content/hexstrike | head -30
!kube-bench run --targets node 2>/dev/null | head -30 || true
!gitleaks detect -s /content -v 2>/dev/null | head -20"""),

code(r"""%%bash
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
curl -fsSL https://raw.githubusercontent.com/kubernetes-goat/kubernetes-goat/master/deploy-k8s.sh | bash 2>/dev/null | tail -20 || true
kubectl get pods -A 2>/dev/null | head -30"""),
]

# ============================================================
# NOTEBOOK 06 — Operator Console
# ============================================================
NB06 = [
md("# 📓 Notebook 06 — Operator Console\n\nLocal abliterated model + MCP tool bridge + CLI agent + tunnel. The brain that drives the other notebooks."),

code(r"""%%bash
# --- free agent CLI (pick one; all MIT/Apache) ---
curl -fsSL https://opencode.ai/install | bash || npm i -g opencode-ai
# alternatives:
# npm i -g @charmland/crush
# curl -fsSL https://block.github.io/goose/install.sh | bash
# npm i -g @google/gemini-cli   # covered by your Google AI Pro plan
opencode --version 2>/dev/null || echo "installed" """),

code(r"""%%bash
# --- MCP servers beyond HexStrike ---
pip -q install mcp
git clone --depth 1 https://github.com/Eutectico/mcp-kali-server /content/mcp-kali 2>/dev/null || true
git clone --depth 1 https://github.com/sudohakan/kali-mcp-server /content/kali-mcp 2>/dev/null || true
echo "mcp servers cloned" """),

code(r"""%%bash
# --- hexstrike MCP frontend (stdio bridge) ---
ls /content/hexstrike/hexstrike_mcp.py && echo "mcp bridge present" """),

code(r"""{
  "provider": {
    "local": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "http://localhost:11434/v1", "apiKey": "ollama" },
      "models": { "qwen3-coder-abl": { "name": "Qwen3-Coder-30B abliterated" } }
    }
  },
  "mcp": {
    "hexstrike": {
      "type": "local",
      "command": ["python3", "/content/hexstrike/hexstrike_mcp.py", "--server", "http://localhost:8888"]
    },
    "kali": {
      "type": "local",
      "command": ["python3", "/content/mcp-kali/server.py"]
    },
    "colab": {
      "type": "local",
      "command": ["uvx", "git+https://github.com/googlecolab/colab-mcp"]
    }
  }
}"""),

code(r"""# on your laptop
uv tool install google-colab-cli
colab ssh            # proxies 8888 (hexstrike) + 11434 (model) to localhost
# OR use the cloudflared URL printed in BASE/Cell 6"""),
]

# ============================================================
# BUILD
# ============================================================
NOTEBOOKS = {
    "01_web_app_offensive.ipynb":   NB01,
    "02_network_infra_ad.ipynb":    NB02,
    "03_mobile.ipynb":              NB03,
    "04_databases.ipynb":           NB04,
    "05_cloud_container_k8s.ipynb": NB05,
    "06_operator_console.ipynb":    NB06,
}

manifest = []
for fname, extra in NOTEBOOKS.items():
    cells = extra[:1] + BASE + extra[1:]   # title, then BASE, then domain cells
    n = write_nb(fname, cells)
    manifest.append((fname, n))

# standalone BASE reference notebook
write_nb("00_BASE_reference.ipynb", BASE)

print("=" * 60)
print(f"Wrote {len(NOTEBOOKS) + 1} notebooks to ./{OUT}/")
for fname, n in manifest:
    print(f"  {fname:34s} {n:3d} cells (incl. {len(BASE)} shared BASE cells)")
print("=" * 60)

# ---------- zip ----------
zip_path = "colab_redteam_notebooks.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(OUT.glob("*.ipynb")):
        z.write(f, f.name)
print(f"zip: {os.path.abspath(zip_path)}")

# ---------- auto-download if in Colab ----------
try:
    import google.colab  # noqa
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

if IN_COLAB:
    from google.colab import files
    files.download(zip_path)
