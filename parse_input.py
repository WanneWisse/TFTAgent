import cv2
import os

def load_images_to_numpy(folder):
    images = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        images.append(img)
    return images

def match_image(images, image_to_match):
    if(len(images) == 0):
        images.append(image_to_match)
    else:
        found = False
        for image in images:
            match_score = cv2.matchTemplate(image, image_to_match, cv2.TM_CCOEFF_NORMED)[0][0]
            if(match_score > 0.6):
                found = True
                break
        if(found == False):
            images.append(image_to_match)
def save_images(folder, images):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        os.remove(path)
    
    for index, image in enumerate(images):
        cv2.imwrite(f"{folder}/{index}.png", image)



images = load_images_to_numpy('images')

cap = cv2.VideoCapture("output.mp4")

width_shopbox = 190
height_shopbox = 140

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # video ended

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for i in range(5):
        x1 = 508 + i * width_shopbox
        x2 = 690 + i * width_shopbox
        y1 = 925
        y2 = 1065

        crop = gray[y1:y2, x1:x2]
        match_image(images, crop)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

save_images('images', images)