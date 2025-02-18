# Cyber Strife API Reference

## AI Overlord API

### Train AI Overlord
POST /api/ai/train
Parameters:
{
  "overlord_id": "12345",
  "experience": 100,
  "strategy": "offensive"
}
Response:
{
  "status": "success",
  "message": "AI Overlord training initiated."
}

### AI Overlord Status
GET /api/ai/status/{overlord_id}
Response:
{
  "overlord_id": "12345",
  "level": 5,
  "hacking_power": 450,
  "defense": 300
}

## PvP & PvE Battle API

### Start PvP Hacking Battle
POST /api/pvp/match
Parameters:
{
  "opponent_id": "0x123",
  "wager": 100
}
Response:
{
  "status": "success",
  "battle_id": "abc123",
  "message": "PvP match initiated."
}
