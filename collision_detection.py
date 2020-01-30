import math
import player_module
import enemy_module


#Methode für die CollisionDetection

def collision_objects(obj1, obj2):
    #check if there is collision between 2 objects
    obj1_top = obj1.position[1] -1
    obj1_bottom = obj1.position[1] + obj1.hitbox[1] +1
    obj1_left = obj1.position[0] -1
    obj1_right = obj1.position[0] + obj1.hitbox[0] +1

    obj2_top = obj2.position[1]
    obj2_bottom = obj2.position[1] + obj2.hitbox[1]
    obj2_left = obj2.position[0]
    obj2_right = obj2.position[0] + obj2.hitbox[0]

    #Check where object 1 collides
    hit_bottom = obj1_bottom > obj2_top
    hit_top = obj1_top < obj2_bottom
    hit_left = obj1_left < obj2_right
    hit_right = obj1_right > obj2_left
    

    if hit_bottom and hit_top and hit_left and hit_right:
        #got hit
        hit_direction = "Bottom"
        #check if below or above
        if obj1_top < obj2_bottom and obj1_bottom < obj2_bottom:
            #obj1 is above obj2
            if obj1_left < obj2_right and obj1_right > obj2_right:
                #is on Right Site (Left Collision)
                if math.fabs(obj1_left - obj2_right) > math.fabs(obj1_bottom - obj2_top):
                    #is Bottom
                    return "Bottom"
                else:
                    #is LEFT
                    return "Left"
            else:
                #is on Left Site (Right Collision)
                if math.fabs(obj1_right - obj2_left) > math.fabs(obj1_bottom - obj2_top):
                    #is Bottom
                    return "Bottom"
                else:
                    #is RIGHT
                    return "Right"
        else:
            #obj1 is below obj2
            if obj1_left < obj2_right and obj1_right > obj2_right:
                #is on Right Site (Left Collision)
                if math.fabs(obj1_left - obj2_right) > math.fabs(obj1_top - obj2_bottom):
                    #is TOP
                    return "Top"
                else:
                    #is LEFT
                    return "Left"
            else:
                #is on Left Site (Right Collision)
                if math.fabs(obj1_right - obj2_left) > math.fabs(obj1_top - obj2_bottom):
                    #is TOP
                    return "Top"
                else:
                    #is RIGHT
                    return "Right"
            
    else:
        return "None"


    
