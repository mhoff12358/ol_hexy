from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

class OpenGLDisplay(object):
    def __init__(self, game, width=600, height=400, windowText="_"):
        self.game = game
        self.width = width
        self.height = height
        self.windowText = windowText
        self.window = None
        self.hexside = 15

    #PUBLIC FACING METHODS
    def setupView(self):
        self.setupGl()
        self.setupWindow()
        self.setupGlutCallbacks()

    def teardownView(self):
        self.teardownGlutCallbacks()
        self.teardownWindow()
        self.teardownGlutCallbacks()

    def resizeWindow(self, width=None, height=None):
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

        glViewport(0, 0, self.width, self.height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)

    #INTERNAL METHODS
    def setupWindow(self):
        glutInit('')
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        self.window = glutCreateWindow(self.windowText)
        glutReshapeFunc(self.resizeWindow)
        glDisable(GL_DEPTH_TEST)

    def teardownWindow(self):
        glutDestroyWindow(self.window)
        glutReshapeFunc(lambda: None)

    def setupGl(self):
        glClearColor(0.392, 0.584, 0.929, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_NEVER)
        glShadeModel(GL_SMOOTH)

    def teardownGl(self):
        pass

    def setupGlutCallbacks(self):
        glutDisplayFunc(self.drawScene)
        glutIdleFunc(self.drawScene)

    def teardownGlutCallbacks(self):
        glutDisplayFunc(lambda: None)
        glutIdleFunc(lambda: None)

    def drawScene(self):
        glClearColor(0.392, 0.584, 0.929, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.drawHexOverlay()

        glutSwapBuffers()

    def drawHexOverlay(self):
        glPushMatrix()
        glTranslate(-1, 1, 0)
        glScale(2./self.width, -2./self.height, 1)
        for x in range(54+1):
            for y in range(30+1):
                glPushMatrix()
                glTranslate(x*self.hexside*3./2., y*self.hexside*math.sqrt(3)+(x%2)*self.hexside*math.sqrt(3)/2., 0)
                glColor(0, 0, 0)
                glBegin(GL_LINES)
                glVertex(self.hexside/2, 0, .5)
                glVertex(0, -self.hexside*math.sqrt(3)/2, .5)
                glVertex(self.hexside/2, 0, .5)
                glVertex(0, self.hexside*math.sqrt(3)/2, .5)
                glVertex(self.hexside/2, 0, .5)
                glVertex(self.hexside*3/2, 0, .5)
                glEnd()
                glPopMatrix()
        glPopMatrix()