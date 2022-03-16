# Run this every boot.
from gpiozero import LED

d = LED(27)
b = LED(21)
m = LED(4)
r = LED(26)
g = LED(19)
bl = LED(13)
bu = LED(3)

d.on()
b.on()
m.on()
r.off()
g.off()
bl.off()
bu.off()
