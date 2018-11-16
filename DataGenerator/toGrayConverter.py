from PIL import Image, ImageFilter
import sys


def convert(image):
	return image.convert("L")
	
def load(filename):
	return Image.open(filename)
	
def data_to_file(image, filename):
	width, height = image.size
	output_file = open(filename, "w")
	
	output_file.write(str(width) + "\n" + str(height) + "\n")
	for y in range(height):
		for x in range(width):
			output_file.write(str(image.getpixel((x, y))) + " ")
		output_file.write("\n")	

def file_to_image(filename):
	input_file = open(filename, "r")
	inWidth = inHeight = 0
	data = []
	image = []
	
	with open(filename, "r") as file:
		for line in file:
			data.append(line)
	
	inWidth = (int)(data.pop(0))
	inHeight = (int)(data.pop(0))
	
	resultImage = Image.new("L", (inWidth, inHeight))
	
	for y in range(inHeight):
		splitRow = data.pop(0).split(' ')
		image.append([])
		for x in range(inWidth):
			image[y].append((int)(splitRow[x]))
			resultImage.putpixel((x, y), (int)(splitRow[x]))
	return resultImage
		
def help():		
	print("Use: scriptname option filename1 [filename2]")
	print("option could be --gen or --rns")
	print("--gen to generate data, needed 2 filenames")
	print("--rns to show and check data, needed 1 filename")

def main():
	try:
		#gen = generate
		if sys.argv[1] == "--gen":
			image = load(sys.argv[2])
			grayImage = convert(image)
			grayImage.show()
			data_to_file(grayImage, sys.argv[3])
			image.close()
			grayImage.close()
			
		#rns = read and show
		if sys.argv[1] == "--rns":
			fileImage = file_to_image(sys.argv[2])
			fileImage.show()
			fileImage.close()
	except:
		help()
		return
	
	
if __name__ == "__main__":
	main()