#Sorting Visualizer.
# Imports
import pygame
import random
import time
####TO DO: ADD TIME COMPLEXITIES OF ALL THE ALGORITHMS.
#### PLace labels well.
pygame.font.init() #initializing font module.
startTime = time.time()
# Total window
screen = pygame.display.set_mode(
    (900, 650) #900 is the width and 650 is height. setting the window frame size.
)


isChosenAgain = False
# a global var to show what did the user select for sorting.
chosenSortingIs = 0

# Title and Icon
pygame.display.set_caption(
    "SORTING VISUALIZER"
)

# Boolean variable to run
# the program in while loop
run = True

# Window size and some initials
width = 900
length = 600
array = [0] * 151 #initializing a list of 151 0's in python's list.
arr_clr = [(0, 204, 102)] * 151  #we split the array lines in 3 different colors.
#green -  Unsorted bar
#Blue – Pivot bar
#Orange – Sorted bar
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0), \
       (0, 0, 153), (255, 102, 0)]
fnt = pygame.font.SysFont("comicsans", 30)
#setting up fonts with sizes.
fnt1 = pygame.font.SysFont("comicsans", 20)
# Function to generate new Array

def generate_arr():
    for i in range(1, 151):
        arr_clr[i] = clr[0] #storing color of the i'th index bar in arr_clr[] list.
        array[i] = random.randrange(1, 100) #storing that i'th bar in array[] list.
        #randrange(start,end) = selects a random number between specified values.


#trigerring an array as above.
generate_arr()


# Function to refill the
# updates on the window
def refill():
    screen.fill((255, 255, 255)) #filling up the screen with white.
    draw() #calling draw()
    pygame.display.update()
    #updating the screen with white and update() for applying changes.
    #delay of 10ms.
    pygame.time.delay(5)


def quicksort(array, l, r):
    if l < r:
        pi = partition(array, l, r)
        quicksort(array, l, pi - 1)
        refill()
        for i in range(0, pi + 1):
            arr_clr[i] = clr[3]
        quicksort(array, pi + 1, r)

    # Function to partition the array


def partition(array, low, high):
    pygame.event.pump()
    pivot = array[high]
    arr_clr[high] = clr[2]
    i = low - 1
    for j in range(low, high):
        arr_clr[j] = clr[1]
        refill()
        arr_clr[high] = clr[2]
        arr_clr[j] = clr[0]
        arr_clr[i] = clr[0]
        if array[j] < pivot:
            i = i + 1
            arr_clr[i] = clr[1]
            array[i], array[j] = array[j], array[i]
    refill()
    arr_clr[i] = clr[0]
    arr_clr[high] = clr[0]
    array[i + 1], array[high] = array[high], array[i + 1]

    return (i + 1)
# Sorting Algorithm: Insertion sort
def insertionSort(array):
    for i in range(1, len(array)):
        # ensuring the reachability of event queue.
        # For each frame,handling the internal triggers of events and OS interactions.
        # bugs out without it so, why not.
        pygame.event.pump()

        #making the screen empty if not.
        refill()

        key = array[i]
        arr_clr[i] = clr[2]
        j = i - 1
        while j >= 0 and key < array[j]:
            arr_clr[j] = clr[2]
            array[j + 1] = array[j]
            refill()
            arr_clr[j] = clr[3]
            j = j - 1
        array[j + 1] = key
        refill()
        arr_clr[i] = clr[0]


def bubblesort(array):
        n = len(array)

        # Traverse through all array elements
        for i in range(0 , n):

            # Last i elements are already in place
            pygame.event.pump()

            refill()

            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if array[j] > array[j + 1]:
                    arr_clr[j] = clr[2]
                    array[j], array[j + 1] = array[j + 1], array[j]
                    refill()
                    arr_clr[j+1] = clr[3]

                refill()
            arr_clr[i] = clr[0]


    # Function to Draw the array values
# Sorting Algo:Merge sort
def mergesort(array, l, r):
    mid =(l + r)//2
    if l<r:
        mergesort(array, l, mid)
        mergesort(array, mid + 1, r)
        merge(array, l, mid,
            mid + 1, r)

def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp =[]
    pygame.event.pump()
    while i<= y1 and j<= y2:
        arr_clr[i]= clr[1]
        arr_clr[j]= clr[1]
        refill()
        arr_clr[i]= clr[0]
        arr_clr[j]= clr[0]
        if array[i]<array[j]:
                temp.append(array[i])
                i+= 1
        else:
                temp.append(array[j])
                j+= 1
    while i<= y1:
        arr_clr[i]= clr[1]
        refill()
        arr_clr[i]= clr[0]
        temp.append(array[i])
        i+= 1
    while j<= y2:
        arr_clr[j]= clr[1]
        refill()
        arr_clr[j]= clr[0]
        temp.append(array[j])
        j+= 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i]= temp[j]
        j+= 1
        arr_clr[i]= clr[2]
        refill()
        if y2-x1 == len(array)-2:
            arr_clr[i]= clr[3]
        else:
            arr_clr[i]= clr[0]

def draw():
    # Text should be rendered
    choosingLabel = fnt.render("Press 1 - for Insertion Sort",
                               1, (0, 0, 0))
    screen.blit(choosingLabel, (20, 5))

    txt = fnt.render("Press 2 - for Quick Sort",
                     1, (0, 0, 0))
    # blit(source,co_ordinates_of_position)Position where text is placed
    screen.blit(txt, (20, 30))

    txt1 = fnt.render("Press 3 - for Merge Sort",
                      1, (0, 0, 0))
    screen.blit(txt1, (20, 55))

    txt5 = fnt.render("Press 4 - for Bubble Sort",
                      1, (0, 0, 0))
    # blit(source,co_ordinates_of_position)Position where text is placed
    screen.blit(txt5, (300, 5))

    keyReload = fnt.render("Press R - for Reset",
                      1, (0, 0, 0))
    screen.blit(keyReload, (300, 30))





    if chosenSortingIs == 1 and isChosenAgain==False:
        #if 1, implies, insertion sort.
        algo = fnt1.render("INSERTION SORT", 1, (0, 0, 0))
        screen.blit(algo, (560, 45))
        worst = fnt1.render("Worst Case : O(n * n) ", 1, (0, 0, 0))
        screen.blit(worst, (710, 45))
        best = fnt1.render("Best Case : O(n) ", 1, (0, 0, 0))
        screen.blit(best, (710, 60))
        average = fnt1.render("Average Case : Theeta(n * n)", 1, (0, 0, 0))
        screen.blit(average, (710, 75))

    elif chosenSortingIs == 2 and isChosenAgain==False:
        algo = fnt1.render("QUICK SORT", 1, (0, 0, 0))
        screen.blit(algo, (560, 45))
        worst = fnt1.render("Worst Case : n * n", 1, (0, 0, 0))
        screen.blit(worst, (710, 45))
        best = fnt1.render("Best Case : n * log(n) ", 1, (0, 0, 0))
        screen.blit(best, (710, 60))
        average = fnt1.render("Average Case : n * log(n)", 1, (0, 0, 0))
        screen.blit(average, (710, 75))

    elif chosenSortingIs == 3 and isChosenAgain==False:
        algo = fnt1.render("MERGE SORT", 1, (0, 0, 0))
        screen.blit(algo, (560, 45))
        worst = fnt1.render("Worst Case : n * log(n)", 1, (0, 0, 0))
        screen.blit(worst, (710, 45))
        best = fnt1.render("Best Case : n * log(n)", 1, (0, 0, 0))
        screen.blit(best, (710, 60))
        average = fnt1.render("Average Case : n * log(n)", 1, (0, 0, 0))
        screen.blit(average, (710, 75))

    elif chosenSortingIs == 4 and isChosenAgain==False:
        algo = fnt1.render("BUBBLE SORT", 1, (0, 0, 0))
        screen.blit(algo, (560, 45))
        worst = fnt1.render("Worst Case : O(n * n) ", 1, (0, 0, 0))
        screen.blit(worst, (710, 45))
        best = fnt1.render("Best Case : O(n) ", 1, (0, 0, 0))
        screen.blit(best, (710, 60))
        average = fnt1.render("Average Case : O(n log n)", 1, (0, 0, 0))
        screen.blit(average, (710, 75))

    else:
        algo = fnt1.render("", 1, (0, 0, 0))
        screen.blit(algo, (560, 45))
        worst = fnt1.render("", 1, (0, 0, 0))
        screen.blit(worst, (710, 45))
        best = fnt1.render("", 1, (0, 0, 0))
        screen.blit(best, (710, 60))
        average = fnt1.render("", 1, (0, 0, 0))
        screen.blit(average, (710, 75))



    text3 = fnt1.render("Running Time(sec): " + \
                        str(int(time.time() - startTime)),
                        1, (0, 0, 0))
    screen.blit(text3, (750, 20))

    element_width = (width - 150) // 150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), (0, 95),
                     (900, 95), 6)

    # Drawing the array values as lines
    for i in range(1, 151):
        pygame.draw.line(screen, arr_clr[i],
                         (boundry_arr * i - 3, 100),
                         (boundry_arr * i - 3,
                          array[i] * boundry_grp + 100), element_width)

    # Program should be run


# continuously to keep the window open
while run:
    # background
    screen.fill((255, 255, 255))

    # Event handler stores all event
    for event in pygame.event.get():

        # If we click Close button in window
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                #clear the existing values.
                isChosenAgain = True #so that we can remove the already written TC.
                refill()
                generate_arr()
            if event.key == pygame.K_1:
                chosenSortingIs = 1
                isChosenAgain = False
                insertionSort(array)
            if event.key == pygame.K_2:
                chosenSortingIs = 2
                isChosenAgain = False
                quicksort(array, 1, len(array) - 1)
            if event.key == pygame.K_3:
                chosenSortingIs = 3
                isChosenAgain = False
                mergesort(array, 1, len(array) - 1)
            if(event.key == pygame.K_4):
                chosenSortingIs = 4
                isChosenAgain = False
                bubblesort(array)

    draw()
    pygame.display.update()

pygame.quit()
