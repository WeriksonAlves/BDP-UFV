% Recortar imagem
% ==================================================
% Capturar a posi��o na imagem referente ao ponto do Campo Padr�o

% Indica��o dos pontos no campo padr�o

axes(Campo.Real.ID)
Campo.Real.idPontos = [];

Campo.Real.idPontos = ginput(2);

Campo.Real.idPontos(:,2) = Cam.Resolucao(2) - Campo.Real.idPontos(:,2);
Cam.ROI = [min(Campo.Real.idPontos(:,1)) min(Campo.Real.idPontos(:,2)) ...
    abs(diff(Campo.Real.idPontos))];

stop(Cam.Video)
set(Cam.Video,'ROIPosition',Cam.ROI)
start(Cam.Video)

Cam.Redimensionar = sqrt(prod(Cam.Resolucao)/2/prod(Cam.ROI(3:4)));

CampoCapturarImagem