
f= open("video_size-1.css","w")

windowSize=1951
step=25

while True:
  videoSize = 0
  if windowSize > 1100:
    videoSize = windowSize - 601
  else:
    videoSize = windowSize - 51
  if windowSize == 1951:
    f.write("@media screen and (min-width: " + str(windowSize) + "px) {\n")
  elif windowSize == 301:
    f.write("@media only screen and (max-width: " + str(windowSize+step-1) + "px) {\n")
  else:
    f.write("@media screen and (min-width: " + str(windowSize) + "px)  and (max-width: " + str(windowSize+step-1) + "px) {\n")
  f.write(".hc-width-content-with-refs { width: " + str(videoSize) + "px; }\n")
  f.write("}\n\n")
  if windowSize == 301:
    break
  windowSize-=step

f.close()
