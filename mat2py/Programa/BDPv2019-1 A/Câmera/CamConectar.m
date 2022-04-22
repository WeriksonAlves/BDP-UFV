%% Configura a Câmera

set(BDP.status(1),'string','Kinect RGB-D :: Conectar câmera')
set(BDP.status(2),'string','1 | 4 :: Conectando ao adaptador')


% Determina o nome do adaptador e o formato da imagem utilizado
Cam.Nome = {'Kinect','1'};
Cam.Formato = {'RGB_640x480'};
Cam.Tipo = 0;
Cam.Redimensionar = 1;

try
    % Inicia a primeira opção de câmera
    Cam.Video = videoinput(Cam.Nome{1},1,Cam.Formato{1});
    Cam.Tipo = 1;
    Cam.Resolucao = get(Cam.Video,'VideoResolution');
    Cam.ROI = get(Cam.Video,'ROIPosition');
    
    set(BDP.status(2),'string','2 | 4 :: Construtor da câmera RGB carregada.')
    
    % Caso consiga iniciar a câmera, define apenas um frame para cada captura de imagem
    if Cam.Tipo ~= 0
        triggerconfig(Cam.Video,'manual');
        Cam.Video.FramesPerTrigger = 1;
        
        set(BDP.status(2),'string','3 | 4 :: Trigger manual selecionado')
    end
    set(BDP.status(2),'string','4 | 4 :: Câmera conectada!!!')
    
    set(Cam.menu(2:3),'enable','on')
catch
    
    % Apresenta uma mensagem de erro
    errordlg('Não foi possível iniciar a câmera')
    set(BDP.status(2),'string','X | X :: Erro ao conectar câmera!!!')
end

