# Importing Image module from PIL package
from PIL import Image
import json
import os

path = r'Insert path of annotation.json file'

f = open(path)
annotation = json.load(f)

for pic_name in os.listdir(r'InsertFILENAME of location of images'):  # annotation


        imageIdx = int(pic_name.split(".")[0])
        charttype = annotation[imageIdx]['type']
        img_w = annotation[imageIdx]['general_figure_info']['figure_info']['bbox']['bbox']['w']
        img_h = annotation[imageIdx]['general_figure_info']['figure_info']['bbox']['bbox']['h']
        output = ''
        filename = ''
        outpath = ''
        # for bars extract Bars - majorTicks - minorTicks
        if charttype == "hbar_categorical" or charttype == "vbar_categorical":
            axis = ''
            if charttype == "hbar_categorical" :
                axis = 'x_axis'
                filename = 'InsertFileName'
            if charttype == "vbar_categorical":
                axis = 'y_axis'
                filename = 'InsertFileName'

            barsinfo = annotation[imageIdx]['models'][0]
            for bb_idx in range(len(barsinfo['bboxes'])):
                x , y = barsinfo['bboxes'][bb_idx]['x'], barsinfo['bboxes'][bb_idx]['y']
                w , h = barsinfo['bboxes'][bb_idx]['w'], barsinfo['bboxes'][bb_idx]['h']
                # Finding midpoints
                x_centre, y_centre = (x + (x + w)) / 2, (y + (y + h)) / 2
                # Normalization
                x_centre, y_centre = (x_centre / img_w), (y_centre / img_h)
                w, h = (w / img_w), (h / img_h)
                # Limiting up to fix number of decimal places
                x_centre, y_centre = round(x_centre, 6), round(y_centre, 6)
                w, h = round(w, 6), round(h, 6)

                # adding to str of yolo file
                output += str(0) + ' ' + str(x_centre) + ' ' + str(y_centre) + ' ' + str(w) + ' ' + str(h) + '\n'


            bboxes = annotation[imageIdx]['general_figure_info'][axis]['major_ticks']['bboxes']
            for tick_idx in range((len(bboxes) // 2)):
                x, y = bboxes[tick_idx]['x'], bboxes[tick_idx]['y']
                w, h = bboxes[tick_idx]['w'], bboxes[tick_idx]['h']
                x_centre, y_centre = (x + (x + w)) / 2, (y + (y + h)) / 2
                # Normalization
                x_centre, y_centre = (x_centre / img_w), (y_centre / img_h)
                w, h = (w / img_w), (h / img_h)
                # Limiting up to fix number of decimal places
                x_centre, y_centre = round(x_centre, 6), round(y_centre, 6)
                w, h = round(w, 6), round(h, 6)
                output += str(1) + ' ' + str(x_centre) + ' ' + str(y_centre) + ' ' + str(w) + ' ' + str(h) + '\n'

            bboxes = annotation[imageIdx]['general_figure_info'][axis]['minor_ticks']['bboxes']
            for tick_idx in range((len(bboxes) // 2)):
                x, y = bboxes[tick_idx]['x'], bboxes[tick_idx]['y']
                w, h = bboxes[tick_idx]['w'], bboxes[tick_idx]['h']
                x_centre, y_centre = (x + (x + w)) / 2, (y + (y + h)) / 2
                # Normalization
                x_centre, y_centre = (x_centre / img_w), (y_centre / img_h)
                w, h = (w / img_w), (h / img_h)
                # Limiting up to fix number of decimal places
                x_centre, y_centre = round(x_centre, 6), round(y_centre, 6)
                w, h = round(w, 6), round(h, 6)
                output += str(2) + ' ' + str(x_centre) + ' ' + str(y_centre) + ' ' + str(w) + ' ' + str(h) + '\n'

            outpath = "InsertFileHere"+ filename

        # For pie extract Legend - and symbols contained in it.
        elif charttype ==  'pie':
            legend = annotation[imageIdx]['general_figure_info']['legend']

            x,y = legend['bbox']['x'], legend['bbox']['y']
            w,h = legend['bbox']['w'], legend['bbox']['h']

            # Finding midpoints
            x_centre , y_centre= (x + (x+w))/2 , (y + (y+h))/2

            # Normalization
            x_centre ,  y_centre = (x_centre / img_w) ,(y_centre / img_h)
            w , h = (w / img_w) , (h / img_h)

            # Limiting upto fix number of decimal places
            x_centre , y_centre = round(x_centre, 6) ,round(y_centre, 6)
            w , h = round(w,  6) ,round(h, 6)

            #adding to str of yolo file
            output += str(0) + ' ' + str(x_centre)+' ' + str(y_centre)+' ' + str(w)+' ' + str(h)+'\n'

            for bb_idx in range(len(legend['items'])):
                x,y = legend['items'][bb_idx]['preview']['bbox']['x'], legend['items'][bb_idx]['preview']['bbox']['y']
                w,h = legend['items'][bb_idx]['preview']['bbox']['w'], legend['items'][bb_idx]['preview']['bbox']['h']

                # Finding midpoints
                x_centre , y_centre= (x + (x+w))/2 , (y + (y+h))/2

                # Normalization
                x_centre ,  y_centre = (x_centre/img_w) ,(y_centre/img_h)
                w , h = (w/img_w) , (h/img_h)

              # Limiting upto fix number of decimal places
                x_centre , y_centre = round(x_centre, 6) ,round(y_centre, 6)
                w , h = round(w,  6) ,round(h, 6)
                output += str(1)  + ' ' + str(x_centre)+' ' + str(y_centre)+' ' + str(w)+' ' + str(h)+'\n'
            outpath = "InsertFileHere" + filename


        with open(outpath+'\\labels\\' + str(imageIdx) + '.txt', "w") as file:
           file.write(output)
        im = Image.open("InsertFileHere" + str(imageIdx) + ".png")
        # save a image using extension
        im.save(outpath + "\\images\\" + str(imageIdx) + ".png")