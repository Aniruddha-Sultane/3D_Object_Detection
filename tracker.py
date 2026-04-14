from deep_sort_realtime.deepsort_tracker import DeepSort

tracker = DeepSort(max_age=30)

def track_objects(results, frame):
    detections = []

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])

        detections.append(([x1, y1, x2-x1, y2-y1], conf, 'object'))

    tracks = tracker.update_tracks(detections, frame=frame)

    return tracks