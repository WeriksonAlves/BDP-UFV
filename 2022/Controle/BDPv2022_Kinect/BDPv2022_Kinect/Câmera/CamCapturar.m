%% Inicia a captura da câmera
set(Cam.status(1),'string','Kinect RGB-D :: Captura'),drawnow

% Se a câmera estiver parada
if ~isrunning(Cam.Video)
    set(Cam.menu(1),'enable','off')
    set(Cam.status(2),'string','1 | 2 :: Iniciando captura'),drawnow
    
    % Inicia a captura
    set(Cam.status(2),'string','2 | 2 :: Captura iniciada'),drawnow
    
    % Habilita os botões do menu principal que necessitam da câmera
    set(BDP.menu(2:4),'enable','on')
else
    
    % Para a captura
    set(Cam.menu(1),'enable','on')
    set(Cam.menu(2),'string','Iniciar captura')
    set(Cam.status(2),'string','1 | 1 :: Captura paralizada'),drawnow
    
    % Desabilita os botões do menu principal que necessitam da câmera
    set(BDP.menu(2:4),'enable','off')
    
end