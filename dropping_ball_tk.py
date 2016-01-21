import turtle, random, time, math
import Tkinter

class Ball (turtle.RawTurtle):

    def __init__ (self, world, initX=0, initY=0, color='black', size=5, xvel=0, yvel=0):
        turtle.RawTurtle.__init__(self,world.canvas)
        self.world = world
        self.up()
        self.goto(initX, initY)
        self.down()
        self.color(color)
        self.shapesize(outline=size)
        self.shape('circle')
        self.xvel = xvel
        self.yvel = yvel
        self.speed(0)
        
    def tick (self):
        self.yvel -= self.world.gravity 
        x,y = self.pos()
        self.goto(x+self.xvel,y+self.yvel)
        self.checkEdges()
        if 0.3 > self.yvel  > -0.3:
            self.yvel = 0
            # Just stop it already

    def checkEdges (self):
        x,y = self.pos()
        if x > self.world.width/2:
            self.goto(self.world.width/2,y)
            if self.xvel > 0:
                self.xvel = self.xvel * -1 * self.world.wall_elasticity
        if x < -self.world.width/2:
            self.goto(-self.world.width/2,y)
            if self.xvel < 0:
                self.xvel = self.xvel * -1 * self.world.wall_elasticity
        if y < -self.world.height/2:
            self.goto(x,-self.world.height/2)
            if self.yvel < 0:
                self.yvel = self.yvel * -1 * self.world.wall_elasticity
        

class World ():
    
    gravity = 9.8
    wall_elasticity = 0.8

    width = 750
    height = 750

    balls = []
    colors = ['red','blue','green','orange','#0033a0','#c6093b','grey','purple','brown','pink']
    ncolor = 0

    def __init__ (self):
        self._ticking = False
        self.root = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.setup_buttonbox()

    def setup_buttonbox (self):
        self.buttonBox = Tkinter.Frame(self.root)
        self.buttonBox.pack(fill=Tkinter.BOTH, expand=True)
        self.smallButton = self.createButton(
            'Small',
            self.onSmall
            )
        self.medButton = self.createButton(
            'Medium',
            self.onMedium
            )
        self.onLarge = self.createButton(
            'Large',
            self.onLarge
            )
        self.gravityLabel = Tkinter.Label(self.buttonBox,text='Gravity:')
        self.gravityLabel.pack(side=Tkinter.LEFT,expand=0)
        self.gravityScale = Tkinter.Scale(self.buttonBox, from_=0.1, to=24, orient=Tkinter.HORIZONTAL)
        self.gravityScale.set(self.gravity)
        self.gravityScale['command'] = self.onUpdateGravity
        self.gravityScale.pack(side=Tkinter.LEFT,expand=0)
        self.clearButton = self.createButton(
            'Clear',
            self.onClear
            )
        self.elasticLabel =Tkinter.Label(self.buttonBox,text='Wall Elasticity:')
        self.elasticLabel.pack(side=Tkinter.LEFT,expand=0)
        self.elasticscale = Tkinter.Scale(self.buttonBox, from_=0.1, to=2,orient=Tkinter.HORIZONTAL)
        self.elasticscale.set(self.wall_elasticity)
        self.elasticscale['command']=self.onUpdateElasticity
        self.elasticscale.pack(side=Tkinter.LEFT,expand=0)

    def createButton (self, text, command):
        '''Create a button and add it to the righthand side of the button box.
        '''
        button = Tkinter.Button(self.buttonBox)
        button['text'] = text
        button['command'] = command
        button.pack(side=Tkinter.RIGHT, expand=0)
        return button

    # Callbacks...

    def onUpdateGravity (self, *args):
        self.gravity = self.gravityScale.get()
    def onUpdateElasticity (self, *args):
        self.wall_elasticity = self.elasticscale.get()

    def onClear (self):
        while self.balls:
            ball = self.balls.pop()
            ball.clear()
            ball.hideturtle()
            del ball

    def onSmall (self):
        b = Ball(self,
                 initX=random.randint(0,750/2),
                 initY=750/2,
                 xvel = random.randint(-40,40),
                 size=random.randint(1,4),
                 color=self.colors[(len(self.balls)) % len(self.colors)]
                 )
        self.balls.append(b)
        if not self._ticking: self.tick()

    def onMedium (self):
        b = Ball(self,
                 initX=random.randint(0,750/2),
                 initY=750/2,
                 xvel = random.randint(-40,40),
                 size=random.randint(5,10),
                 color=self.colors[(len(self.balls)) % len(self.colors)]
                 )
        self.balls.append(b)
        if not self._ticking: self.tick()
        if not self._ticking: self.tick()

    def onLarge (self):
        b = Ball(self,
                 initX=random.randint(0,750/2),
                 initY=750/2,
                 xvel = random.randint(-40,40),
                 size=random.randint(11,20),
                 color=self.colors[(len(self.balls)) % len(self.colors)]
                 )
        self.balls.append(b)
        if not self._ticking: self.tick()
        if not self._ticking: self.tick()

    # Animation and mainloop
    def tick (self):
        #print 'Tick!',time.time()
        self._ticking = True
        for b in self.balls:
            b.tick()
        self.root.after(100,self.tick)

        
    def run (self):
        #self.tick()
        self.root.mainloop()

     
World().run()
