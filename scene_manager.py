import pygame

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene    
    
    def set_scene(self, scene):
        self.current_scene = scene
        self.current_scene.initialize()
    
    def handle_event(self):
        if self.current_scene:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.current_scene.handle_event(ev)
    
    def update(self):
        if self.current_scene:
            result = self.current_scene.update()

            if result:
                self.current_scene = self.scenes[result]
                self.current_scene.initialize()

    def render(self):
        if self.current_scene:
            self.current_scene.render()

    