% Anular recorte
stop(Cam.Video)
set(Cam.Video,'ROIPosition',[0 0 Cam.Resolucao])
start(Cam.Video)

Cam.Redimensionar = 1;
CampoCapturarImagem