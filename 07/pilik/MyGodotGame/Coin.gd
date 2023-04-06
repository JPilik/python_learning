extends Area2D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_body_entered(body):
	body.scale.x += 0.1
	body.scale.y += 0.1
	
	$AudioStreamPlayer.stream = load("res://collectcoin-6075.mp3")
	$AudioStreamPlayer.play()
	self.visible = false
	await $AudioStreamPlayer.finished
	queue_free()
	
	
