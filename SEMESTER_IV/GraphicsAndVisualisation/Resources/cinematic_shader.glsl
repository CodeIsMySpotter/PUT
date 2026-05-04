#version 330 core

#if defined VERTEX_SHADER

// Zmienne z modelu GLTF (nazwy wbudowane w moderngl_window)
in vec3 in_position;
in vec3 in_normal;
in vec2 in_texcoord_0;

// Macierze transformacji
uniform mat4 m_proj;
uniform mat4 m_camera;
uniform mat4 m_model;

out vec3 v_position;
out vec3 v_normal;
out vec2 v_texcoord;

void main() {
    vec4 pos = m_model * vec4(in_position, 1.0);
    gl_Position = m_proj * m_camera * pos;
    
    v_position = pos.xyz;
    // Prawidłowa transformacja wektorów normalnych 
    v_normal = mat3(transpose(inverse(m_model))) * in_normal;
    v_texcoord = in_texcoord_0;
}

#elif defined FRAGMENT_SHADER

in vec3 v_position;
in vec3 v_normal;
in vec2 v_texcoord;

uniform sampler2D texture0; // Tekstura przypisana z pliku .glb
uniform vec3 camera_pos;    // Zmienna, którą będziemy przesyłać z Pythona
uniform vec3 lamp_pos;      // Pozycja wiszącej żarówki
uniform vec3 lamp_color;    // Kolor emitowanego światła

// Krzywa ACES Filmic Tone Mapping - Standard prosto z Hollywood
vec3 ACESFilm(vec3 x) {
    float a = 2.51;
    float b = 0.03;
    float c = 2.43;
    float d = 0.59;
    float e = 0.14;
    return clamp((x * (a * x + b)) / (x * (c * x + d) + e), 0.0, 1.0);
}

out vec4 f_color;

void main() {
    // Pobranie koloru z tekstury
    vec3 albedo = texture(texture0, v_texcoord).rgb;
    vec3 normal = normalize(v_normal);
    vec3 view_dir = normalize(camera_pos - v_position);
    
    // 1. Główne światło punktowe
    vec3 light_vec = lamp_pos - v_position;
    float distance = length(light_vec);
    vec3 L = normalize(light_vec);
    
    // Spadek jasności wraz z odległością (Attenuation)
    float attenuation = 1.0 / (1.0 + 0.03 * distance + 0.008 * (distance * distance));
    
    // Miękkie oświetlenie bryły (Half-Lambert) - światło delikatnie owija się na zacienione strony
    float wrap = dot(normal, L) * 0.5 + 0.5;
    float diff = wrap * wrap;
    
    // Błysk (Specular) - odbicie żarówki na powierzchni obiektów
    vec3 H = normalize(L + view_dir);
    float spec = pow(max(dot(normal, H), 0.0), 32.0); // 32.0 to ostrość błysku
    
    // Połączenie koloru drewna z miękkim światłem i błyskiem
    vec3 key_light = (albedo * diff + vec3(spec * 0.4)) * lamp_color * 35.0 * attenuation;
    
    // 2. Zimne, niebieskie światło konturowe (Rim Light)
    float rim_factor = 1.0 - max(dot(view_dir, normal), 0.0);
    rim_factor = smoothstep(0.7, 1.0, rim_factor); // Wygładzenie i ograniczenie do krawędzi
    vec3 rim_light = rim_factor * vec3(0.1, 0.3, 0.6) * 0.8; // Zmniejszono, by lampka grała główne skrzypce
    
    // 3. Miękkie tło sferyczne (Hemisphere Ambient)
    float hemi = normal.y * 0.5 + 0.5;
    vec3 ambient_up = vec3(0.05, 0.03, 0.01); // Ciepły brąz odbijający się od blatu
    vec3 ambient_down = vec3(0.01, 0.015, 0.03); // Zimny granat w głębokich cieniach
    vec3 ambient = albedo * mix(ambient_down, ambient_up, hemi);
    
    // Złożenie i przepuszczenie przez krzywą kinową (ACES)
    vec3 final_color = key_light + ambient + rim_light;
    final_color = ACESFilm(final_color); 
    final_color = pow(final_color, vec3(1.0 / 2.2)); // Korekcja Gamma
    
    f_color = vec4(final_color, 1.0);
}
#endif