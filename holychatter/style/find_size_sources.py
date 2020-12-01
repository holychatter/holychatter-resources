
paddingVal=15
min_width=150
max_width=150

def widthOfFolders(nbOfFolders, withOfAFolder):
  return withOfAFolder*nbOfFolders + paddingVal*nbOfFolders*2 + paddingVal*2



def maxNbOfFolders(winowSize):
  res=2
  while widthOfFolders(res, min_width)<=winowSize:
    res+=1
  return res-1


def maxFolderWidth(winowSize, nbOfFolders):
  res=min_width+1
  while widthOfFolders(nbOfFolders, res)<=winowSize and res<=max_width:
    res+=1
  return res-1

def getHeight(width):
  return width



f= open("sources.css","w")

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
  f.write(".hc-sources-left-margin { margin-left: " + str(margin) + "px; }\n")
  f.write("}\n\n")
  if winowSize == 301:
    break
  winowSize-=step

f.write(".hc-big-button-source-height { height:150px; }\n")
f.write(".hc-big-button-source-width { width:150px; }\n")
f.close()
