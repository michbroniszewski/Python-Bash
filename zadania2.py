#zad 1
#plik z lista studentow
# try:
#     f = open("lista.txt",'r+')
# except IOError:
#     f = open("lista.txt",'w')
# lista = []
# t = ''
# while t != 'y':
#     t = input("Podaj liste studentow > [koniec: y ]")
#     lista.append(t)
# lista = lista[:len(lista)-1]
# if f.mode == 'w':
#     for line in lista:
#         f.write(line + '\n')
# else:
#     f.seek(0,2)
#     for line in lista:
#         f.write(line + '\n')
# f.close()

#zad 2
#klasa reprezentujaca liczbe zespolona

# class Complex:
#     def __init__(self, re , im):
#         self.re = re
#         self.im = im

#     def __add__(self, complex_number):
#         return Complex(self.re + complex_number.re, self.im + complex_number.im)

#     def __sub__(self, complex_number):
#         return Complex(self.re - complex_number.re, self.im - complex_number.im)

#     def __truediv__(self, complex_number):
#         if complex_number.re and complex_number.im == 0:
#             return

#         a = self.re
#         b = self.im
#         c = complex_number.re
#         d = complex_number.im

#         return Complex((a * c + b * d)/(c ** 2 + d ** 2), (b * c - a * d)/(c ** 2 + d ** 2))

#     def __mul__(self, complex_number):

#         a = self.re
#         b = self.im
#         c = complex_number.re
#         d = complex_number.im

#         return Complex((a * c - b * d), (a * d + b * c))

#     def __str__(self):
#         temp = str(self.im)
#         if self.im >= 0:
#             temp = "+" + temp

#         return str(self.re) + temp + "i"
    
# if __name__ == "__main__":
#     a = Complex(1,4)
#     b = Complex(2,4)

#     print(b / a)
#     print(b + a)
#     print(b - a)
#     print(b * a)

# zad3
from xml.dom.minidom import parseString, getDOMImplementation

# test_xml = '''<?xml version="1.0" encoding="ISO-8859-1"?>
# <AppName>
#     <out>This is a sample output with <test>default</test> text </out>
# </AppName>'''

# replacements = {'test':'example'}
# dom = parseString(test_xml)
# if (len(dom.getElementsByTagName('out'))!=0):
#     xmlTag = dom.getElementsByTagName('out')[0]
#     children =  xmlTag.childNodes
#     text = ""
#     for c in children:
#         if c.nodeType == c.TEXT_NODE:
#             text += c.data
#         else:
#             if c.nodeName in replacements.keys():
#                 text += replacements[c.nodeName]
#             else: # not text, nor a listed tag
#                 text += c.toxml()
#     print (text)

#zad 5
import threading
# import random
# import time


# # Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.
# #
# # Deadlock is avoided by never waiting for a fork while holding a fork (locked)
# # Procedure is to do block while waiting to get first fork, and a nonblocking
# # acquire of second fork.  If failed to get second fork, release first fork,
# # swap which fork is first and which is second and retry until getting both.
# #
# # See discussion page note about 'live lock'.

# class Philosopher(threading.Thread):
#     running = True

#     def __init__(self, xname, forkOnLeft, forkOnRight):
#         threading.Thread.__init__(self)
#         self.name = xname
#         self.forkOnLeft = forkOnLeft
#         self.forkOnRight = forkOnRight

#     def run(self):
#         while (self.running):
#             #  Philosopher is thinking (but really is sleeping).
#             time.sleep(random.uniform(3, 13))
#             print ('%s is hungry.' % self.name)
#             self.dine()

#     def dine(self):
#         fork1, fork2 = self.forkOnLeft, self.forkOnRight

#         while self.running:
#             fork1.acquire(True)
#             locked = fork2.acquire(False)
#             if locked: break
#             fork1.release()
#             print ('%s swaps forks' % self.name)
#             fork1, fork2 = fork2, fork1
#         else:
#             return

#         self.dining()
#         fork2.release()
#         fork1.release()

#     def dining(self):
#         print ('%s starts eating ' % self.name)
#         time.sleep(random.uniform(1, 10))
#         print ('%s finishes eating and leaves to think.' % self.name)


# def DiningPhilosophers():
#     forks = [threading.Lock() for n in range(5)]
#     philosopherNames = ('Aristotle', 'Kant', 'Buddha', 'Marx', 'Russel')

#     philosophers = [Philosopher(philosopherNames[i], forks[i % 5], forks[(i + 1) % 5]) \
#                     for i in range(5)]

#     random.seed(507129)
#     Philosopher.running = True
#     for p in philosophers: p.start()
#     time.sleep(100)
#     Philosopher.running = False
#     print ("Now we're finishing.")


# DiningPhilosophers()
