extends CharacterBody2D

func _physics_process(delta):
  
	velocity = Vector2()
  
	if Input.is_key_pressed(KEY_LEFT) or Input.is_key_pressed(KEY_A):
		velocity = update_velocity(velocity, -1, 0)
	if Input.is_key_pressed(KEY_RIGHT) or Input.is_key_pressed(KEY_D):
		velocity = update_velocity(velocity, 1, 0)
	if Input.is_key_pressed(KEY_UP) or Input.is_key_pressed(KEY_W):
		velocity = update_velocity(velocity, 0, -1)
	if Input.is_key_pressed(KEY_DOWN) or Input.is_key_pressed(KEY_S):
		velocity = update_velocity(velocity, 0, 1)
	
	velocity *= 50
	move_and_slide()
	
func update_velocity(temp_velocity, x, y):
	temp_velocity.x += x
	temp_velocity.y += y
	
	if $AudioStreamPlayer.playing == false:
		$AudioStreamPlayer.stream = load("res://01-footstep.ogg")
		$AudioStreamPlayer.play()
	return temp_velocity
