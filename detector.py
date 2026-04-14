from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model([frame], verbose=False)   # ✅ wrap in list
    return results[0]