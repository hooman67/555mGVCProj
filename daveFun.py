import time, re, os


def getY(x1,y1,x2,y2,x3):
	if((x2-x1)==0):
		return None

	m = y2-y1/(x2-x1)

	b = y2 - m*x2;

	return (m*x3 + b);

print(getY(2,4,3,6,1))