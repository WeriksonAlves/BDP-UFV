try
    set(Cam.ID,'Visible','off');
end
if isfield(Cam,'Video')
    if Cam.Video.Previewing
        closepreview(Cam.Video)
        set(Cam.menu(3),'String','Abrir Preview');
    end
end
