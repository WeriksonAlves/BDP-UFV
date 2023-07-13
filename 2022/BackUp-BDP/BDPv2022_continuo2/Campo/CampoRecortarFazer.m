% Recortar imagem
% ==================================================
% Capturar a posição na imagem referente ao ponto do Campo Padrão

% Indicação dos pontos no campo padrão

axes(Campo.Real.ID)
Campo.Real.Recorte = [];

Campo.Real.Recorte = round(ginput(2));


Campo.Real.Im  = Campo.Real.Im(min(Campo.Real.Recorte(:,2)):max(Campo.Real.Recorte(:,2)),...
    min(Campo.Real.Recorte(:,1)):max(Campo.Real.Recorte(:,1)),:);

Campo.Real.fig = imshow(Campo.Real.Im,'parent',Campo.Real.ID);

% Campo.Real.idPontos(:,2) = Cam.Resolucao(2) - Campo.Real.idPontos(:,2);
% Cam.ROI = [min(Campo.Real.idPontos(:,1)) min(Campo.Real.idPontos(:,2)) ...
%     abs(diff(Campo.Real.idPontos))];
% 
% stop(Cam.Video)
% set(Cam.Video,'ROIPosition',Cam.ROI)
% start(Cam.Video)
% 
% Cam.Redimensionar = sqrt(prod(Cam.Resolucao)/2/prod(Cam.ROI(3:4)));

% CampoCapturarImagem