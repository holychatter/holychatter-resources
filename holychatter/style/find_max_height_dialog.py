
f= open("dialog_max_height.css","w")

winowHeight=1551
step=25

while True:
  height = winowHeight - 150
  if winowHeight == 1551:
    f.write("@media screen and (min-height: " + str(winowHeight) + "px) {\n")
  elif winowHeight == 301:
    f.write("@media only screen and (max-height: 325px) {\n")
  else:
    f.write("@media screen and (min-height: " + str(winowHeight) + "px)  and (max-height: " + str(winowHeight+step-1) + "px) {\n")
  f.write(".hc-dialog-height-match-screen { height: " + str(height) + "px; }\n")
  f.write("}\n\n")
  if winowHeight == 301:
    break
  winowHeight-=step

f.close()
