#!/usr/bin/python
# This is a captcha-breaker modified from http://www.boyter.org/decoding-captchas/
# The original handles number captcha
# This code can handle man-shape letter captcha

from PIL import Image
import hashlib
import time
import os
import math
import sys
from BeautifulSoup import BeautifulSoup



class VectorCompare:
  def magnitude(self,concordance):
    total = 0
    for word,count in concordance.iteritems():
      total += count ** 2
    return math.sqrt(total)

  def relation(self,concordance1, concordance2):
    relevance = 0
    topvalue = 0
    for word, count in concordance1.iteritems():
      if concordance2.has_key(word):
        topvalue += count * concordance2[word]
    return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))



def buildvector(im):
  d1 = {}
  count = 0
  for i in im.getdata():
    d1[count] = i
    count += 1
  return d1

# Main function
if __name__ == '__main__':
	# Input the captcha file that you want to break
	im = Image.open("out.png")
	
	# PIL complains if you don't load explicitly
	im.load()

	# Get the alpha band
	alpha = im.split()[-1]
	im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

	# Set all pixel values below 10 to 255,
	# and the rest to 0
	mask = Image.eval(alpha, lambda a: 255 if a <=10 else 0)
	# Paste the color of index 255 and use alpha as a mask
	im.paste(255, mask)

	# The transparency index is 255
	im.save("out.gif", transparency=255)
	v = VectorCompare()

	iconset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	imageset = []

	for letter in iconset:
	  for img in os.listdir('./iconset/%s/'%(letter)):
		temp = []
		if img != "Thumbs.db": # windows check...
		  temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
		imageset.append({letter:temp})

	# Read the image file
	im = Image.open("out.gif")
	im2 = Image.new("P",im.size,255)
	im = im.convert("P")
	temp = {}

	for x in range(im.size[1]):
	  for y in range(im.size[0]):
		pix = im.getpixel((y,x))
		temp[pix] = pix
		if pix == 1 or pix == 3 or pix == 4 or pix == 5 or pix == 6 or pix == 7: # these are the numbers to get
		  im2.putpixel((y,x),0)
		
	inletter = False
	foundletter=False
	start = 0
	end = 0

	letters = []

	for y in range(im2.size[0]): # slice across
	  for x in range(im2.size[1]): # slice down
		pix = im2.getpixel((y,x))
		if pix != 255:
		  inletter = True

	  if foundletter == False and inletter == True:
		foundletter = True
		start = y

	  if foundletter == True and inletter == False:
		foundletter = False
		end = y
		letters.append((start,end))


	  inletter=False
	# Crack the captcha and print the result
	count = 0
	k = 0
	result = [0]*len(letters)
	for letter in letters:
	  m = hashlib.md5()
	  im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
	  guess = []
	  for image in imageset:
		for x,y in image.iteritems():
		  if len(y) != 0:
		    guess.append( ( v.relation(y[0],buildvector(im3)),x) )

	  guess.sort(reverse=True)
	  result[k] = guess[0][1]
	  k += 1
	  count += 1
	print result








