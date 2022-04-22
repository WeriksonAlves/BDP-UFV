
% Processar imagem e entrar as camadas segmentadas
% Identificação das cores
% 1- Red
% 2- Orange
% 3- Yellow
% 4- Green
% 5- Cyan
% 6- Blue
% 7- Magenta

% TESTE PDI
% PDI.Imagem.RGB = imresize(imread('img13.png'),Cam.Redimensionar,'bicubic');
% obtem uma imagem da camera
PDI.Imagem.RGB = flipud(imresize(getsnapshot(Cam.Video),Cam.Redimensionar,'bicubic'));
PDI.Imagem.HSV = rgb2hsv(PDI.Imagem.RGB);

PDI.CoresMM = {[],[],[],[],[],[],[]}; % Posição regiões, separadas por cores, em milímetros


if Cores.Usadas(PDI.ROI.CP(1))
    % REALIZAR A SEGMENTAÇÃO EM HSV
    if PDI.LimitesHSV(PDI.ROI.CP(1),1) < PDI.LimitesHSV(PDI.ROI.CP(1),2)
        PDI.Imagem.SegH = (PDI.Imagem.HSV(:,:,1) >= PDI.LimitesHSV(PDI.ROI.CP(1),1)/360) & (PDI.Imagem.HSV(:,:,1) <= PDI.LimitesHSV(PDI.ROI.CP(1),2)/360);
    else
        PDI.Imagem.SegH = (PDI.Imagem.HSV(:,:,1) >= PDI.LimitesHSV(PDI.ROI.CP(1),1)/360) | (PDI.Imagem.HSV(:,:,1) <= PDI.LimitesHSV(PDI.ROI.CP(1),2)/360);
    end
    PDI.Imagem.SegS = (PDI.Imagem.HSV(:,:,2) >= PDI.LimitesHSV(PDI.ROI.CP(1),3)/100) & (PDI.Imagem.HSV(:,:,2) <= PDI.LimitesHSV(PDI.ROI.CP(1),4)/100);
    PDI.Imagem.SegV = (PDI.Imagem.HSV(:,:,3) >= PDI.LimitesHSV(PDI.ROI.CP(1),5)/100) & (PDI.Imagem.HSV(:,:,3) <= PDI.LimitesHSV(PDI.ROI.CP(1),6)/100);
    
    % =============================================
    % Salva cada segmentação na variável pré alocada
    
    PDI.Imagem.SegTotal(:,:,PDI.ROI.CP(1)) = medfilt2(PDI.Imagem.SegH & PDI.Imagem.SegS & PDI.Imagem.SegV); % Eliminar Ruído Sal e Pimenta
    
    % =============================================
    PDI.Imagem.Regioes = regionprops(PDI.Imagem.SegTotal(:,:,PDI.ROI.CP(1)));
    
    % Armezenar regiões em função da área
    kk = 1;
    for jj = 1:length(PDI.Imagem.Regioes)
        if PDI.Imagem.Regioes(jj).Area > PDI.pPar.AreaMin
            % Transformação para Pixel para Milimetros
            PDI.CoresMM{PDI.ROI.CP(1)}(kk,:) = [PDI.T.transformPointsForward(PDI.Imagem.Regioes(jj).Centroid) PDI.Imagem.Regioes(jj).Area];
            kk = kk + 1;
        end
    end
    
end




