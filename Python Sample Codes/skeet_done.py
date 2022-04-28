import arcade
import math
import random



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
        self.x = 0.0
        self.y = 0.0

class Velocity:
    def __init__(self):
        self.dx = random.uniform(1, 5)
        self.dy = random.uniform(-2, 5)

class FlyingObject:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True

    def advance(self):
        self.center.y += self.velocity.dy
        self.center.x += self.velocity.dx

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        is_off_screen = False

        if self.center.x > SCREEN_WIDTH:
            is_off_screen = True

        elif self.center.y > SCREEN_HEIGHT:
            is_off_screen = True

        return is_off_screen


class Bullet(FlyingObject):
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS

    def draw(self):
        arcade.draw_commands.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED


class Target(FlyingObject):
    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS
        self.center.y = random.uniform(250, 500)

    def draw(self):
        arcade.draw_commands.draw_circle_filled(self.center.x, self.center.y, self.radius, TARGET_COLOR)

    def hit(self):
        
        self.alive = False
        return 1

class Strong(FlyingObject):
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 3)
        self.center.y = random.uniform(250, 500)
        self.lives = 3
        self.radius = TARGET_RADIUS

    def draw(self):
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, arcade.color.PURPLE)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, arcade.color.CARROT_ORANGE, font_size=20)

    def hit(self):
        self.lives -= 1
        hit = 1
        if self.lives == 0:
            self.alive = False
            hit = 5
        return hit


class Safe(FlyingObject):
    def __init__(self):
        super().__init__()
        self.radius = TARGET_SAFE_RADIUS
        self.center.y = random.uniform(250, 500)

    def draw(self):
        arcade.draw_commands.draw_rectangle_filled(self.center.x, self.center.y, 40, 40, TARGET_SAFE_COLOR)

    def hit(self):
        self.alive = False
        return -10


class Rifle:
    
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


class Game(arcade.Window):
    

    def __init__(self, width, height):
        
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        arcade.set_background_color(arcade.color.WHITE)


    def on_draw(self):
        

       
        arcade.start_render()

        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
       
        self.check_collisions()
        self.check_off_screen()

        
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        
        for target in self.targets:
            target.advance()

    def create_target(self):
        
        number = random.randint(1, 3)
        target = None

        if number == 1:
            target = Target()
        elif number == 2:
            target = Strong()
        elif number == 3:
            target = Safe()

        self.targets.append(target)

    def check_collisions(self):
        

        for bullet in self.bullets:
            for target in self.targets:

                
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        
                        bullet.alive = False
                        self.score += target.hit()

                        
        self.cleanup_zombies()

    def cleanup_zombies(self):
        
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
    
        
        angle_radians = math.atan2(x, y)

        
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()