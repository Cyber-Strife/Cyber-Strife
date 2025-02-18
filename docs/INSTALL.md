# Installation Guide

## Prerequisites
Before installing Cyber Strife, ensure you have the following dependencies installed:

- **Python 3.9+**
- **Node.js 16+**
- **Solidity Compiler**
- **Docker (Optional)**
- **Git**

## Installation Steps

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/cyber-strife.git
cd cyber-strife

2️⃣ Set Up Python Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Install Frontend Dependencies
cd web/frontend
npm install

4️⃣ Deploy Smart Contracts (Testnet)
cd src/contracts
npx hardhat compile
npx hardhat run scripts/deploy.js --network rinkeby

5️⃣ Run the Game Server
cd web/backend
python server.py

6️⃣ Start the Frontend
cd web/frontend
npm start
