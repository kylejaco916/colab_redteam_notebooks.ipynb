# 📓 Google Colab Notebook Master Library

A curated, comprehensive suite of all Google Colab notebooks developed, verified, and operationalized across all projects for **Kyle Jaco (`kylejaco916`)**.

---

## ⚡ Notebook Catalog

| # | Notebook | Project / Domain | Recommended GPU | Open in Colab Badge |
|---|---|---|---|---|
| **00** | `00_BASE_reference.ipynb` | Shared Base Infrastructure (GPU detection, Docker, Kali, HexStrike, Ollama) | T4 / L4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/00_BASE_reference.ipynb) |
| **01** | `01_web_app_offensive.ipynb` | Web Application Security (Burp, SQLMap, Nuclei, Nikto, Feroxbuster) | T4 / L4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/01_web_app_offensive.ipynb) |
| **02** | `02_network_infra_ad.ipynb` | Network, Infra & Active Directory (CrackMapExec, Responder, Impacket, BloodHound) | T4 / L4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/02_network_infra_ad.ipynb) |
| **03** | `03_mobile.ipynb` | Mobile Pentesting (Android APK decompilation, Frida, objection, MobSF) | T4 / L4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/03_mobile.ipynb) |
| **04** | `04_databases.ipynb` | Database Security & Exploitation (Postgres, MySQL, Redis, MongoDB auditing) | T4 / L4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/04_databases.ipynb) |
| **05** | `05_cloud_container_k8s.ipynb` | Cloud, Docker & Kubernetes (Kube-hunter, ScoutSuite, Trivy, Docker breakout) | T4 / L4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/05_cloud_container_k8s.ipynb) |
| **06** | `06_operator_console.ipynb` | Operator Console & Multi-Agent (Operator Dashboard, C2, AI Automation) | T4 / L4 / A100 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/06_operator_console.ipynb) |
| **07** | `make_redteam_notebooks.ipynb` | Red Team Suite Verbatim Builder | Any (CPU) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/make_redteam_notebooks.ipynb) |
| **08** | `ai_stack_deployment.ipynb` | Flagship AI Stack: Qwen3.8 Abliterated / WhiteRabbitNeo + ComfyUI | T4 / A100 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/ai_stack_deployment.ipynb) |
| **09** | `ComfyUI_SDXL_Colab_Setup.ipynb` | ComfyUI + SDXL Photorealism + Realistic LoRAs + OpenPose | T4 / A100 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/ComfyUI_SDXL_Colab_Setup.ipynb) |
| **10** | `Antigravity_Colab_Worker.ipynb` | Antigravity Cloud Bridge (Termux ↔ Colab VM Cloud Worker) | T4 / L4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/Antigravity_Colab_Worker.ipynb) |
| **11** | `comfyui_colab_with_manager.ipynb` | ComfyUI Studio with ComfyUI-Manager Preinstalled | T4 / A100 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/comfyui_colab_with_manager.ipynb) |
| **⭐** | `Colab_Master_Library_Synchronizer.ipynb` | **Master Hub: 1-Click Drive Sync, GitHub Push & Zip Export** | Any (CPU) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kylejaco916/colab_redteam_notebooks.ipynb/blob/main/Colab_Master_Library_Synchronizer.ipynb) |

---

## 🛠️ How to Access & Sync to Your Colab Library in Browser

### Method 1: Master Synchronizer (1-Click Permanent Google Drive Sync)
1. Open Google Colab: [https://colab.research.google.com](https://colab.research.google.com)
2. Click **File -> Upload notebook** -> upload `Colab_Master_Library_Synchronizer.ipynb` (from `Download/colab_notebook_library/` on your phone).
3. Run **Cell 1**: Click **Connect to Google Drive**.
4. That's it! All 12 notebooks are permanently saved into your Google Drive `Colab Notebooks` library and will always appear in your Colab browser library under "Recent" and "Google Drive".

### Method 2: Push to GitHub & Browse in Colab
1. Run `upload-notebooks-github <YOUR_GITHUB_TOKEN>` from Termux, or run **Cell 2** inside `Colab_Master_Library_Synchronizer.ipynb`.
2. Open Google Colab: [https://colab.research.google.com](https://colab.research.google.com)
3. Click **File -> Open notebook** -> select the **GitHub** tab.
4. Type `kylejaco916` -> select `colab_redteam_notebooks.ipynb`.
5. Every single notebook appears with 1-click browser access.

### Method 3: Direct Android Phone Upload
All notebooks are stored directly in your phone's accessible download folder:
- Folder: `/sdcard/Download/colab_notebook_library/`
- Zip Archive: `/sdcard/Download/colab_notebook_library.zip`
In Colab in Chrome: Click **File -> Upload notebook**, tap **Browse**, and pick any notebook instantly.

---

## 📂 Storage Locations on Device
- **Termux Master Copy:** `~/colab_notebook_library/`
- **Phone Downloads Folder:** `/sdcard/Download/colab_notebook_library/`
- **Zip Archive:** `/sdcard/Download/colab_notebook_library.zip`
- **Sync Command:** `upload-notebooks-github [PAT]`
