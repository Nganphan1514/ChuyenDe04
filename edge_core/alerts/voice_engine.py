"""
Quản lý cảnh báo âm thanh và giọng nói tiếng Việt bất đồng bộ (Non-blocking Audio Engine).
Đảm bảo phát chuông báo động hoặc Text-to-Speech mà không làm suy giảm FPS của camera loop.
"""
import threading
import queue
import time
from typing import Optional

class AsyncAudioEngine:
    def __init__(self):
        self._queue: queue.Queue = queue.Queue(maxsize=10)
        self._running: bool = True
        self._last_alert_time: float = 0.0
        self._worker_thread = threading.Thread(target=self._process_audio_queue, daemon=True)
        self._worker_thread.start()

    def _process_audio_queue(self):
        """Hàm worker chạy trên luồng phụ để tiêu thụ các sự kiện âm thanh."""
        while self._running:
            try:
                alert_type, message = self._queue.get(timeout=0.5)
                self._play_sound(alert_type, message)
                self._queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print(f"[AudioEngine Error] {e}")

    def _play_sound(self, alert_type: str, message: Optional[str] = None):
        """Xử lý âm thanh thực tế dựa trên alert_type."""
        if alert_type == "SIREN":
            print("[AUDIO CRITICAL] KICH HOAT COI BAO DONG NGU GAT!")
        elif alert_type == "WARNING":
            print(f"[AUDIO WARNING] Canh bao met moi: {message or 'Vui long tap trung!'}")
        elif alert_type == "REST_STOP":
            print(f"[AUDIO REST STOP] {message}")

    def trigger_critical_siren(self):
        """Kích hoạt còi báo động ngủ gật khẩn cấp."""
        now = time.time()
        if now - self._last_alert_time >= 1.0: # Cooldown 1s
            self._last_alert_time = now
            if not self._queue.full():
                self._queue.put(("SIREN", None))

    def trigger_fatigue_warning(self, text: str = "Tài xế có dấu hiệu mệt mỏi"):
        """Nhắc nhở mệt mỏi nhẹ nhàng."""
        now = time.time()
        if now - self._last_alert_time >= 3.0: # Cooldown 3s
            self._last_alert_time = now
            if not self._queue.full():
                self._queue.put(("WARNING", text))

    def trigger_rest_recommendation(self, place_name: str, distance_km: float):
        """Gợi ý trạm dừng nghỉ gần nhất."""
        msg = f"Gợi ý trạm dừng nghỉ {place_name}, cách khoảng {distance_km:.1f} km"
        if not self._queue.full():
            self._queue.put(("REST_STOP", msg))

    def stop(self):
        """Dừng luồng worker âm thanh."""
        self._running = False
        if self._worker_thread.is_alive():
            self._worker_thread.join(timeout=1.0)

# Singleton instance
audio_engine = AsyncAudioEngine()
