hwInfo = imaqhwinfo('kinect');
hwInfo.DeviceInfo(1);

colorVid = videoinput('kinect',1);
triggerconfig([colorVid],'manual');

colorVid.FramesPerTrigger = 100;

start(colorVid);

colorVid.FramesPerTrigger = 100;

N=101;
for ii = 51:N
[colorFrameData,colorTimeData,colorMetaData] = getdata(colorVid);
imshow(colorFrameData)
    %imwrite(img,strcat('imm/my_new',num2str(ii),'.png'));

end


stop(colorVid)