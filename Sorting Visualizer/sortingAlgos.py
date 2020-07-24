from tkinter import *
from tkinter import ttk
import random as rd
from bubble_sort import bubble_sort
root = Tk()
root.title('Sorting Algorithms Visualizer')
root.maxsize(1200,800)
root.config(bg='black')

#Variable
selected_alg = StringVar()
data = []
#draw Function
def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data)+1)
    offset = 25
    spacing = 1
    normalisizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalisizedData):
        #topleft
        x0 = i*x_width + offset + spacing
        y0 = c_height - (height * 340)
        #bottom right
        x1 = (i+1)*x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0,x1, y1, fill = colorArray[i])
        #canvas.create_text(x0+2, y0, anchor = SW, text = str(data[i]))
    root.update_idletasks()
#generate Function
def Generate():
    #print("Selected Algo "+ selected_alg.get())
    global data
    data = []
    # for i in range(100):
    #     data.append(i)
    # data.remove(data[0])

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    # try:
    #     minVal = int(minEntry.get())
    # except:
    #     minVal = 1
    # try:
    #     maxVal = int(maxEntry.get())
    # except:
    #     maxVal = 10
    # try:
    #     size = int(sizeEntry.get())
    # except:
    #     size = 10

    # if minVal < 0 : minVal = 0
    # if maxVal > 100 : maxVal = 100
    # if size > 100 or size < 3 : size = 100
    # if minVal > maxVal : minVal,maxVal = maxVal,minVal

    for i in range(size):
        data.append(rd.randrange(minVal,maxVal+1))
    drawData(data,['red' for x in range(len(data))])

#start Function
def StartAlgorithm():
    global data
    #timer = float(speedScale.get())
    bubble_sort(data, drawData,0.6)

#frame/ base layout
UI_frame = Frame(root,width = 600,height = 200, bg='grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady= 5)

canvas = Canvas(root, width = 650, height = 380, bg = 'white')
canvas.grid(row = 1, column = 0, padx = 10, pady= 5)

#user interface area
#row[0]
Label(UI_frame, text="Algorithms: ",bg="grey").grid(row=0,padx = 5, pady = 5, sticky = W)
algoMenu = ttk.Combobox(UI_frame, textvariable = selected_alg, values = ['Bubble Sort', 'Merge Sort'])
algoMenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algoMenu.current(0)

#Speed Scale
speedScale = Scale(UI_frame, from_= 0.1, to= 2.0, length= 200, digits = 2, resolution = 0.2, orient = HORIZONTAL, label = "Select Speed [s]").grid(row =0 ,column=2, padx = 5, pady = 5)#.grid(row = 0, column = 2, padx = 5, pady = 5)
Button(UI_frame, text = "Start", command = StartAlgorithm, bg='red').grid(row = 0, column = 3,padx = 5, pady = 5)

#row[1]
#Label(UI_frame, text="Size: ",bg="grey").grid(row=1,column = 0,padx = 5, pady = 5, sticky = W)
sizeEntry =  Scale(UI_frame, from_= 3, to= 100,resolution = 1, orient = HORIZONTAL, label = "Datasize")
sizeEntry.grid(row = 1, column = 0, padx = 5, pady = 5)

#Label(UI_frame, text="Min Value: ",bg="grey").grid(row=1,column = 2,padx = 5, pady = 5, sticky = W)
minEntry =  Scale(UI_frame, from_= 0, to= 10, resolution = 1, orient = HORIZONTAL, label = "minEntry")
minEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

#Label(UI_frame, text="Max Value: ",bg="grey").grid(row=1,column = 4,padx = 5, pady = 5, sticky = W)
maxEntry = Scale(UI_frame, from_= 10, to= 100, resolution = 1, orient = HORIZONTAL, label = "maxEntry")
maxEntry.grid(row = 1, column = 2, padx = 5, pady = 5)
# Generate Button
Button(UI_frame, text = "Generate", command = Generate, bg='white').grid(row = 1, column = 3, padx = 5, pady = 5)



#MainLoop
root.mainloop()
