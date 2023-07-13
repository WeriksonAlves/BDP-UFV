% Processar imagem e entrar as camadas segmentadas
% Identifica��o das cores
% 1- Red
% 2- Orange
% 3- Yellow
% 4- Green
% 5- Cyan
% 6- Blue
% 7- Magenta

% TESTE PDI

PDI.Imagem.RGB = flipud(imresize(getsnapshot(Cam.Video),Cam.Redimensionar,'bicubic'));
PDI.Imagem.HSV = rgb2hsv(PDI.Imagem.RGB);

PDI.CoresMM = {[],[],[],[],[],[],[]}; % Posi��o regi�es, separadas por cores, em mil�metros
for ii =  1:7
    % REALIZAR A SEGMENTA��O EM HSV
    if PDI.LimitesHSV(ii,1) < PDI.LimitesHSV(ii,2)
        PDI.Imagem.SegH = (PDI.Imagem.HSV(:,:,1) >= PDI.LimitesHSV(ii,1)/360) & (PDI.Imagem.HSV(:,:,1) <= PDI.LimitesHSV(ii,2)/360);
    else
        PDI.Imagem.SegH = (PDI.Imagem.HSV(:,:,1) >= PDI.LimitesHSV(ii,1)/360) | (PDI.Imagem.HSV(:,:,1) <= PDI.LimitesHSV(ii,2)/360);
    end
    PDI.Imagem.SegS = (PDI.Imagem.HSV(:,:,2) >= PDI.LimitesHSV(ii,3)/100) & (PDI.Imagem.HSV(:,:,2) <= PDI.LimitesHSV(ii,4)/100);
    PDI.Imagem.SegV = (PDI.Imagem.HSV(:,:,3) >= PDI.LimitesHSV(ii,5)/100) & (PDI.Imagem.HSV(:,:,3) <= PDI.LimitesHSV(ii,6)/100);
    
    % =============================================
    % Salva cada segmenta��o na vari�vel pr� alocada
    PDI.Imagem.SegTotal(:,:,ii) = medfilt2(PDI.Imagem.SegH & PDI.Imagem.SegS & PDI.Imagem.SegV); % Eliminar Ru�do Sal e Pimenta

    % =============================================    
    PDI.Imagem.Regioes = regionprops(PDI.Imagem.SegTotal(:,:,ii));
    
    % Armezenar regi�es em fun��o da �rea
    kk = 1;
    for jj = 1:length(PDI.Imagem.Regioes)
        if PDI.Imagem.Regioes(jj).Area > PDI.pPar.AreaMin
            % Transforma��o para Pixel para Milimetros
            PDI.CoresMM{ii}(kk,:) = [PDI.T.transformPointsForward(PDI.Imagem.Regioes(jj).Centroid) PDI.Imagem.Regioes(jj).Area];
            kk = kk + 1;
        end
    end
end