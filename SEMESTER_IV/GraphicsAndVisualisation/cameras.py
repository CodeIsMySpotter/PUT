import glm
import math

class StaticTopView:
    def __init__(self, height=15.0):
        self.position = glm.vec3(0.0, height, 0.0)
        # Patrząc pionowo w dół wzdłuż osi Y, wektor "up" kamery musi być ustawiony wzdłuż osi Z
        self.view_matrix = glm.lookAt(self.position, glm.vec3(0.0, 0.0, 0.0), glm.vec3(0.0, 0.0, -1.0))

    def update(self, time, frame_time, **kwargs):
        pass # Statyczna kamera nie wymaga aktualizacji stanu

    @property
    def view(self):
        return self.view_matrix

    @property
    def pos(self):
        return self.position


class DynamicMovementView:
    def __init__(self, radius=50.0, height=8.0, speed=0.4):
        self.radius = radius
        self.height = height
        self.speed = speed
        self.position = glm.vec3(0.0, height, radius)
        self.view_matrix = glm.lookAt(self.position, glm.vec3(0.0, 0.0, 0.0), glm.vec3(0.0, 1.0, 0.0))

    def update(self, time, frame_time, **kwargs):
        # Wyliczenie współrzędnych okręgu na podstawie trygonometrii i czasu
        x = math.sin(time * self.speed) * self.radius
        z = math.cos(time * self.speed) * self.radius
        self.position = glm.vec3(x, self.height, z)
        
        # Ciągła aktualizacja orientacji obiektywu w stronę centrum planszy
        self.view_matrix = glm.lookAt(self.position, glm.vec3(0.0, 0.0, 0.0), glm.vec3(0.0, 1.0, 0.0))

    @property
    def view(self):
        return self.view_matrix

    @property
    def pos(self):
        return self.position


class FreeMovementView:
    def __init__(self, start_pos=(0.0, 8.0, 12.0), speed=10.0):
        self.position = glm.vec3(*start_pos)
        # Kamera na start skierowana jest delikatnie w dół w stronę centrum
        self.front = glm.normalize(glm.vec3(0.0, 0.0, 0.0) - self.position)
        self.up = glm.vec3(0.0, 1.0, 0.0)
        self.speed = speed
        
        # Wyliczenie początkowych kątów Yaw i Pitch na podstawie początkowego wektora front
        # Zabezpieczamy wartość Y przed wyjściem poza przedział [-1, 1] dla math.asin
        y_clamped = max(-1.0, min(1.0, self.front.y))
        self.yaw = math.degrees(math.atan2(self.front.z, self.front.x))
        self.pitch = math.degrees(math.asin(y_clamped))
        
        self._update_view_matrix()

    def mouse_look(self, dx, dy, sensitivity=0.15):
        self.yaw += dx * sensitivity
        self.pitch -= dy * sensitivity # Odwracamy oś Y (ruch myszką w dół to mniejsze pitch)

        # Zabezpieczenie przed tzw. Gimbal Lock (wywróceniem kamery do góry nogami)
        if self.pitch > 89.0: self.pitch = 89.0
        if self.pitch < -89.0: self.pitch = -89.0

        # Przeliczenie nowego wektora kierunkowego front z użyciem trygonometrii
        front = glm.vec3()
        front.x = math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        front.y = math.sin(math.radians(self.pitch))
        front.z = math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        self.front = glm.normalize(front)
        
        self._update_view_matrix()

    def _update_view_matrix(self):
        self.view_matrix = glm.lookAt(self.position, self.position + self.front, self.up)

    def update(self, time, frame_time, keys_pressed=None, wnd_keys=None, **kwargs):
        if keys_pressed is not None and wnd_keys is not None:
            velocity = self.speed * frame_time
            right = glm.normalize(glm.cross(self.front, self.up))
            
            # Obsługa wektorów ruchu (WASD dla bocznych, Q/E góra/dół)
            if wnd_keys.W in keys_pressed: self.position += self.front * velocity
            if wnd_keys.S in keys_pressed: self.position -= self.front * velocity
            if wnd_keys.A in keys_pressed: self.position -= right * velocity
            if wnd_keys.D in keys_pressed: self.position += right * velocity
            if wnd_keys.SPACE in keys_pressed: self.position += self.up * velocity
            if wnd_keys.LEFT_SHIFT in keys_pressed: self.position -= self.up * velocity

            if keys_pressed: # Aktualizuj matrycę tylko gdy nastąpił ruch
                self._update_view_matrix()

    @property
    def view(self):
        return self.view_matrix

    @property
    def pos(self):
        return self.position