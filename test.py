import os, cv2

# Image prediction boxes in order
# Each array containes object in continues matching
PredBoxes = {
  "636.jpg": ([890,1774], [1930, 1347],[2532, 1478], [4508,1680], [4879,1936], [7067,1683]), # First Image Objects
  "637.jpg": ([739,1823], [1573, 1369],[2231, 1436], [4624,1608], [5577,1829], [7460,1781]), # Second Image Objects
  "638.jpg": ([655,1837], [1302, 1434],[1930, 1447], [4764,1535], [6725,1784], [7655,1792]), # Third Image Objects
  "639.jpg": ([545,1860], [1021, 1515],[1542, 1467], [5009,1409], [7445,1867], [7791,1840])  # Forth Image Objects
}

def imageFov (im):
    # FOV lines®®®
    cv2.line(im, (4096, 4096), (0, 0), (224, 224, 224), 10)
    cv2.line(im, (4096, 4096), (8192, 0), (224, 224, 224), 10)
    cv2.putText(im, '0', (4030, 4000), cv2.FONT_HERSHEY_SIMPLEX,
                5, (255, 0, 0), 5, cv2.LINE_AA)

def calcDiff (data):
    print(1)


for img in PredBoxes:
    image_path = os.path.join("./imgs", img)
    im = cv2.imread(image_path)
    imageFov(im)
    for obj in PredBoxes[img]:
        cv2.line(im, (4096, 4096), obj, (255, 255, 120), 10)
        # calcDiff(PredBoxes, obj)
    cv2.imshow("panoptic prediction", im)
    cv2.waitKey(0)