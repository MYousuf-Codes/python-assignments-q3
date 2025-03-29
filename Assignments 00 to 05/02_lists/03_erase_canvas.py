import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Eraser on Canvas")
    
    # Canvas dimensions
    canvas_width = 600
    canvas_height = 600
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Grid configuration
    rows = 10
    cols = 10
    cell_width = canvas_width // cols
    cell_height = canvas_height // rows

    # Create grid of blue cells and store their IDs
    cell_ids = []
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            cell = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
            cell_ids.append(cell)

    # Create the eraser rectangle (a bit larger than one cell for demonstration)
    eraser_width = cell_width * 2
    eraser_height = cell_height * 2
    # Initial position of eraser (top left corner)
    eraser = canvas.create_rectangle(0, 0, eraser_width, eraser_height, outline="red", width=3)

    def on_drag(event):
        # Center the eraser on the mouse pointer
        new_x1 = event.x - eraser_width // 2
        new_y1 = event.y - eraser_height // 2
        new_x2 = new_x1 + eraser_width
        new_y2 = new_y1 + eraser_height

        # Update the eraser rectangle's position
        canvas.coords(eraser, new_x1, new_y1, new_x2, new_y2)

        # Find all items overlapping with the eraser rectangle
        overlapping_items = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)
        for item in overlapping_items:
            # Check if the overlapping item is one of our grid cells
            if item in cell_ids:
                canvas.itemconfig(item, fill="white")

    # Bind the left mouse button drag to the canvas
    canvas.bind("<B1-Motion>", on_drag)

    root.mainloop()

if __name__ == '__main__':
    main()
