def draw_linked_list(canvas, linked_list):
    current = linked_list.head
    coords = [50, 150]

    while current is not None:
        rect_coords = (coords[0], coords[1], coords[0] + 50, coords[1] + 50)
        canvas.create_rectangle(*rect_coords, fill="black")
        canvas.create_text(coords[0] + 25, coords[1] + 25, text=f"{current.data}", fill="white")

        coords[0] += 100
        current = current.next
