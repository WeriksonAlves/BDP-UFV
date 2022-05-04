import cv2
#Para opção webcam n = 0, para realsense n = 2. Conferir gerenciador de dispositivos
tipo_camera = 0

cam = cv2.VideoCapture(tipo_camera)
#cam = cv2.VideoCapture(tipo_camera, cv2.CAP_DSHOW)#corrigi bug ao fechar aplicação
cv2.namedWindow("preview")
while True:
    ret, frame = cam.read()
    if not ret:
        print("Câmera desativada")
        break
    cv2.imshow("preview", frame)
    k = cv2.waitKey(1)
    if (cv2.getWindowProperty("preview", cv2.WND_PROP_VISIBLE) <1):
        break

cam.release()
cv2.destroyAllWindows()