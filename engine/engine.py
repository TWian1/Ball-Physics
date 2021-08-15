import os
import json
import time as t
class settings:
  def screensize(x, y):
    settings = open('engine/settings.json', 'r').readlines()
    settings[1] = " \"GameHeight\": \"" + str(y) + "\",\n"
    settings[2] = " \"GameWidth\": \"" + str(x) + "\",\n"
    open('engine/settings.json', 'w').writelines(settings)
    settings2 = json.loads(open('engine/settings.json', 'r').read())
    notouch.inititializeboard(int(settings2["GameHeight"]), int(settings2["GameWidth"]), settings2["BoardStartColor"])
  def startingcolor(color):
    settings = open('engine/settings.json', 'r').readlines()
    settings[3] = " \"BoardStartColor\": \"" + color + "\",\n"
    open('engine/settings.json', 'w').writelines(settings)
    settings2 = json.loads(open('engine/settings.json', 'r').read())
    notouch.inititializeboard(int(settings2["GameHeight"]), int(settings2["GameWidth"]), settings2["BoardStartColor"])
class time:
  def sleep(seconds):
    t.sleep(seconds)
  def time():
    return t.time()
class notouch:
  def inititializeboard(height, width, startcolor):
    boardcopy = []
    for a in range(height):
      for b in range(width):
        boardcopy.append(startcolor + "\n")
      boardcopy.append("line\n")
    open("engine/ImageProcessing/image.txt", 'w').writelines(boardcopy)
  def checkifsprite(inpname):
    data = ps.getdata()
    if inpname in data.names: return True
    else: return False
  def updateboard(newboard):
    board = open("engine/ImageProcessing/image.txt", 'w')
    board.writelines(newboard)
  def refresh():
    data = ps.getdata()
    for a in range(len(data.names)):
      pixel.color(data.xs[a], data.ys[a], data.colors[a])

class general:
  def start():
    settings2 = open('engine/settings.json', 'r').readlines()
    settings2[1] = " \"GameHeight\": \"20\",\n"
    settings2[2] = " \"GameWidth\": \"20\",\n"
    settings2[3] = " \"BoardStartColor\": \"0 0 0\",\n"
    open('engine/settings.json', 'w').writelines(settings2)

    ps.clear()
    settings = json.loads(open('engine/settings.json', 'r').read())
    clearmsg = ['cls', 'clear'][1]
    change = open('engine/settings.json', 'r').readlines()
    change[4] = " \"OS\": \"" + clearmsg + "\"\n"
    open('engine/settings.json', 'w').writelines(change)
    notouch.inititializeboard(int(settings["GameHeight"]), int(settings["GameWidth"]), settings["BoardStartColor"])

  def printbrd():
    notouch.refresh()
    import engine.ImageProcessing.render as prcs
    prcs.main()

  def clearscreen():
    settings = json.loads(open('engine/settings.json', 'r').read())
    os.system(settings["OS"])

class inpt:
  
  def text(Question):
    a = input("\n" + Question)
    print("\n")
    return a

class pixel:
  def colorfill(xpos, ypos, width, length, color):
    for a in range(length):
      for b in range(width):
        pixel.color(xpos + b, ypos + a, color)
  def color(x, y, color):
    settings = json.loads(open('engine/settings.json', 'r').read())
    imagefilecopy = open('engine/ImageProcessing/image.txt', 'r').readlines()
    index = x + (y*int(settings["GameWidth"])) + y
    imagefilecopy[index] = color + "\n"
    notouch.updateboard(imagefilecopy)
  class data():
    def p(x, y):
      notouch.refresh()
      settings = json.loads(open('engine/settings.json', 'r').read())
      b = open('engine/ImageProcessing/image.txt', 'r').readlines()
      c = []
      for a in b:
        if not(a == "line\n"):
          c.append(a.rstrip('\n'))
      index = x + (y*int(settings["GameWidth"]))
      return c[index]
    def a():
      notouch.refresh()
      b = open('engine/ImageProcessing/image.txt', 'r').readlines()
      c = []
      for a in b:
        if not(a == "line\n"):
          c.append(a.rstrip('\n'))
      return c
class ps:
  def move(name, x, y, ofx, ofy):
    if notouch.checkifsprite(name):
      pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
      index = 0
      data = ps.getdata()
      indexsprte = ps.index(name)
      oldposx = data.xs[indexsprte]
      oldposy = data.ys[indexsprte]
      if x == -1 and y == -1:
        index = data.xs[indexsprte] + ofx
        indey = data.ys[indexsprte] + ofy
      else:
        index = x
        indey = y
      pixelsprites[indexsprte] = name + " " + data.colors[indexsprte] + " " + str(index) + " " + str(indey) + "\n"
      open('engine/data/pixelsprites.txt', 'w').writelines(pixelsprites)
      pixel.color(oldposx, oldposy, "0 0 0")

  def changecolor(name, color):
    pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
    if notouch.checkifsprite(name):
      spaces = 0
      tempx = ""
      tempy = ""
      for a in pixelsprites[ps.index(name)]:
        if a == " ":
          spaces+=1
        else:
          if spaces == 4:
            tempx += a
          if spaces == 5:
            tempy += a
      pixelsprites[ps.index(name)] = name + " "+ color + " " + tempx + " " + tempy
      open('engine/data/pixelsprites.txt', 'w').writelines(pixelsprites)

  def new(x, y, color, name):
    data = ps.getdata()
    pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
    if name in data.names: return
    pixelspriteswrite = open('engine/data/pixelsprites.txt', 'w')
    pixelsprites.append(name + " " + color + " " + str(x) + " " + str(y) + "  \n")
    pixelspriteswrite.writelines(pixelsprites)

  def getdata(name=False):
    if name == False:
      class data:
        colors = []
        names = []
        xs = []
        ys = []
      pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()   
      for a in pixelsprites:
        color = ""
        tempx = ""
        tempy = ""
        name = ""
        spaces = 0
        for b in a:
          if b == " ": 
            spaces += 1
            if spaces in [2, 3]: color += " "
          else:
            if spaces in [1, 2, 3]: color += b
            if spaces == 4: tempx += b
            if spaces == 5: tempy += b
            if spaces == 0: name += b
        data.colors.append(color)
        data.names.append(name)
        data.xs.append(int(tempx))
        data.ys.append(int(tempy))
      return data
    else:
      class data:
        color = ""
        x = 0
        y = 0
      pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()   
      color = ""
      tempx = ""
      tempy = ""
      spaces = 0
      for b in pixelsprites[ps.index(name)]:
        if b == " ": 
          spaces += 1
          if spaces in [2, 3]: color += " "
        else:
          if spaces in [1, 2, 3]: color += b
          if spaces == 4: tempx += b
          if spaces == 5: tempy += b
      data.color = color
      data.x = int(tempx)
      data.y = int(tempy)
      return data

  def clear():
    data = ps.getdata()
    for a in range(len(data.names)):
      pixel.color(data.xs[a], data.ys[a], "0 0 0")
    open('engine/data/pixelsprites.txt', 'w')
  def index(inpname):
    pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
    counter = -1
    for a in pixelsprites:
      counter +=1
      name = ""
      space = True
      for b in a:
        if b == " ": space = False
        if space: name += b
      if name == inpname: return counter