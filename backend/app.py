"""
SleepAlert Central Fleet Management Backend (FastAPI)
Cổng tiếp nhận sự kiện cảnh báo từ xe và cung cấp API giám sát đội xe.
"""
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="SleepAlert Fleet Management API",
    description="Hệ thống quản trị và giám sát an toàn tài xế thời gian thực",
    version="1.0.0",
)

# Cho phép CORS cho frontend dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas
class AlertEventPayload(BaseModel):
    vehicle_id: str = Field(..., example="VN-43A-9999")
    driver_id: Optional[str] = Field(None, example="DRV-001")
    event_type: str = Field(..., example="DROWSINESS_CRITICAL")
    ear_value: float = Field(..., example=0.14)
    perclos_value: float = Field(..., example=0.28)
    pitch_angle: float = Field(..., example=-24.5)
    latitude: Optional[float] = Field(None, example=16.0544)
    longitude: Optional[float] = Field(None, example=108.2022)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class AlertEventResponse(BaseModel):
    status: str
    message: str
    event_id: str

# In-memory mock storage for baseline
events_db: List[AlertEventPayload] = []

@app.get("/", tags=["Health"])
async def root():
    return {
        "service": "SleepAlert Fleet API",
        "status": "online",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

@app.post("/api/v1/alerts", response_model=AlertEventResponse, status_code=status.HTTP_201_CREATED, tags=["Alerts"])
async def receive_alert_event(payload: AlertEventPayload):
    """Tiếp nhận sự kiện vi phạm / cảnh báo từ thiết bị Edge trên xe."""
    events_db.append(payload)
    event_id = f"EVT-{len(events_db):05d}"
    print(f"📥 [ALERT RECEIVED] Xe: {payload.vehicle_id} | Loại: {payload.event_type} | EAR: {payload.ear_value} | PERCLOS: {payload.perclos_value}")
    return AlertEventResponse(
        status="success",
        message="Sự kiện cảnh báo đã được ghi nhận",
        event_id=event_id
    )

@app.get("/api/v1/alerts", response_model=List[AlertEventPayload], tags=["Alerts"])
async def list_recent_alerts(limit: int = 50):
    """Lấy danh sách các sự kiện cảnh báo gần nhất."""
    return events_db[-limit:]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)
