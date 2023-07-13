%% Configura a Câmera

set(Cam.status(1),'string','RealSense RGB :: Conectar câmera'),drawnow
set(Cam.status(2),'string','1 | 2 :: Conectando ao adaptador'),drawnow

% Determina o nome do adaptador e o formato da imagem utilizado
Cam.Nome = 'Intel(R) RealSense(TM) Depth Camera 435 with RGB Module RGB'; %'Integrated Webcam'; 
Cam.Formato = '640x480';
Cam.Resolucao = [640 480];

% try
    % Inicia a primeira opção de câmera
    Cam.Video = webcam(Cam.Nome);
    Cam.Video.Resolution = Cam.Formato;
    
    set(Cam.status(2),'string','2 | 2 :: Câmera conectada!!!'),drawnow
    
    set(Cam.menu(2),'enable','on') % Preview
    set(Cam.menu(4),'enable','on') % Calibrar cores
    set(Cam.menu(5),'enable','on') % Calibrar campo

    set(BDP.menu(4),'enable','on') % Habilitar partida

%catch
%     
%     % Apresenta uma mensagem de erro
%     errordlg('Não foi possível iniciar a câmera')
%     set(Cam.status(2),'string','X | X :: Erro ao conectar câmera!!!'),drawnow
% end

