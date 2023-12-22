from time import sleep


FPS = 24


def move_node_to(canvas, node, x, y):
    current_coords = canvas.coords(node.id)
    delx = x - current_coords[0]
    dely = y - current_coords[1]

    for i in range(FPS):
        canvas.move(node.id, delx / FPS, dely / FPS)
        canvas.move(node.data_id, delx / FPS, dely / FPS)
        sleep(1 / FPS)
        canvas.update()

    canvas.coords(node.id, x, y, x + 50, y + 50)
