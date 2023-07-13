%% Configura a C�mera

set(Cam.status(1),'string','Kinect RGB :: Conectar c�mera'),drawnow
set(Cam.status(2),'string','1 | 2 :: Conectando ao adaptador'),drawnow

% Determina o nome do adaptador e o formato da imagem utilizado
Cam.Nome = {'Kinect','1'}; %'Integrated Webcam'; 
% Cam.Formato = '640x480';
% Cam.Resolucao = [640 480];

try
    % Inicia a primeira op��o de c�mera
    Cam.Video = videoinput(Cam.Nome{1});
%     Cam.Video.VideoResolution = Cam.Formato;
    
    set(Cam.status(2),'string','2 | 2 :: C�mera conectada!!!'), drawnow
    
    set(Cam.menu(2),'enable','on') % Preview
    set(Cam.menu(4),'enable','on') % Calibrar cores
    set(Cam.menu(5),'enable','on') % Calibrar campo

    set(BDP.menu(4),'enable','on') % Habilitar partida

catch
    
    % Apresenta uma mensagem de erro
    errordlg('N�o foi poss�vel iniciar a c�mera')
    set(Cam.status(2),'string','X | X :: Erro ao conectar c�mera!!!'),drawnow
end

