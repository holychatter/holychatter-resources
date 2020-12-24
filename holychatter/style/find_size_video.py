
f= open("video_size-1.css","w")

winowSize=1951
step=25

while True:
  videoSize = 0
  if winowSize > 1100:
    videoSize = winowSize - 601
  else:
    videoSize = winowSize - 51
  if winowSize == 1951:
    f.write("@media screen and (min-width: " + str(winowSize) + "px) {\n")
  elif winowSize == 301:
    f.write("@media only screen and (max-width: " + str(winowSize+step-1) + "px) {\n")
  else:
    f.write("@media screen and (min-width: " + str(winowSize) + "px)  and (max-width: " + str(winowSize+step-1) + "px) {\n")
  f.write(".hc-width-content-with-refs { width: " + str(videoSize) + "px; }\n")
  if videoSize > 500:
    f.write(".hc-width-image-with-refs { width: 500px; }\n")
  else:
    f.write(".hc-width-image-with-refs { width: " + str(videoSize) + "px; }\n")
  f.write("}\n\n")
  if winowSize == 301:
    break
  winowSize-=step

f.close()
