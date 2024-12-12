from assets_loader import *


back_ground_image = load_image("assets/bg.png")


pipe_sprites = {
    "DL" : load_animated_image("assets/D_Ls.png"),
    "LD" : load_animated_image("assets/L_Ds.png"),
    "DR" : load_animated_image("assets/D_Rs.png"),
    "RD" : load_animated_image("assets/R_Ds.png"),
    "DU" : load_animated_image("assets/D_Ts.png"),
    "UD" : load_animated_image("assets/T_Ds.png"),
    "LR" : load_animated_image("assets/L_Rs.png"),
    "RL" : load_animated_image("assets/R_Ls.png"),
    "LU" : load_animated_image("assets/L_Ts.png"),
    "UL" : load_animated_image("assets/T_Ls.png"),
    "UR" : load_animated_image("assets/T_Rs.png"),
    "RU" : load_animated_image("assets/R_Ts.png"),

}

start_pipe_sprites = {
    "D" : load_animated_image("assets/START_D.png"),
    "L" : load_animated_image("assets/START_L.png"),
    "R" : load_animated_image("assets/START_R.png"),
    "U" : load_animated_image("assets/START_T.png")
}

end_pipe_sprites = {
    "D" : load_animated_image("assets/END_D.png"),
    "L" : load_animated_image("assets/END_L.png"),
    "R" : load_animated_image("assets/END_R.png"),
    "U" : load_animated_image("assets/END_T.png")
}

wall_button_image = load_alpha_image("assets/wall.png")
play_button_image = load_alpha_image("assets/play.png")
find_button_image = load_alpha_image("assets/find.png")

font = load_font(None, 30)