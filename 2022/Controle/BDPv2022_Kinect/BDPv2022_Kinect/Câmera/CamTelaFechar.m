set(BDP.menu(1),'Value',0);
set(Cam.ID,  'Visible','off');

if isfield(Cam,'Video')
    if Cam.Video.Previewing
        closepreview(Cam.Video)
        set(Cam.menu(3),'String','Abrir Preview');
    end
end