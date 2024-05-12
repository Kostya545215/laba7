import cv2 as cv

#task 1

#функции для подсчета координаты левого верхнего угла фотографии
def calc_coord(x, d, d_n):
    s = x + d//2
    x_n =  s - d_n//2

    return x_n 

img = cv.imread(cv.samples.findFile("laba_python/variant-9.png"))

first = cv.resize(img, (125, 125))
second = cv.resize(img, (150, 150))
third = cv.resize(img, (175,175))
forth = cv.resize(img, (200, 200))

y1 = 0
y2 = 125
y3 = 150 + y2
y4 = 175 + y3 
x1 = 100
x2 = calc_coord(100, 125, 150)
x3 = calc_coord(x2, 150, 175)
x4 = calc_coord(x3, 175, 200)
cv.imshow('Image 1', first)
cv.moveWindow('Image 1', x1, y1)

cv.imshow('Image 2', second)
cv.moveWindow('Image 2', x2, y2 )

cv.imshow('Image 3', third)
cv.moveWindow('Image 3', x3, y3)

cv.imshow('Image 4', forth)
cv.moveWindow('Image 4', x4, y4)
k = cv.waitKey(0)

#task 2

# cap = cv.VideoCapture(0)
# template = cv.imread('laba_python/ref-point.jpg', 0)
# template = cv.resize(template, (100, 100))

# crds_of_cntr = []

# while True:
#     ret, frame = cap.read()
#     frame = cv.resize(frame, (1000, 700))

#     #делаем наше выводимое изображение серым
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     #проверяем соответствие загруженной картинки и кадров с камеры
#     res = cv.matchTemplate(gray, template, cv.TM_CCOEFF_NORMED)

#     #с помощью функции minMaxLoc мы понимаем, где находится картинка, которая посчиталась соответствующей
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
#     top_left_angle = max_loc
    
#     #рисуем 2 линии, чтобы получился крест по середине нашей метки

#     cv.line(gray, (top_left_angle[0] + 50, top_left_angle[1] + 30),(top_left_angle[0] + 50, top_left_angle[1] + 70), (255, 255, 255), 2)
#     cv.line(gray, (top_left_angle[0] + 30, top_left_angle[1] + 50),(top_left_angle[0] + 70, top_left_angle[1] + 50), (255, 255, 255), 2)

#     cv.imshow('frame', gray)

#     if cv.waitKey(1) == ord('q'):
#         break

#     crds_of_cntr.append((top_left_angle[0] + 50, top_left_angle[1] + 50))
    
# cap.release()

# #task 2.2 (запускается вместе с куском кода task 2)

# sum_x = 0
# sum_y = 0

# for i in range(len(crds_of_cntr)):
#     sum_x += crds_of_cntr[i][0]
#     sum_y += crds_of_cntr[i][1]

# print(f'Avg coordinates - ({sum_x//len(crds_of_cntr)}, {sum_y//len(crds_of_cntr)})')