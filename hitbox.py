
import pygame
import spritesheet

#clock
clock = pygame.time.Clock()
dt = 0
running = True

pygame.init()
SCREEN_WIDTH= 1000
SCREEN_HEIGHT= 750

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Spritesheets")

sprite_sheet_image = pygame.image.load('background/entire_background.png').convert_alpha()
c_sprite_sheet_image= pygame.image.load('characters/DRAGON_DONE.png').convert_alpha()
c_sprite_sheet_image_2= pygame.image.load('characters/DRAGON_DONE.png').convert_alpha()
platform_frame_1 = pygame.image.load('platform/platform_frame1.png').convert_alpha()
platform_frame_2 = pygame.image.load('platform/platform_frame2.png').convert_alpha()
character_1= pygame.image.load('characters/dragon_still.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
c_sprite_sheet = spritesheet.SpriteSheet(c_sprite_sheet_image)
c_sprite_sheet_2= spritesheet.SpriteSheet(c_sprite_sheet_image_2)
BG = (20, 50, 50)
BLACK=(0,0,0)

#create animation list
#frame, width, height

last_update = pygame.time.get_ticks()



#background animations
animation_list =[]
#8 is just rain 5 is lightning 
animation_steps= [8,5]
frame=0
step_counter=0
#action 0 is rain 1 is lighting
action = 0
animation_cooldown = 100

for animation in animation_steps:
    temp_img_list =[]
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 1000, 750, BLACK))
        step_counter +=1
    animation_list.append(temp_img_list)

#character animations
#player 1
c_animation_list=[]
c_step_counter=0
c_frame=0
character_animation_steps=[4,11,8,4,11,8]
idle_right=0
idle_left=3
air_blast_right=1
air_blast_left=4
fly_right=2
fly_left=5
c_action = 0
c_animation_cooldown = 100
c_last_update = pygame.time.get_ticks()
for animation in character_animation_steps:
    temp_img_list =[]
    for _ in range(animation):
        temp_img_list.append(c_sprite_sheet.get_image(c_step_counter, 150, 150, BLACK))
        c_step_counter +=1
    c_animation_list.append(temp_img_list)
#player 2
c_animation_list_2=[]
c_step_counter_2=0
c_frame_2=0
character_animation_steps_2=[4,11,8,4,11,8]
idle_right_2=0
idle_left_2=3
air_blast_right_2=1
air_blast_left_2=4
fly_right_2=2
fly_left_2=5
c_action_2= 0
c_animation_cooldown_2= 100
c_last_update_2 = pygame.time.get_ticks()
for animation in character_animation_steps_2:
    temp_img_list =[]
    for _ in range(animation):
        temp_img_list.append(c_sprite_sheet_2.get_image(c_step_counter_2, 150, 150, BLACK))
        c_step_counter_2+=1
    c_animation_list_2.append(temp_img_list)
    



gravity=1
red='red'
green='green'

#player 1
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_velocity_y=0
facing_right=True
air_blast=False
fly=True
flapping=False
jumps=0
key_was_pressed=False
#player 2
player_pos_2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_velocity_y_2=0
facing_right_2=True
air_blast_2=False
fly_2=True
flapping_2=False
jumps_2=0
key_was_pressed_2=False


#hitboxs

#player 1
player_hitbox=[]
if facing_right and not fly:
    player_hitbox.append(pygame.Rect(player_pos.x-25,player_pos.y-90,55,90,))
    player_hitbox.append(pygame.Rect(player_pos.x+20,player_pos.y-110,40,30,))
if not facing_right and not fly:
    player_hitbox.append(pygame.Rect(player_pos.x-20,player_pos.y-90,55,90,))
    player_hitbox.append(pygame.Rect(player_pos.x-45,player_pos.y-110,40,30,))
if fly and facing_right:
    player_hitbox.append(pygame.Rect(player_pos.x-30,player_pos.y-120,50,120,))
    player_hitbox.append(pygame.Rect(player_pos.x+15,player_pos.y-120,40,30,))
if fly and not facing_right:
    player_hitbox.append(pygame.Rect(player_pos.x-20,player_pos.y-120,50,120,))
    player_hitbox.append(pygame.Rect(player_pos.x-55,player_pos.y-120,40,30,))


#player 2
player_2_hitbox=[]
if facing_right_2 and not fly_2:
    player_2_hitbox.append(pygame.Rect(player_pos_2.x-25,player_pos_2.y-90,55,90,))
    player_2_hitbox.append(pygame.Rect(player_pos_2.x+20,player_pos_2.y-110,40,30,))
if not facing_right_2 and not fly_2:
    player_2_hitbox.append(pygame.Rect(player_pos_2.x-20,player_pos_2.y-90,55,90,))
    player_2_hitbox.append(pygame.Rect(player_pos_2.x-45,player_pos_2.y-110,40,30,))
if fly_2 and facing_right_2:
    player_2_hitbox.append(pygame.Rect(player_pos_2.x-30,player_pos_2.y-120,50,120,))
    player_2_hitbox.append(pygame.Rect(player_pos_2.x+15,player_pos_2.y-120,40,30,))
if fly_2 and not facing_right_2:
    player_2_hitbox.append(pygame.Rect(player_pos_2.x-20,player_pos_2.y-120,50,120,))
    player_2_hitbox.append(pygame.Rect(player_pos_2.x-55,player_pos_2.y-120,40,30,))


#platform
platform= pygame.Rect(SCREEN_WIDTH*0.15,SCREEN_HEIGHT*0.8,SCREEN_WIDTH*0.7,SCREEN_HEIGHT*0.05)
#lighting
frames = 0
lighting_happening=True
#grass
grass_change=1


while running:
    frames += 1
    screen.blit(animation_list[action][frame], (0, 0))
    #player 1 animations
    if not facing_right and not fly:
        screen.blit(c_animation_list[c_action][c_frame], (player_pos.x-90, player_pos.y-135))
    if facing_right and not fly:
        screen.blit(c_animation_list[c_action][c_frame], (player_pos.x-50, player_pos.y-135))
    if fly and facing_right:
        screen.blit(c_animation_list[c_action][c_frame], (player_pos.x-75, player_pos.y-135))
    if fly and not facing_right:
        screen.blit(c_animation_list[c_action][c_frame], (player_pos.x-75, player_pos.y-135))
    
    #player 2 animations
    if not facing_right_2 and not fly_2:
        screen.blit(c_animation_list_2[c_action_2][c_frame_2], (player_pos_2.x-90, player_pos_2.y-135))
    if facing_right_2 and not fly_2:
        screen.blit(c_animation_list_2[c_action_2][c_frame_2], (player_pos_2.x-50, player_pos_2.y-135))
    if fly_2 and facing_right_2:
        screen.blit(c_animation_list_2[c_action_2][c_frame_2], (player_pos_2.x-75, player_pos_2.y-135))
    if fly_2 and not facing_right_2:
        screen.blit(c_animation_list_2[c_action_2][c_frame_2], (player_pos_2.x-75, player_pos_2.y-135))
    
    #background animation
    current_time =pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame+=1
        last_update=current_time
        if frame>=len(animation_list[action]):
            frame=0

    #character animation
    if current_time - c_last_update >= c_animation_cooldown:
        c_frame+=1
        c_last_update=current_time
        if c_frame>=len(c_animation_list[c_action]):
            c_frame=0
    if current_time - c_last_update_2 >= c_animation_cooldown_2:
        c_frame_2+=1
        c_last_update_2=current_time
        if c_frame_2>=len(c_animation_list_2[c_action_2]):
            c_frame_2=0
            
       
    
    #hitbox
    

    #player 1
    if facing_right and not fly:
        pygame.draw.rect(screen,red , pygame.Rect(player_pos.x-25,player_pos.y-90,55,90,),2)
        pygame.draw.rect(screen,red , pygame.Rect(player_pos.x+20,player_pos.y-110,40,30,),2)
    if not facing_right and not fly:
        pygame.draw.rect(screen,green , pygame.Rect(player_pos.x-20,player_pos.y-90,55,90,),2)
        pygame.draw.rect(screen,green , pygame.Rect(player_pos.x-45,player_pos.y-110,40,30,),2)
    if fly and facing_right:
        pygame.draw.rect(screen,red , pygame.Rect(player_pos.x-30,player_pos.y-120,50,120,),2)
        pygame.draw.rect(screen,red , pygame.Rect(player_pos.x+15,player_pos.y-120,40,30,),2)
    if fly and not facing_right:
        pygame.draw.rect(screen,green , pygame.Rect(player_pos.x-20,player_pos.y-120,50,120,),2)
        pygame.draw.rect(screen,green , pygame.Rect(player_pos.x-55,player_pos.y-120,40,30,),2)   
    
    #player 2
    if facing_right_2 and not fly_2:
        pygame.draw.rect(screen,red , pygame.Rect(player_pos_2.x-25,player_pos_2.y-90,55,90,),2)
        pygame.draw.rect(screen,red , pygame.Rect(player_pos_2.x+20,player_pos_2.y-110,40,30,),2)
    if not facing_right_2 and not fly_2:
        pygame.draw.rect(screen,green , pygame.Rect(player_pos_2.x-20,player_pos_2.y-90,55,90,),2)
        pygame.draw.rect(screen,green , pygame.Rect(player_pos_2.x-45,player_pos_2.y-110,40,30,),2)
    if fly_2 and facing_right_2:
        pygame.draw.rect(screen,red , pygame.Rect(player_pos_2.x-30,player_pos_2.y-120,50,120,),2)
        pygame.draw.rect(screen,red , pygame.Rect(player_pos_2.x+15,player_pos_2.y-120,40,30,),2)
    if fly_2 and not facing_right_2:
        pygame.draw.rect(screen,green , pygame.Rect(player_pos_2.x-20,player_pos_2.y-120,50,120,),2)
        pygame.draw.rect(screen,green , pygame.Rect(player_pos_2.x-55,player_pos_2.y-120,40,30,),2)  
        

    #hitbox of position
    pygame.draw.rect(screen,green , pygame.Rect(player_pos.x,player_pos.y,10,10,)) 

    
    #grass animation
    if grass_change%2==0:
        screen.blit(platform_frame_2,(platform.topleft))
    if grass_change%2==1:
        screen.blit(platform_frame_1,(platform.topleft))
    

    #gravity
    
    #player 1
    if player_velocity_y>-36:
        player_velocity_y-=gravity
    player_pos.y-=player_velocity_y
    if  player_pos.y>platform.top and player_pos.y<platform.bottom and player_pos.x>platform.left and player_pos.x<platform.right:
        player_velocity_y=0
        player_pos.y=platform.top
    
    #player 2
    if player_velocity_y_2>-36:
        player_velocity_y_2-=gravity
    player_pos_2.y-=player_velocity_y_2
    if  player_pos_2.y>platform.top and player_pos_2.y<platform.bottom and player_pos_2.x>platform.left and player_pos_2.x<platform.right:
        player_velocity_y_2=0
        player_pos_2.y=platform.top
    
        
    #respawn
    
    #player 1
    if player_pos.y-100>SCREEN_HEIGHT:
        jumps=0
        player_pos.x=SCREEN_WIDTH/2
        player_pos.y=SCREEN_HEIGHT/2
    #player 2
    if player_pos_2.y-100>SCREEN_HEIGHT:
        jumps=0
        player_pos_2.x=SCREEN_WIDTH/2
        player_pos_2.y=SCREEN_HEIGHT/2

    #key inputs
    keys = pygame.key.get_pressed()

    #player 1
    if keys[pygame.K_w]:
        if not air_blast:
            if player_pos.y==platform.top:
                key_was_pressed=True
                c_frame=2
                player_velocity_y=25

            if fly and jumps<2 and not key_was_pressed:
                flapping=True
                key_was_pressed=True
                jumps+=1                
                c_frame=2                
                player_velocity_y=25
    if not keys[pygame.K_w]:
        key_was_pressed=False
    if keys[pygame.K_e] and not fly and not flapping and not air_blast:
        c_frame=0
        air_blast=True
    if keys[pygame.K_s]:
        if player_pos.y>=SCREEN_HEIGHT*0.781 and player_pos.x<platform.right and player_pos.x>platform.left:
                player_pos.y += 0 * dt
        else:
            player_pos.y += 15
    if keys[pygame.K_a] and not air_blast:
        facing_right=False
        player_pos.x -= 10
    if keys[pygame.K_d] and not air_blast:
        facing_right=True
        player_pos.x += 10
    
    #player 2
    if keys[pygame.K_i]:
        if not air_blast_2:
            if player_pos_2.y==platform.top:
                key_was_pressed_2=True
                c_frame_2=2
                player_velocity_y_2=25

            if fly_2 and jumps_2<2 and not key_was_pressed_2:
                flapping_2=True
                key_was_pressed_2=True
                jumps_2+=1                
                c_frame_2=2                
                player_velocity_y_2=25
    if not keys[pygame.K_i]:
        key_was_pressed_2=False
    if keys[pygame.K_o] and not fly_2 and not flapping_2 and not air_blast_2:
        c_frame_2=0
        air_blast_2=True
    if keys[pygame.K_k]:
        if player_pos_2.y>=SCREEN_HEIGHT*0.781 and player_pos_2.x<platform.right and player_pos_2.x>platform.left:
                player_pos_2.y += 0 * dt
        else:
            player_pos_2.y += 15
    if keys[pygame.K_j] and not air_blast_2:
        facing_right_2=False
        player_pos_2.x -= 10
    if keys[pygame.K_l] and not air_blast_2:
        facing_right_2=True
        player_pos_2.x += 10
    #fly
        
    #player 1
    if player_pos.y<platform.top or player_pos.y>platform.bottom or player_pos.x<platform.left or player_pos.x>platform.right:
        fly=True
    if flapping:
        c_animation_cooldown=25
        if facing_right:
            c_action=fly_right
        if not facing_right:
            c_action=fly_left
        if c_frame==7:
            flapping=False
    if fly and not flapping:
        if facing_right:
            c_frame=0
            c_action=fly_right
        else:
            c_frame=0
            c_action=fly_left
    #player 2 
    if player_pos_2.y<platform.top or player_pos_2.y>platform.bottom or player_pos_2.x<platform.left or player_pos_2.x>platform.right:
        fly_2=True
    if flapping_2:
        c_animation_cooldown_2=25
        if facing_right_2:
            c_action_2=fly_right_2
        if not facing_right_2:
            c_action_2=fly_left_2
        if c_frame_2==7:
            flapping_2=False
    if fly_2 and not flapping_2:
        if facing_right_2:
            c_frame_2=0
            c_action_2=fly_right_2
        else:
            c_frame_2=0
            c_action_2=fly_left_2
    #stop flying
    #player 1
    if player_pos.y==platform.top and player_pos.x<platform.right and player_pos.x>platform.left:
        jumps=0
        if fly or flapping:
            c_animation_cooldown=100
            flapping=False
            fly=False
            c_frame=0
    #player 2
    if player_pos_2.y==platform.top and player_pos_2.x<platform.right and player_pos_2.x>platform.left:
        jumps_2=0
        if fly_2 or flapping_2:
            c_animation_cooldown_2=100
            flapping_2=False
            fly_2=False
            c_frame_2=0     

    #prevent glitches
    if air_blast and fly:
        air_blast=False
    if air_blast_2 and fly_2:
        air_blast_2=False

    #air blast animation
        
    #player 1
    if air_blast:
        c_animation_cooldown=50
        if facing_right:
            c_action=air_blast_right
        if not facing_right:
            c_action=air_blast_left
        if c_frame==10:
            c_animation_cooldown=100
            air_blast=False
            c_frame=0
    #player 2
    if air_blast_2:
        c_animation_cooldown_2=50
        if facing_right_2:
            c_action_2=air_blast_right_2
        if not facing_right_2:
            c_action_2=air_blast_left_2
        if c_frame_2==10:
            c_animation_cooldown_2=100
            air_blast_2=False
            c_frame_2=0
    #idle animation
    
    #player 1
    if not air_blast and not fly and not flapping:
        if facing_right:
            c_action=idle_right
        else:
            c_action=idle_left
    #player 2
    if not air_blast_2 and not fly_2 and not flapping_2:
        if facing_right_2:
            c_action_2=idle_right_2
        else:
            c_action_2=idle_left_2
    
    #background lighting animation
    if lighting_happening and frame>3:
            lighting_happening=False
            frame=0
            action=0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(60) / 1000
    #% 30 = seconds
    if (frames/60)%5==0:
        lighting_happening=True
        frame=0
        action=1
    if (frames/60)%1==0:
        grass_change+=1
pygame.quit()