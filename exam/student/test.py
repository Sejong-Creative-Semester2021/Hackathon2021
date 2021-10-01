import cv2
from datetime import datetime, timedelta
from pytz import timezone
import keyboard
# from pynput.keyboard import Key, Listener
import keyboard

while True:
    x = keyboard.read(1000,timeout=0)
    if len(x):
        print(x)
# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
# while True:
#     if keyboard.is_pressed('c'):
#         print('복사하셨습니다.')
#     if keyboard.is_pressed('ctrl+v'):
#         print('붙혀넣기 하셨습니다.')
# cap = cv2.VideoCapture(0)
# now = datetime.now(timezone('Asia/Seoul'))
# file_name = now.strftime('%Y%m%d-%H%M%S')
# print(file_name)
# if cap.isOpened:
#     file_path = 'record.avi'
#     fps = 10.0
#     fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#     width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#     height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#     size = (int(width), int(height))
#     out = cv2.VideoWriter(file_path, fourcc, fps, size)
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow('camera-recording', frame)
#             out.write(frame)
#             if cv2.waitKey(int(1000/fps)) != -1:
#                 break

#         else:
#             print('no frame!')
#             break
#     out.release()
# else:
#     print('cant open camera')
# cap.release()
# cv2.destroyAllWindows()