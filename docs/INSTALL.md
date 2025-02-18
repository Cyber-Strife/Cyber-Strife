# Installation Guide

## Prerequisites
Before installing Cyber Strife, ensure you have the following dependencies installed:
- **Python 3.9+**
- **Node.js 16+**
- **Solidity Compiler**
- **Docker (Optional)**
- **Git**

## Installation Steps

### Clone the Repository
git clone https://github.com/YOUR_USERNAME/cyber-strife.git
cd cyber-strife

### Set Up Python Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### Install Frontend Dependencies
cd web/frontend
npm install

### Deploy Smart Contracts (Testnet)
cd src/contracts
npx hardhat compile
npx hardhat run scripts/deploy.js --network rinkeby

### Run the Game Server
cd web/backend
python server.py

### Start the Frontend
cd web/frontend
npm start

## Additional Setup
- **Database Configuration:** Ensure your database is running and accessible.
- **Environment Variables:** Copy `config/env.example` to `.env` and update settings.

## Troubleshooting
- If installation fails, verify that all dependencies are correctly installed.
- Check for any missing environment variables or incorrect configurations.

## Support
For support, please join our [Discord](https://discord.gg/cyberstrife) or open an issue on [GitHub](https://github.com/YOUR_USERNAME/cyber-strife/issues).
