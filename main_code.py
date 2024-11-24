import pygame
import random

pygame.init()

window = pygame.display.set_mode((800,600))
background = pygame.image.load('forest_background_image.jpeg')
background = pygame.transform.smoothscale(background, window.get_size())
pygame.display.set_caption("Mushroom simulation game!")
clock = pygame.time.Clock()

window.blit(background, (0, 0))

pygame.display.flip()

mushroom1_stages = [pygame.image.load("mushroom1_stage1.png"), pygame.image.load("mushroom1_stage2.png"), pygame.image.load("mushroom1_stage3.png")]
mushroom2_stages = [pygame.image.load("mushroom2_stage1.png"), pygame.image.load("mushroom2_stage2.png"), pygame.image.load("mushroom2_stage3.png")]
mushroom3_stages = [pygame.image.load("mushroom3_stage1.png"), pygame.image.load("mushroom3_stage2.png"), pygame.image.load("mushroom3_stage3.png")]

food_image = pygame.image.load("mushroom_food.png")
water_image = pygame.image.load("water_drop.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    class mushroom_1():
        def __init__(self, name, growth_stage, water_level, food_level, mushroom1_image):
            self.growth = 1
            self.x = 300
            self.y = 500
            pygame.display.set_mode(self.x,self.y)
            self.food_level = 0
            self.water_level = 0
            self.isAlive = True


            def grow():
                if self.growth < 3:
                    self.growth += 1

            def regress():
                if self.growth > 1:
                    self.growth -= 1

                else:
                    isAlive = False

            if self.growth == 1:
                self.image = mushroom1_stages[0]

            if self.growth == 2:
                self.image = mushroom1_stages[1]

            if self.growth == 3:
                self.image = mushroom1_stages[2]

            if self.growth == 0:
                isAlive = False

                
    class items():
        def __init__(self, x, y, item_type):
            self.x = random.randint(40, 700)
            self.y = random.randint(40, 500)
            self.type = item_type

        def spawn(self):
            if self.type == "food":
                window.blit(food_image, (self.x,self.y))

            elif self.type == "water":
                window.blit(water_image, (self.x,self.y))


pygame.quit()