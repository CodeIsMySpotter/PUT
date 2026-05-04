import moderngl_window as mglw
import moderngl
import chess.pgn
import glm
import numpy as np
import math
from cameras import StaticTopView, DynamicMovementView, FreeMovementView

class ChessAnimationApp(mglw.WindowConfig):
    gl_version = (3, 3) # Używamy OpenGL 3.3 Core (wspiera nowoczesne shadery)
    title = "Szachowa Animacja 3D"
    window_size = (1280, 720)
    resource_dir = 'Resources' # Wskazanie folderu na modele i tekstury

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Włączenie testowania głębokości i ukrywania niewidocznych ścianek.
        # Dzięki temu model będzie solidny i trójkąty z tyłu nie będą przebijać do przodu.
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        
        # 1. Konfiguracja kamer
        self.projection = glm.perspective(glm.radians(45.0), self.aspect_ratio, 0.1, 100.0)
        
        self.cameras = {
            'static': StaticTopView(height=18.0),
            'dynamic': DynamicMovementView(radius=25.0, height=25.0, speed=0.3),
            'free': FreeMovementView(start_pos=(0.0, 8.0, 12.0), speed=12.0)
        }
        self.active_camera = 'dynamic'  # Animację możemy zacząć od krążącej
        self.pressed_keys = set()       # Śledzi klawisze wciśnięte w danym momencie (np. W, A, S, D)

        # 2. Wczytanie czystego modelu planszy szachowej
        self.chessboard = self.load_scene('chessboard.glb')

        # Wczytanie naszego filmowego shadera
        self.cinematic_prog = self.load_program('cinematic_shader.glsl')
        
        # Podmiana domyślnego shadera w każdej geometrii planszy
        for mesh in self.chessboard.meshes:
            mesh.prog = self.cinematic_prog
        
        # 3. Ustawienia światła zawieszonego nad planszą
        self.lamp_pos = glm.vec3(0.0, 12.0, 0.0)
        self.lamp_color = (1.0, 0.9, 0.8) # Neutralne, lekko ciepłe światło z góry
        
        if 'lamp_pos' in self.cinematic_prog:
            self.cinematic_prog['lamp_pos'].value = tuple(self.lamp_pos)
        if 'lamp_color' in self.cinematic_prog:
            self.cinematic_prog['lamp_color'].value = self.lamp_color

        # 3. Tu przygotujesz logikę szachową za pomocą python-chess

    def on_key_event(self, key, action, modifiers):
        # Kiedy wciskamy klawisz, dodajemy go do "zbioru" (set)
        if action == self.wnd.keys.ACTION_PRESS:
            self.pressed_keys.add(key)
            
            # Skróty klawiszowe 1, 2, 3 do natychmiastowego zmieniania trybu kamery
            if key == self.wnd.keys.NUMBER_1:
                self.active_camera = 'static'
                self.wnd.mouse_exclusivity = False
            elif key == self.wnd.keys.NUMBER_2:
                self.active_camera = 'dynamic'
                self.wnd.mouse_exclusivity = False
            elif key == self.wnd.keys.NUMBER_3:
                self.active_camera = 'free'
                self.wnd.mouse_exclusivity = True # Blokuje kursor w oknie jak w grach FPS
                
            # Narzędzie deweloperskie (P jak Print) do pobrania idealnych koordynatów dla żarówki!
            elif key == self.wnd.keys.P:
                cam = self.cameras[self.active_camera]
                print("\n--- SKOPIUJ TO DO KODU (LINIJKA 47 i 48) ---")
                print(f"self.lamp_pos = glm.vec3({cam.pos.x:.2f}, {cam.pos.y:.2f}, {cam.pos.z:.2f})")

        # Gdy odpuszczamy, natychmiast usuwamy, żeby ruch (WASD) się zatrzymał
        elif action == self.wnd.keys.ACTION_RELEASE:
            if key in self.pressed_keys:
                self.pressed_keys.remove(key)

    def on_mouse_position_event(self, x, y, dx, dy):
        # Gdy ruszamy myszą, a aktywna jest wolna kamera, obracamy widok
        if self.active_camera == 'free':
            self.cameras['free'].mouse_look(dx, dy)

    def on_render(self, time, frame_time):
        # Pobranie aktywnej kamery z naszego słownika i jej zaktualizowanie
        cam = self.cameras[self.active_camera]
        cam.update(time, frame_time, keys_pressed=self.pressed_keys, wnd_keys=self.wnd.keys)

        # Czyszczenie ekranu - jeszcze ciemniejsze tło mocniej podkreśli światło konturowe
        self.ctx.clear(0.02, 0.02, 0.03)
        
        # Przekazanie pozycji kamery do shadera (wymagane przez efekt Rim Light)
        if 'camera_pos' in self.cinematic_prog:
            self.cinematic_prog['camera_pos'].value = tuple(cam.pos)
            
        # Rysowanie planszy
        self.chessboard.draw(projection_matrix=self.projection.to_bytes(), camera_matrix=cam.view.to_bytes())

if __name__ == '__main__':
    mglw.run_window_config(ChessAnimationApp)