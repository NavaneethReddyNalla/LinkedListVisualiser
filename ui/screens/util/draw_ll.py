from ui.styles import *


def draw_node(canvas, node, coords):
    arrow_coords = [coords[0] + 50, coords[1] + 25, coords[0] + 100, coords[1] + 25]
    rect_coords = (coords[0], coords[1], coords[0] + 50, coords[1] + 50)
    node.id = canvas.create_rectangle(*rect_coords, fill=PRIMARY_COLORS["node"])
    node.data_id = canvas.create_text(coords[0] + 25, coords[1] + 25, text=f"{node.data}", fill=PRIMARY_COLORS["data"])
    node.arrow_id = canvas.create_line(*arrow_coords, arrow="last", arrowshape=(7, 10, 5))


def un_draw_node(canvas, node):
    canvas.delete(node.id, node.data_id, node.arrow_id)

# This function became useless after completing the animation with only one node
# def draw_linked_list(canvas, linked_list):
#     current = linked_list.head
#     coords = [50, 150]
#
#     while current is not None:
#         rect_coords = (coords[0], coords[1], coords[0] + 50, coords[1] + 50)
#         canvas.create_rectangle(*rect_coords, fill="black")
#         canvas.create_text(coords[0] + 25, coords[1] + 25, text=f"{current.data}", fill="white")
#
#         coords[0] += 100
#         current = current.next
