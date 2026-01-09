import turtle

# Global bounds
min_x = max_x = min_y = max_y = 0
import turtle

# Global bounds
min_x = max_x = min_y = max_y = 0


def update_bounds():
    global min_x, max_x, min_y, max_y
    x, y = turtle.position()
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)


    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)   