#required packages for the class
'''
This package is for python 3.x+
1) sys
2) pip3
'''
class ImageProcessing():
    '''
        This class contains all image manipulation and preprocessing libraries.
    '''
    def convert_image_format_and_resize_changeResolution(self,batch_processing=None,image_dir_path=None,updated_image_path= None,image_format=None,width=None,height=None,dpi= None):
        '''
        Method description : This function convert a image or group of images to 
        1) [jpg or png or tif or gif] format.
        2) we can resize the image or batch of images.
        3) we can change the resolution by changing the dpi value of the image. 
            
            This function takes input arguments:
            1) batch : (True/False) : 
                1.1) True : If you want to convert all images in a folder to any legitimate image format.
                1.2) False : If you want to convert only one image.
            2) image_dir_path : Take the input image path
                2.1) If batch = True ,then we need to specify the path of the directory ,were all the images are present
                2.2) If batch = False ,then we need to specify the path of the particular image.
            3) updated_image_path : Take path in which user want to store the converted image.(default it will store in the current dir by creating a new dir named updated_image_folder_147)
            4)image_format :- It will take the format[jpg or png or tif or gif] of the image which user want to convert default it will take jpg.
            5)width :- you need to give the width of the new image [if you dont give width and height parameters this,then it will not resize the image]
            6)height :- you need to give the height of the image.
            7)dpi :- if you want to change the resolution of the image ,then give the dpi value,else the resolution will be same.
        '''
        import sys
        import os
        package_name = ("PIL","re")
        #Installing the supporting packages if not installed
        for package in package_name:
            if((package in sys.modules)==False):
                os.system("pip3 install"+" "+package)

        import PIL.Image
        import re
        
        #if batch processing required.
        self.batch = batch_processing
        #image path.
        self.image_dir_path = image_dir_path
        #path for saving the image.
        self.updated_image_path = updated_image_path
        #formt of the image to convert
        self.image_format = image_format
        #image dimensions
        self.width = width
        self.height = height
        #resolution of image (dpi (dots per inch))
        self.dpi = dpi
        
        #if input parameter not given,then default parameter will be specified.
        default_save_path = False
        if(self.batch == None):
            self.batch = False
        if(self.updated_image_path == None):
            dir_name = "updated_image_folder_147"
            default_save_path = True
            if(dir_name in os.listdir()):
                os.rmdir(dir_name)
            os.mkdir(dir_name)
            self.updated_image_path = os.getcwd()+os.getcwd()[0]+dir_name
        if(self.image_format==None):
            self.image_format = "jpg"
        else:
            #check for upper case in the image file format.
            if(self.image_format.isupper()):
                self.image_format = self.image_format.lower()
        #resolution parameter
        no_change_resolution = False
        if(self.dpi == None):
            no_change_resolution = True
        resize = False
        #checking for resize of image
        if((self.width and self.height)==None):
            resize = False
        else:
            resize = True
        #checking if batch processing required.
        if(self.batch == True):
            #setting all the image formats which we want to extract.
            r = re.compile(".*.(jpg|png|tif|gif)")
            #extracting all the image files from the given path.
            files=list(filter(r.match,os.listdir(self.image_dir_path)))
            #checking for resize parameter
            if(resize == True):
                if(no_change_resolution == False):
                    #init the file number.
                    file_number = 0
                    for file in files:
                        print("processing file :- ",file_number)
                        file_name = "file"+str(file_number)+"."+self.image_format
                        file_number+=1
                        img=PIL.Image.open(self.image_dir_path+self.image_dir_path[0]+file).resize((self.width,self.height)) #width,height
                        img.convert("RGB").save(self.updated_image_path+self.updated_image_path[0]+file_name,dpi=(self.dpi,self.dpi))
                else:
                    #init the file number.
                    file_number = 0
                    for file in files:
                        print("processing file :- ",file_number)
                        file_name = "file"+str(file_number)+"."+self.image_format
                        file_number+=1
                        img=PIL.Image.open(self.image_dir_path+self.image_dir_path[0]+file).resize((self.width,self.height)) #width,height
                        img.convert("RGB").save(self.updated_image_path+self.updated_image_path[0]+file_name)
            else:
                if(no_change_resolution == False):
                    #init the file number.
                    file_number = 0
                    for file in files:
                        print("processing file :- ",file_number)
                        file_name = "file"+str(file_number)+"."+self.image_format
                        file_number+=1
                        img=PIL.Image.open(self.image_dir_path+self.image_dir_path[0]+file)
                        img.convert("RGB").save(self.updated_image_path+self.updated_image_path[0]+file_name,dpi=(self.dpi,self.dpi))
                else:
                    #init the file number.
                    file_number = 0
                    for file in files:
                        print("processing file :- ",file_number)
                        file_name = "file"+str(file_number)+"."+self.image_format
                        file_number+=1
                        img=PIL.Image.open(self.image_dir_path+self.image_dir_path[0]+file)
                        img.convert("RGB").save(self.updated_image_path+self.updated_image_path[0]+file_name)
        
        #for single image
        else:
            #setting all the image formats which we want to extract.
            r = re.compile(".*.(jpg|png|tif|gif)")    
            if(re.match(".*.(jpg|png|tif|gif)",self.image_dir_path)):
                if(resize == True):
                    if(no_change_resolution == False):
                        file_name = "file171"+"."+self.image_format
                        img=PIL.Image.open(self.image_dir_path).resize((self.width,self.height)) #width,height
                        img.convert("RGB").save(self.updated_image_path+self.updated_image_path[0]+file_name,dpi=(self.dpi,self.dpi))
                    else:
                        file_name = "file171"+"."+self.image_format
                        img=PIL.Image.open(self.image_dir_path).resize((self.width,self.height)) #width,height
                        img.convert("RGB").save(self.updated_image_path+self.updated_image_path[0]+file_name)
                else:
                    if(no_change_resolution == False):
                        file_name = "file171"+"."+self.image_format
                        img=PIL.Image.open(self.image_dir_path)
                        img.convert("RGB").save(self.updated_image_path+self.updated_image_path[0]+file_name,dpi=(self.dpi,self.dpi))
                    else:
                        file_name = "file171"+"."+self.image_format
                        img=PIL.Image.open(self.image_dir_path)
                        img.convert("RGB").save(self.updated_image_path+self.updated_image_path[0]+file_name)
            else:
                print("Invalied image format")