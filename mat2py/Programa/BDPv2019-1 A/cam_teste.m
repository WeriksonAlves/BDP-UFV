x = videoinput('Kinect', 1, 'RGB_640x480');

Imagem = flipud(imresize(getsnapshot(x),1,'bicubic'));

imshow(x)