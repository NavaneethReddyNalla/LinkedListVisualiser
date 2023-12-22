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
    canvas.coords(node.data_id, x + 25, y + 25)


def shift_list(canvas, linked_list_start, step=1):
    step_size = 100
    delx = step * step_size
    curr = None

    for i in range(FPS):
        curr = linked_list_start

        while curr:
            canvas.move(curr.id, delx / FPS, 0)
            canvas.move(curr.data_id, delx / FPS, 0)
            curr = curr.next

        sleep(1 / FPS)
        canvas.update()

    while curr:
        current_coords = canvas.coords(curr.id)
        text_coords = canvas.coords(curr.data_id)
        current_coords[0] += step_size
        current_coords[3] += step_size
        text_coords[0] += step_size

        canvas.coords(curr.id, *current_coords)
        canvas.coords(curr.data_id, *text_coords)
