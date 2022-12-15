import os
import cv2
import shutil

def SDM(folder):
	tmp = os.path.join(os.path.split(folder)[0], "tmp")
	try:
		os.mkdir(tmp)
	except FileExistsError:
		shutil.rmtree(tmp)
		os.mkdir(tmp)
	
	sdm = os.path.join(os.path.join(os.path.split(folder)[0], 'tmp'), 'a_sdm.png')


	if os.path.isdir(folder):
		items = os.listdir(folder)
		weight = (1/len(items))*2
		for idx, i  in enumerate(items):
			img = os.path.join(folder, i)
			im = cv2.imread(img)
			im_mult = cv2.multiply(cv2.multiply(im, weight),10)
			im_name = os.path.join(tmp, 'sdm_' + str(idx)+'.png')
			cv2.imwrite(im_name, im_mult)	
	for idx, i in enumerate(os.listdir(tmp)):
		im1 = cv2.imread(os.path.join(tmp, os.listdir(tmp)[0]))

		im2 = cv2.imread(os.path.join(tmp, i))

		awm = cv2.add(im1, im2)
		gray = cv2.cvtColor(awm, cv2.COLOR_BGR2GRAY)
		cv2.imwrite(sdm, gray)
	else:
		pass

	os.replace(sdm, os.path.join(os.path.split(folder)[0], os.path.split(sdm)[1]))
	shutil.rmtree(tmp)


SDM('C:/tmp/SDM/png')
