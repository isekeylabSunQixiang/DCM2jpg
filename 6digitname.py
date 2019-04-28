import SimpleITK as sitk
import numpy as np
import cv2
import os

def convert_from_dicom_to_jpg(img,low_window,high_window,save_path):
    lungwin = np.array([low_window*1., high_window*1.])
    newimg = (img-lungwin[0])/(lungwin[1]-lungwin[0])    #归一化
    newimg = (newimg*255).astype('uint8')                #将像素值扩展到[0,255]
    cv2.imwrite(save_path, newimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

if __name__ == '__main__':
    dcm_image_path = 'D:\\dataset\\1001\\img\\'
    output_jpg_path = 'D:\\datasetv1\\img\\'
    for filename_img in os.listdir(dcm_image_path):
        ds_array = sitk.ReadImage(dcm_image_path + filename_img)
        # print(dcm_image_path + filename_img)
        img_array = sitk.GetArrayFromImage(ds_array)
        shape = img_array.shape
        img_array = np.reshape(img_array, (shape[1], shape[2]))
        high = np.max(img_array)
        low = np.min(img_array)
        save_path = output_jpg_path + os.path.splitext(filename_img)[0] + '.jpg'
        print(save_path)
        convert_from_dicom_to_jpg(img_array, low, high, save_path)
    print('Next.')

    name = os.listdir(output_jpg_path)
    n = 0
    for i in name:
        oldname = output_jpg_path + name[n]
        imgname = str(n + 1)
        imgname_new = imgname.zfill(6)
        newname = output_jpg_path + imgname_new + '.jpg'
        os.rename(oldname, newname)
        print(newname)
        n += 1

    jpg_name = os.listdir(output_jpg_path)
    xml_path = 'D:\\datasetv1\\xml\\'
    x =0
    for xml in os.listdir(xml_path):
        xml_name_new = xml_path + jpg_name[n][0:6] + '.xml'
        os.rename(xml, xml_name_new)
        print(xml_name_new)
        x += 1

    print("finish")