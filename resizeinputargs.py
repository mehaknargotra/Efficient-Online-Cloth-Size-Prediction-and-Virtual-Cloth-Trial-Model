import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import os
import cv2 as cv
import argparse
import math
import PIL
from PIL import Image
import time
#% matplotlib qt 
# This is a magic command to display in external window 

parser = argparse.ArgumentParser(
        description='This script is used to demonstrate OpenPose human pose estimation network '
                    'from https://github.com/CMU-Perceptual-Computing-Lab/openpose project using OpenCV. '
                    'The sample and model are simplified and could be used for a single person on the frame.')
parser.add_argument('--input', help='Path to input image.')
args = parser.parse_args()
# img=cv.imread(r'C:\Users\Mehek\Desktop\PROJECT\GUI\7.jpg',-1)
def resizeinput(img,shirt):
            print('hello from function')
            args.proto=r'pose/coco/deploy_coco.prototxt'
            args.model=r'pose/coco/pose_iter_440000.caffemodel'
            args.dataset=r'COCO'
            args.input=img
            print("ARGS.INPUT=", img)
            def premultiply(im):
                pixels = im.load()
                for y in range(im.size[1]):
                    for x in range(im.size[0]):
                        r, g, b, a = pixels[x, y]
                        if a != 255:
                            r = r * a // 255
                            g = g * a // 255
                            b = b * a // 255
                            pixels[x, y] = (r, g, b, a)

            def unmultiply(im):
                pixels = im.load()
                for y in range(im.size[1]):
                    for x in range(im.size[0]):
                        r, g, b, a = pixels[x, y]
                        if a != 255 and a != 0:
                            r = 255 if r >= a else 255 * r // a
                            g = 255 if g >= a else 255 * g // a
                            b = 255 if b >= a else 255 * b // a
                            pixels[x, y] = (r, g, b, a)

            def calculateDistance(p1,p2):
                cor1=[]
                cor2=[]
                x1=None
                x2=None
                y1=None
                y2=None
                #for x in p1:
                #   cor1.append(x)
                #for pair in cor1:
                #   x1=pair[0]
                #   y1=pair[1]
                #for x in p2:
                #   cor2.append(x)
                #for pair in cor1:
                #   x2=pair[0]
                #   y2=pair[1]
                x1,y1=p1
                x2,y2=p2
                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                return dist

            if args.dataset == 'COCO':
                BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
                               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

                POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
                               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
                               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
                               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
                               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]
            elif args.dataset=='MPI':
                #assert(args.dataset == 'MPI')
                BODY_PARTS = { "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                               "Background": 15 }

                POSE_PAIRS = [ ["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                               ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                               ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                               ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"] ]
            else:
                
                BODY_PARTS ={"Nose":0,"Neck":1,"RShoulder":2,"RElbow":3,"RWrist":4,"LShoulder":5,"LElbow":6,"LWrist":7,"MidHip":8,"RHip":9,"RKnee":10,"RAnkle":11,"LHip":12,"LKnee":13,"LAnkle":14,"REye":15,"LEye":16,"REar":17,"LEar":18,"LBigToe":19,"LSmallToe":20,"LHeel":21,"RBigToe":22,"RSmallToe":23,"RHeel":24,"Background":25}

                POSE_PAIRS =[ ["Neck","MidHip"],   ["Neck","RShoulder"],   ["Neck","LShoulder"],   ["RShoulder","RElbow"],   ["RElbow","RWrist"],   ["LShoulder","LElbow"],   ["LElbow","LWrist"],   ["MidHip","RHip"],   ["RHip","RKnee"],  ["RKnee","RAnkle"], ["MidHip","LHip"],  ["LHip","LKnee"], ["LKnee","LAnkle"],  ["Neck","Nose"],   ["Nose","REye"], ["REye","REar"],  ["Nose","LEye"], ["LEye","LEar"],   
            ["RShoulder","REar"],  ["LShoulder","LEar"],   ["LAnkle","LBigToe"],["LBigToe","LSmallToe"],["LAnkle","LHeel"], ["RAnkle","RBigToe"],["RBigToe","RSmallToe"],["RAnkle","RHeel"] ]

            inWidth = 368
            inHeight = 368
            args.thr = 0.1
            # args.width = 368
            # args.height = 368


            net = cv.dnn.readNetFromCaffe(args.proto, args.model)

            
            frame = cv2.imread(args.input,1)
            frameWidth = frame.shape[1]
            frameHeight = frame.shape[0]

            inp = cv.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                                          (0, 0, 0), swapRB=False, crop=False)
            net.setInput(inp)
            start_t = time.time()
            out = net.forward()
                
            print("time is ",time.time()-start_t)
            # print(inp.shape)
            #kwinName="Pose Estimation Demo: Cv-Tricks.com"
            #cv.namedWindow(kwinName, cv.WINDOW_AUTOSIZE)
            #assert(len(BODY_PARTS) == out.shape[1])

            points = []
            for i in range(len(BODY_PARTS)):
                # Slice heatmap of corresponging body's part.
                heatMap = out[0, i, :, :]

                # Originally, we try to find all the local maximums. To simplify a sample
                # we just find a global one. However only a single pose at the same time
                # could be detected this way.
                _, conf, _, point = cv.minMaxLoc(heatMap)
                x = (frameWidth * point[0]) / out.shape[3]
                y = (frameHeight * point[1]) / out.shape[2]

                # Add a point if it's confidence is higher than threshold.
                points.append((int(x), int(y)) if conf > args.thr else None)

            for pair in POSE_PAIRS:
                partFrom = pair[0]
                partTo = pair[1]
                assert(partFrom in BODY_PARTS)
                assert(partTo in BODY_PARTS)

                idFrom = BODY_PARTS[partFrom]
                idTo = BODY_PARTS[partTo]
                if points[idFrom] and points[idTo]:
                    cv.line(frame, points[idFrom], points[idTo], (255, 74, 0), 3)
                    cv.ellipse(frame, points[idFrom], (4, 4), 0, 0, 360, (255, 255, 255), cv.FILLED)
                    cv.ellipse(frame, points[idTo], (4, 4), 0, 0, 360, (255, 255, 255), cv.FILLED)
                    cv.putText(frame, str(idFrom), points[idFrom], cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255),2,cv.LINE_AA)
                    cv.putText(frame, str(idTo), points[idTo], cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255),2,cv.LINE_AA)

            idFrom = BODY_PARTS["RShoulder"]
            idTo = BODY_PARTS["Neck"]
            p1=points[idFrom]

            _,y01=p1
            p2=points[idTo]
            td=calculateDistance(p1,p2)
            shr=p1
            idFrom = BODY_PARTS["Neck"]
            idTo = BODY_PARTS["LShoulder"]
            p1=points[idFrom]
            p2=points[idTo]

            _,y02=p2
            td=td+calculateDistance(p1,p2)
            idFrom = BODY_PARTS["RWrist"]
            idTo = BODY_PARTS["LWrist"]
            x01,_=points[idFrom]
            x02,_=points[idTo]
            nshr=(x01,y01)
            nshl=(x02,y02)
            t1=(x01,y01)

            idFrom = BODY_PARTS["RElbow"]
            idTo = BODY_PARTS["LElbow"]
            p1=points[idFrom]
            p2=points[idTo]
            td=calculateDistance(p1,p2)
            print(td)
            tsize="MEDIUM"
            if td > 1250:
                tsize="LARGE"
            elif td>1000:
                tsize="MEDIUM"
            else:
                tsize="SMALL"
                    

            idFrom = BODY_PARTS["LHip"]
            hip=points[idFrom]
            xh,yh=hip
            # j='.jpg'
            abcd=img.split('.')
            # resultimg=abcd[0]+"_result.jpg"
            # print(resultimg)
            cv.imwrite(abcd[0]+"_result.jpg",frame)
           
            # im1 = cv.imread(r'result_'+ args.input)
        


            #cv2.imshow("result",args.input)
            #print(result.shape)
            print("x =",x ,"y=",y, " x01=", x01,"  y01=",y01, " x02=",x02," y02=",y02 ," xh=", xh)
            

            rsh=points[BODY_PARTS["RShoulder"]]
            lsh=points[BODY_PARTS["LShoulder"]]
            relbow=points[BODY_PARTS["RElbow"]]
            lelbow=points[BODY_PARTS["LElbow"]]
            rhip=points[BODY_PARTS["RHip"]]
            rshoulder_shirt=(39,59)
            lshoulder_shirt=(241,59)
            rwaist_shirt=(48,358)
            b=int(calculateDistance(rsh,lsh))
            l=int(rhip[1]-rsh[1])
            print("b=",b,"l=",l)
            bshirt=int(calculateDistance(rshoulder_shirt,lshoulder_shirt))
            lshirt=int(rwaist_shirt[1]-rshoulder_shirt[1])
            print("bshirt=",bshirt,"lshirt=",lshirt)




            #--------------------------OVERLAYING---------------------------------------------------------------- 
            display_windowb=900
            display_windowl=800
            #background image
            im1 = cv.imread(abcd[0]+'_result.jpg')
            print("im1.shape=",im1.shape)
            hn,wn,c=im1.shape
            #resize background image
            background_img=cv.resize(im1,(display_windowb,display_windowl))

            #shirt
            overlay_t=cv.imread(shirt,-1)
            print("overlay_t=",overlay_t.shape)
            lprime,bprime,cs=overlay_t.shape

            #function 
            def overlay_transparent(background_img, overlay_t, x=l, y=b, overlay_size=(l*b)):
                bg_img = background_img.copy()
                if overlay_size is not None:
                    img_to_overlay_t = cv.resize(overlay_t.copy(), overlay_size)
                    b,g,r,a = cv.split(img_to_overlay_t)
                    overlay_color = cv.merge((b,g,r))
                    mask = cv.medianBlur(a,5)
                    h, w, _ = overlay_color.shape
                    roi = bg_img[y:y+h, x:x+w]
                    img1_bg = cv.bitwise_and(roi.copy(),roi.copy(),mask = cv.bitwise_not(mask))
                    img2_fg = cv.bitwise_and(overlay_color,overlay_color,mask = mask)
                    bg_img[y:y+h, x:x+w] = cv.add(img1_bg, img2_fg)
                    return bg_img


            #scaling breadthnd length of the shirt wrt display window


            b=b*display_windowb//wn
            l=l*display_windowl//hn

            bprimenew=bprime* b //bshirt
            lprimenew=lprime* l //lshirt

            # bscaling_factor=1+0.4
            # lscaling_factor=1+0.3
            # b=int(b*bscaling_factor)
            # l=int(l*lscaling_factor)

            # bshirt= int(bprime * (b / bshirt))
            # lshirt= int(lprime * (l / lshirt))

            # bshirt=bshirt*display_windowb//wn
            # lshirt=lshirt*display_windowl//hn
            rshoulder_shirtnew=[0,0]
            rshoulder_shirtnew[0]=rshoulder_shirt[0] * bprimenew // bprime
            rshoulder_shirtnew[1]=rshoulder_shirt[1] * lprimenew // lprime




            #bshirt=int(bshirt*bscaling_factor)
            #lshirt=int(lshirt*lscaling_factor)

            # boff=b//10
            # loff=l//10
            print("l=",l, "b=", b)
            print("bshirt=", bshirt, "lshirt=", lshirt)
            print("rshoulder_shirt=",rshoulder_shirt)
            print("RShoulder",rsh)
            print("rsh[0]*display_windowb//wn===", rsh[0]*display_windowb//wn)
            #abc=overlay_transparent(background_img,overlay_t,(rsh[0]*display_windowb//wn-boff),(rsh[1]*display_windowl//hn-loff),(bshirt,lshirt))
            abc=overlay_transparent(background_img,overlay_t, (rsh[0]*display_windowb//wn - rshoulder_shirtnew[0]),(rsh[1]*display_windowl//hn - rshoulder_shirtnew[1]),(bprimenew,lprimenew))
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50) 
            fontScale = 2
            color = (255, 0, 0)
            thickness = 4
            abc = cv2.putText(abc, tsize, org, font,fontScale, color, thickness, cv2.LINE_AA)
            cv.imwrite('final_result_overlay.jpg',abc)

            print(abc.shape)
            cv2.imshow('imagess',abc)  
            cv.waitKey(0)

#             #------------------------OVERLAYING NEW---------------------------------

#resizeinput(r'C:\Users\Mehek\Desktop\PROJECT\GUI\7.jpg',r'C:\Users\Mehek\Desktop\PROJECT\GUI\Dress7\newtshirt.png')

