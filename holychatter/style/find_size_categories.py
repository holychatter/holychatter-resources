
paddingVal=15

def widthOfFolders(nbOfFolders, withOfAFolder):
  return withOfAFolder*nbOfFolders + paddingVal*nbOfFolders*2 + paddingVal*2



def maxNbOfFolders(winowSize):
  res=2
  while widthOfFolders(res, 270)<=winowSize:
    res+=1
  return res-1


def maxFolderWidth(winowSize, nbOfFolders):
  res=271
  while widthOfFolders(nbOfFolders, res)<=winowSize and res<=320:
    res+=1
  return res-1

def getHeight(width):
  return int(round((width*150)/270.))



f= open("categories.css","w")

winowSize=1951
step=25

while True:
  nbOfFolders = maxNbOfFolders(winowSize)
  width = maxFolderWidth(winowSize, nbOfFolders)
  height = getHeight(width)
  margin = int(round((winowSize - widthOfFolders(nbOfFolders, width) + (paddingVal*2)) / 2.))
  if margin<0:
    margin = 0
  if winowSize == 1951:
    f.write("@media screen and (min-width: " + str(winowSize) + "px) {\n")
  elif winowSize == 301:
    f.write("@media only screen and (max-width: 350px) {\n")
  else:
    f.write("@media screen and (min-width: " + str(winowSize) + "px)  and (max-width: " + str(winowSize+step-1) + "px) {\n")
  f.write(":root {\n")
  f.write("  --hc-val-big-button-normal-height: " + str(height) + "px;\n")
  f.write("  --hc-val-big-button-normal-width: " + str(width) + "px;\n")
  f.write("}\n")
  f.write(".hc-categories-left-margin { margin-left: " + str(margin) + "px; }\n")
  f.write("}\n\n")
  if winowSize == 301:
    break
  winowSize-=step

f.write(".hc-big-button-normal-height { height:var(--hc-val-big-button-normal-height); }\n")
f.write(".hc-big-button-normal-width { width:var(--hc-val-big-button-normal-width); }\n")
f.close()
