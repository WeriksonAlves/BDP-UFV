%% Inicia a captura da c�mera
set(BDP.status(1),'string','Kinect RGB-D :: Captura')

% Se a c�mera estiver parada
if ~isrunning(Cam.Video)
    set(Cam.menu(1),'enable','off')
    set(BDP.status(2),'string','1 | 2 :: Iniciando captura')
    
    % Inicia a captura
    start(Cam.Video)
    set(Cam.menu(2),'string','Parar captura')
    set(BDP.status(2),'string','2 | 2 :: Captura iniciada')
    
else   
    % Para a captura
    stop(Cam.Video)
    set(Cam.menu(1),'enable','on')
    set(Cam.menu(2),'string','Iniciar captura')
    set(BDP.status(2),'string','1 | 1 :: Captura paralizada')
    
end