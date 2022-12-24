#
import cv2


def click_event(event, x, y, flags, params):

	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.imshow('image', img)


		print(x, ' ', y)

		color = img[y, x]
		print(color)
		hexv = (color[0] << 16) + (color[1] << 8) + (color[2])
		hex_num = hex(hexv)
		print(hex_num)
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) +
					str(g)  + str(r) + ',' + hex_num,
					(x, y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('image', img)

	if event==cv2.EVENT_RBUTTONDOWN:
		cv2.imshow('image', img)

		print(x, ' ', y)



		color = img[y, x]
		hexv = (color[0] << 16) + (color[1] << 8) + (color[2])
		hex_num = hex(hexv)
		print(hex_num)
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r)+','+hex_num,
					(x, y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('image', img)



# driver function
if __name__=="__main__":
	#inp = input("Enter file path: ")
	img = cv2.imread('src/sample.png', 1)


	cv2.imshow('image', img)


	cv2.setMouseCallback('image', click_event)


	cv2.waitKey(0)


	cv2.destroyAllWindows()
