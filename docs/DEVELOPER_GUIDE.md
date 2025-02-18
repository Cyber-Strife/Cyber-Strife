# Cyber Strife Developer Guide

## 1. Overview
This guide provides technical documentation for developers contributing to **Cyber Strife**, covering **AI Overlords, smart contracts, game mechanics, and Web3 integration**.

---

## 2. Project Structure

### 2.1 Directory Layout
```
cyber-strife/
│── docs/                 # Documentation files
│── src/                  # Source code
│   ├── agents/           # AI Agent logic
│   ├── contracts/        # Smart contracts
│   ├── game/             # Game mechanics
│   ├── web/              # Web frontend & backend
│── tests/                # Test scripts
│── scripts/              # Utility scripts
│── config/               # Configuration files
│── assets/               # Images, media, and branding
```
---

## 3. AI Overlord Development

### 3.1 Training AI Overlords
AI Overlords use **reinforcement learning models** to adapt to **hacking strategies**. The AI models are stored in:
src/agents/models/

### 3.2 Running AI Simulations
python scripts/train_ai.py

---

## 4. Smart Contract Development

### 4.1 Key Contracts
Contract            | Description
------------------- | ----------------------------------------
Token.sol          | $CYBER token contract
Marketplace.sol    | NFT trading contract
Governance.sol     | DAO governance contract
Staking.sol        | Staking contract for rewards

### 4.2 Deploying Contracts
cd src/contracts
npx hardhat compile
npx hardhat run scripts/deploy.js --network rinkeby

---

## 5. Game Mechanics

### 5.1 PvP & PvE Systems
- **PvP Battles:** game/cyber_arena.py
- **PvE Missions:** game/pve_ai.py

### 5.2 Leaderboards & Syndicates
- **Ranking System:** game/ranking.py
- **Guilds & Alliances:** game/syndicate.py

---

## 6. Web3 Integration

### 6.1 API Endpoints
Endpoint               | Description
---------------------- | -------------------------------------
POST /api/ai/train    | Train AI Overlord
POST /api/pvp/match   | Initiate PvP battle
POST /api/token/stake | Stake $CYBER tokens

---

## 7. Contribution Guidelines

### 7.1 Submitting Code
- **Follow PEP8 for Python & Solidity best practices.**
- **Write unit tests before committing new features.**
- **Ensure smart contracts pass security audits.**

### 7.2 Running Tests
pytest tests/

---

## 8. Getting Involved
Join our **developer community**:
- 🚀 Discord: Cyber Strife Dev Hub (https://discord.gg/cyberstrife)
-
