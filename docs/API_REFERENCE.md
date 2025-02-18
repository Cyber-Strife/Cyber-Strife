# Cyber Strife API Reference

## Overview
The Cyber Strife API allows developers to interact with the **AI Overlords**, battle system, staking mechanisms, and economy using RESTful API calls.

---

## 1. AI Overlord Management

### Train AI Overlord
**Endpoint:**  
POST /api/ai/train

**Parameters:**
{
  "overlord_id": "12345",
  "experience": 100,
  "strategy": "offensive"
}

**Response:**
{
  "status": "success",
  "message": "AI Overlord training initiated."
}

### Get AI Overlord Status
**Endpoint:**  
GET /api/ai/status/{overlord_id}

**Response:**
{
  "overlord_id": "12345",
  "level": 5,
  "hacking_power": 450,
  "defense": 300
}

---

## 2. PvP & PvE Battles

### Initiate PvP Battle
**Endpoint:**  
POST /api/pvp/match

**Parameters:**
{
  "player_overlord_id": "12345",
  "opponent_overlord_id": "67890"
}

**Response:**
{
  "status": "success",
  "match_id": "98765",
  "result": "pending"
}

### Get Battle Results
**Endpoint:**  
GET /api/pvp/result/{match_id}

**Response:**
{
  "match_id": "98765",
  "winner": "12345",
  "loser": "67890",
  "xp_earned": 150
}

---

## 3. $CYBER Token Economy

### Stake $CYBER Tokens
**Endpoint:**  
POST /api/token/stake

**Parameters:**
{
  "user_wallet": "0xABC123...",
  "amount": 1000
}

**Response:**
{
  "status": "success",
  "message": "1000 $CYBER tokens staked."
}

### Get Staking Rewards
**Endpoint:**  
GET /api/token/rewards/{user_wallet}

**Response:**
{
  "wallet": "0xABC123...",
  "rewards": 50
}

---

## 4. NFT Marketplace

### List AI Overlord for Sale
**Endpoint:**  
POST /api/nft/list

**Parameters:**
{
  "overlord_id": "12345",
  "price": 5000
}

**Response:**
{
  "status": "success",
  "message": "AI Overlord listed for 5000 $CYBER."
}

### Purchase AI Overlord
**Endpoint:**  
POST /api/nft/buy

**Parameters:**
{
  "buyer_wallet": "0xXYZ789...",
  "overlord_id": "12345"
}

**Response:**
{
  "status": "success",
  "message": "AI Overlord purchased successfully."
}

---

## 5. Leaderboards & Rankings

### Get Global Rankings
**Endpoint:**  
GET /api/leaderboard/global

**Response:**
[
  {"rank": 1, "player": "0xABC123...", "wins": 50, "losses": 5},
  {"rank": 2, "player": "0xDEF456...", "wins": 48, "losses": 7},
  {"rank": 3, "player": "0xXYZ789...", "wins": 45, "losses": 10}
]

---

## Error Handling
All API responses will return a **status** field indicating success or failure.  
Example of an error response:
{
  "status": "error",
  "message": "Invalid API key."
}

## API Authentication
To use certain API endpoints, developers must include an API key in the request headers:
Authorization: Bearer YOUR_API_KEY

---

## Conclusion
The Cyber Strife API provides seamless interaction with AI Overlords, battles, and the $CYBER token economy. Developers can extend and integrate the API to build custom applications, automation tools, or analytics dashboards.

📖 **For more details, visit the [Cyber Strife Developer Hub](https://dev.cyberstrife.com)**  
