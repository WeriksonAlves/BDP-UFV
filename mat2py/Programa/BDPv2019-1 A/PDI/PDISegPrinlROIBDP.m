
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

PDI.Imagem.RGB = flipud(imresize(getsnapshot(Cam.Video),Cam.Redimensionar,'bicubic'));
PDI.Imagem.HSV = rgb2hsv(PDI.Imagem.RGB);

%TesteFiltro========================================================================================
switch Calib.Filtro.Usado.Value
    case 2
        PDI.Imagem.HSV2 = PDI.Imagem.HSV(:,:,1:2);
        PDI.Imagem.HSV = rgb2hsv(PDI.Imagem.RGB-imopen(PDI.Imagem.RGB,eval(Filtro.Comando)));
        PDI.Imagem.HSV(:,:,1:2) = PDI.Imagem.HSV2;
end
%===================================================================================================
PDI.CoresMM = {[],[],[],[],[],[],[]}; % Posição regiões, separadas por cores, em milímetros

for jj=1:3
    %localiza a posição de cada jogador levando em consideração sua posição anterior
    PDI.ROI.Pos(jj,:) = PDI.T.transformPointsInverse(JogBDP(jj).pPos.X(1:2)');
    
    %impedi que a posição do jogador exceda o tamanho da imagem
    PDI.ROI.PAXi(jj) = round(PDI.ROI.Pos(jj,2)-PDI.ROI.TamanhoP);
    if PDI.ROI.PAXi(jj)<1
        PDI.ROI.PAXi(jj)=1;
    end
    PDI.ROI.PAXf(jj) = round(PDI.ROI.Pos(jj,2)+PDI.ROI.TamanhoP);
    if PDI.ROI.PAXf(jj)>PDI.ROI.Xm
        PDI.ROI.PAXf(jj)=PDI.ROI.Xm;
    end
    PDI.ROI.PAYi(jj) = round(PDI.ROI.Pos(jj,1)-PDI.ROI.TamanhoP);
    if PDI.ROI.PAYi(jj)<1
        PDI.ROI.PAYi(jj)=1;
    end
    PDI.ROI.PAYf(jj) = round(PDI.ROI.Pos(jj,1)+PDI.ROI.TamanhoP);
    if PDI.ROI.PAYf(jj)>PDI.ROI.Ym
        PDI.ROI.PAYf(jj)=PDI.ROI.Ym;
    end
end

kk = 1;
if Cores.Usadas(PDI.ROI.CP(1))
    for cp=1:3
        %realiza a segmentação em HSV das 3 regioes encontradas 
        if PDI.LimitesHSV(PDI.ROI.CP(1),1) < PDI.LimitesHSV(PDI.ROI.CP(1),2)
            PDI.Imagem.SegH(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp)) = (PDI.Imagem.HSV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),1) >= PDI.LimitesHSV(PDI.ROI.CP(1),1)/360) & (PDI.Imagem.HSV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),1) <= PDI.LimitesHSV(PDI.ROI.CP(1),2)/360);
        else
            PDI.Imagem.SegH(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp)) = (PDI.Imagem.HSV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),1) >= PDI.LimitesHSV(PDI.ROI.CP(1),1)/360) | (PDI.Imagem.HSV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),1) <= PDI.LimitesHSV(PDI.ROI.CP(1),2)/360);
        end
        PDI.Imagem.SegS(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp)) = (PDI.Imagem.HSV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),2) >= PDI.LimitesHSV(PDI.ROI.CP(1),3)/100) & (PDI.Imagem.HSV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),2) <= PDI.LimitesHSV(PDI.ROI.CP(1),4)/100);
        PDI.Imagem.SegV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp)) = (PDI.Imagem.HSV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),3) >= PDI.LimitesHSV(PDI.ROI.CP(1),5)/100) & (PDI.Imagem.HSV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),3) <= PDI.LimitesHSV(PDI.ROI.CP(1),6)/100);
        
        % =============================================
        % Salva cada segmentação na variável pré alocada
        
        PDI.Imagem.SegTotal(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp),PDI.ROI.CP(1)) = medfilt2( PDI.Imagem.SegH(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp)) & PDI.Imagem.SegS(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp)) & PDI.Imagem.SegV(PDI.ROI.PAXi(cp):PDI.ROI.PAXf(cp),PDI.ROI.PAYi(cp):PDI.ROI.PAYf(cp))); % Eliminar Ruído Sal e Pimenta
        
    end
    % =============================================
    PDI.Imagem.Regioes = regionprops(PDI.Imagem.SegTotal(:,:,PDI.ROI.CP(1)));
    
    % Armezenar regiões em função da área
    
    for ll = 1:length(PDI.Imagem.Regioes)  % analisa todas as regioes 
        if PDI.Imagem.Regioes(ll).Area > PDI.pPar.AreaMin % testa o tamanho minimo da area
            % Transformação para Pixel para Milimetros
            PDI.CoresMM{PDI.ROI.CP(1)}(kk,:) = [PDI.T.transformPointsForward( [(PDI.Imagem.Regioes(ll).Centroid(1)) (PDI.Imagem.Regioes(ll).Centroid(2))] ) PDI.Imagem.Regioes(ll).Area];
            kk = kk + 1; % número de localizações validas
        end
    end
end

