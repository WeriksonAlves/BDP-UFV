%% Abre o preview da câmera

if strcmp(Cam.Video.preview,'off')
    preview(Cam.Video)
    set(Cam.menu(3),'String','Fechar Preview');
else
    closepreview(Cam.Video)
    set(Cam.menu(3),'String','Abrir Preview');
end