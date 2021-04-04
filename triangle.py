import tkinter
import random
import time
import threading
import winsound


class Item:
    def __init__(self, x1, y1, x2, y2, num, g):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.num = num
        self.g = g


def shuffle():
    time.sleep(1)
    for x in range(item_count):
        dup = items[x]
        rand = random.randint(0, item_count-1)
        items[x] = items[rand]
        items[rand] = dup

        c.delete(items[x].g)
        c.delete(items[rand].g)

        x1 = items[x].x1
        x2 = items[x].x2

        items[x].x1 = dup.x1
        items[x].x2 = dup.x2

        items[rand].x1 = x1
        items[rand].x2 = x2

        items[x].g = c.create_rectangle(items[x].x1, items[x].y1, items[x].x2, items[x].y2, outline="gray", fill="white")
        items[rand].g = c.create_rectangle(items[rand].x1, items[rand].y1, items[rand].x2, items[rand].y2, outline="gray", fill="white")
        time.sleep(0.005)
    time.sleep(1)
    
    # random sort each shuffle
    # if random.randint(0, 1):
        # insertion_sort()
    # else:
        # bubble_sort()
    insertion_sort()
        
    threading.Thread(target=shuffle).start()


def insertion_sort():
    for i in range(1, len(items)):

        key = items[i]
        j = i - 1
        while j >= 0 and key.num < items[j].num:
            dup = items[j + 1]

            items[j + 1] = items[j]
            items[j] = dup

            c.delete(items[j + 1].g)
            c.delete(items[j].g)


            x1 = items[j + 1].x1
            x2 = items[j + 1].x2

            items[j + 1].x1 = dup.x1
            items[j + 1].x2 = dup.x2

            items[j].x1 = x1
            items[j].x2 = x2


            items[j + 1].g = c.create_rectangle(items[j + 1].x1, items[j + 1].y1, items[j + 1].x2, items[j + 1].y2, outline="gray", fill="white")
            items[j].g = c.create_rectangle(items[j].x1, items[j].y1, items[j].x2, items[j].y2, outline="gray", fill="red")

            j -= 1
        items[j + 1] = key
        c.delete(items[j + 1].g)
        items[j + 1].x1 = key.x1
        items[j + 1].x2 = key.x2
        items[j + 1].g = c.create_rectangle(items[j + 1].x1, items[j + 1].y1, items[j + 1].x2, items[j + 1].y2, outline="gray", fill="white")


def bubble_sort():
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j].num > items[j + 1].num:
                dup = items[j + 1]

                items[j + 1] = items[j]
                items[j] = dup

                c.delete(items[j + 1].g)
                c.delete(items[j].g)

                x1 = items[j + 1].x1
                x2 = items[j + 1].x2

                items[j + 1].x1 = dup.x1
                items[j + 1].x2 = dup.x2

                items[j].x1 = x1
                items[j].x2 = x2

                items[j + 1].g = c.create_rectangle(items[j + 1].x1, items[j + 1].y1, items[j + 1].x2, items[j + 1].y2,
                                                    outline="gray", fill="white")
                items[j].g = c.create_rectangle(items[j].x1, items[j].y1, items[j].x2, items[j].y2, outline="gray",
                                                fill="white")


root = tkinter.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.state('zoomed')
# root.attributes("-fullscreen", True)
c = tkinter.Canvas(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth(), bg="black")
c.pack()

item_count = 100
items = []
count = 0
for x in range(item_count):
    width_covered = root.winfo_screenwidth() - (root.winfo_screenwidth() * 0.05)
    height_covered = root.winfo_screenheight() - (root.winfo_screenheight() * 0.05)
    count += 1
    x1 = ((width_covered/item_count) * count)+((root.winfo_screenwidth()-width_covered)/2)-(width_covered/item_count)
    y1 = root.winfo_screenheight()-((root.winfo_screenheight()-height_covered)/2)
    x2 = (((width_covered/item_count) * count)+((root.winfo_screenwidth()-width_covered)/2))
    y2 = root.winfo_screenheight()-((root.winfo_screenheight()-height_covered)/2)-((height_covered/item_count) * count)
    g = c.create_rectangle(x1, y1, x2, y2, outline="gray", fill="white")

    items.append(Item(x1, y1, x2, y2, x, g))


threading.Thread(target=shuffle).start()

root.mainloop()
