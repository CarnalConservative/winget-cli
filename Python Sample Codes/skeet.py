import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15

class Point:

    def __init__(self):
        self.x = float(random.uniform(1,10))
        self.y = float(random.uniform(1,10))

class Velocity:
    def __init__(self):
        self.dx = float(random.uniform(1,10))
        self.dy = float(random.uniform(1,10))


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(float(self.center.x), float(self.center.y), RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, 360-self.angle)

class flying_object:
    def __init__(self):
        self.center = Point
        self.velocity = Velocity
        self.alive = True
        self.radius = BULLET_RADIUS

    
    def advance(self):
        self.velocity.dx = 0
        self.velocity.dy = 0
        self.x += self.velocity.dx
        self.y += self.velocity.dy
        
        def is_off_screen(self,SCREEN_HEIGHT, SCREEN_WIDTH):
        if Point.x and Point.y < SCREEN_WIDTH and SCREEN_HEIGHT:
            self.alive = True            
        else:
            Game.check_off_screen()

class Bullet(flying_object):
    
    def __init__(self):
        super().__init__():
        


        
    
    def draw(self):
        arcade.draw_ellipse_filled(float(self.center.x), float(self.center.y), BULLET_RADIUS, BULLET_RADIUS, BULLET_COLOR, 0, -1)
    
    def fire(self,angle):
        Bullet.draw(angle)

class Target(flying_object):
    def __init__(self):
        super().__init__():

    
    def draw(self):
        arcade.draw_ellipse_filled(float(self.center.x), float(self.center.y), TARGET_RADIUS, TARGET_RADIUS, TARGET_COLOR, 0, -1)
    def is_off_screen(self,SCREEN_HEIGHT, SCREEN_WIDTH):
        if Target.x and Target.y < SCREEN_HEIGHT and SCREEN_WIDTH:
            pass
        else:
            Game.check_off_screen()


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []
        self.targets = []
                
        # XXXTODO: Create a list for your targets (similar to the above bullets)


        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw(self)

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        for target in self.targets:
            Target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        Target.draw(self)

        # TODO: Decide what type of target to create and append it to the list

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = Bullet.radius + Target.radius

                    if (abs(Bullet.x - Target.x) < too_close and
                                abs(Bullet.y - Target.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += Target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self,x: float,y: float,button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.

        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()