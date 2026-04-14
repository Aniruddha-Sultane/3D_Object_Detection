import cv2
from detector import detect_objects
from depth import estimate_depth

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Object detection
    results = detect_objects(frame)

    # Depth estimation
    depth_map = estimate_depth(frame)

    # Draw detections
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])

        # Get depth at center
        cx, cy = (x1+x2)//2, (y1+y2)//2
        depth_value = depth_map[cy, cx]

        label = f"{results.names[cls]} {conf:.2f} D:{depth_value}"

        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(frame, label, (x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    # Show outputs
    cv2.imshow("Detection", frame)
    cv2.imshow("Depth", depth_map)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()