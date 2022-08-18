axes(PWM.SegIm)

PDI.Imagem.Final(:,:,1)=zeros(size(PDI.Imagem.SegTotal(:,:,1)));
PDI.Imagem.Final(:,:,2)=zeros(size(PDI.Imagem.SegTotal(:,:,1)));
PDI.Imagem.Final(:,:,3)=zeros(size(PDI.Imagem.SegTotal(:,:,1)));

if Cores.Usadas(1)==1 %Red
    PDI.Imagem.Final(:,:,1)=PDI.Imagem.Final(:,:,1)+PDI.Imagem.SegTotal(:,:,1);
end

if Cores.Usadas(2)==1 %Orange
    PDI.Imagem.Final(:,:,1)=PDI.Imagem.Final(:,:,1)+PDI.Imagem.SegTotal(:,:,2);
    PDI.Imagem.Final(:,:,2)=PDI.Imagem.Final(:,:,2)+0.5*PDI.Imagem.SegTotal(:,:,2);
end

if Cores.Usadas(3)==1 %Yellow
    PDI.Imagem.Final(:,:,1)=PDI.Imagem.Final(:,:,1)+PDI.Imagem.SegTotal(:,:,3);
    PDI.Imagem.Final(:,:,2)=PDI.Imagem.Final(:,:,2)+PDI.Imagem.SegTotal(:,:,3);
end

if Cores.Usadas(4)==1 %Green
    PDI.Imagem.Final(:,:,2)=PDI.Imagem.Final(:,:,2)+PDI.Imagem.SegTotal(:,:,4);
end

if Cores.Usadas(5)==1 %Cyan
    PDI.Imagem.Final(:,:,2)=PDI.Imagem.Final(:,:,2)+PDI.Imagem.SegTotal(:,:,5);
    PDI.Imagem.Final(:,:,3)=PDI.Imagem.Final(:,:,3)+PDI.Imagem.SegTotal(:,:,5);
end

if Cores.Usadas(6)==1 %Blue
    PDI.Imagem.Final(:,:,3)=PDI.Imagem.Final(:,:,3)+PDI.Imagem.SegTotal(:,:,6);
end

if Cores.Usadas(7)==1 %Magenta
    PDI.Imagem.Final(:,:,1)=PDI.Imagem.Final(:,:,1)+ PDI.Imagem.SegTotal(:,:,7);
    PDI.Imagem.Final(:,:,3)=PDI.Imagem.Final(:,:,3)+ PDI.Imagem.SegTotal(:,:,7);
end

Partida.Seg.fig = imshow(PDI.Imagem.Final,'parent',PWM.SegIm);
