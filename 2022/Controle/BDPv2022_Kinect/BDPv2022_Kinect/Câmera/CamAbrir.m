%% Abre o preview da c�mera

% Acertar bot�o para abrir e fechar
if isfield(Cam,'Video')
    if strcmp(Cam.Video.Previewing,'on')
        closepreview(Cam.Video)
        set(Cam.menu(2),'String','Abrir Preview');
    else
        preview(Cam.Video)
        set(Cam.menu(2),'String','Fechar Preview');
    end
end

% Cam.Video.closePreview