from engine.engine import ps, general, inpt, pixel, time, settings
general.start()

bounciness = 10
acc = 1.4
decel = 1.01
startx = 0
starty = 7
trace = False
loops = 100


ps.new(startx, starty, "255 255 255", "ball")
xspeed = 1
yspeed = -3
xpos = startx
ypos = starty
lastx = 0
lastlasty = 0
lasty = 0
for a in range(loops):
  time.sleep(0.3)
  general.clearscreen()
  general.printbrd()
  lastlasty = lasty
  lastx = round(xpos)
  lasty = round(ypos)
  xpos += xspeed
  xspeed = xspeed / decel
  yspeed = yspeed + acc
  ypos += yspeed
  if xpos > 19.4:
    xspeed = ((xspeed * -1) / (3*(0.9**bounciness)))
    xpos = 19.4
  if xpos < -0.4:
    xspeed = ((xspeed * -1) / (3*(0.9**bounciness)))
    xpos = -0.4
  if ypos > 19.4:
    yspeed = ((yspeed * -1) / (3*(0.9**bounciness)))
    ypos = 19.4
    xspeed = xspeed / decel
  if ypos < -0.4:
    yspeed = ((yspeed * -1) / (3*(0.9**bounciness)))
    ypos = -0.4
    xspeed = xspeed / decel
  ps.move("ball", round(xpos), round(ypos), 0, 0)
  if trace:
    pixel.color(lastx, lasty, "255 0 0")
  if abs(xspeed) < 0.25:
    xspeed = 0