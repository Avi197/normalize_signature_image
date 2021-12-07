# normalize_signature_image


### Problem
When comparing 2 signature image, the same signature might be crop in a distored way, so we need to keep the features of the signature

Incetptionv3 architecture's input is 150x150 pixel

If we resize the image, it will be stretch out, the features might be distorted </br>

![og_img](https://github.com/Avi197/normalize_signature_image/blob/main/img/og_img.png) </br>
![og_img_resize](https://github.com/Avi197/normalize_signature_image/blob/main/img/og_img_resize.png) </br>


### Solution
##### Resize but keep the signature's feature
- Keep the same ratio of the image when resize and fill the rest of the image with white background to get the desired size 150x150 </br>
- The image's longer side will be resize to 150, the other side will be devide to og_w/150

##### Using Otsu algorithm to clean up background
- Convert image to numpy </br>
- Calculate otsu threshold </br>
- Change all numpy value < otsu threshold to 0 </br>

### Output

![og_img](https://github.com/Avi197/normalize_signature_image/blob/main/img/og_img.png) </br>
![norm_img](https://github.com/Avi197/normalize_signature_image/blob/main/img/norm_img.png)
