%% Cria��o da tela para a segmenta��o

% Inicia e modifica os par�metros da tela de pixels
Calib.Pixels.ID = figure;
set(Calib.Pixels.ID,'menubar','none','numbertitle','off')
set(Calib.Pixels.ID,'name','Sele��o de pixels')

% Cria os bot�es de selecionar e segmentar os pixels
Calib.Pixels.Botao(1) = uicontrol(Calib.Pixels.ID,'style','pushbutton','string','Selecionar Pixels'     ,'units','normalized','position',[0.15 0.025 0.3 0.1],'fontsize',09,'callback','CalibPixelsSelecionar');
Calib.Pixels.Botao(2) = uicontrol(Calib.Pixels.ID,'style','pushbutton','string','Atualizar Segmenta��o' ,'units','normalized','position',[0.55 0.025 0.3 0.1],'fontsize',09,'callback','CalibPixelsAtualizar');
set(Calib.Pixels.Botao(2),'enable','off')

% Determina o local da tela de pixels onde ser� exibida a imagem
Calib.Pixels.Painel = uipanel(Calib.Pixels.ID,'units','normalized','position',[0.1 0.15 0.8 0.8]);
Calib.Pixels.Imagem = subplot(1,1,1,'parent',Calib.Pixels.Painel,'position',[0 0 1 1]);

% Cria e exibe a imagem atual
% TESTE PDI
% Calib.Pixels.Atual = (imresize(imread('img13.png'),Cam.Redimensionar,'bicubic'));
%Calib.Pixels.Atual = flipud(imresize(Cam.Video.snapshot,Cam.Redimensionar));
Calib.Pixels.Atual = Cam.Video.snapshot;
imshow(Calib.Pixels.Atual,'parent',Calib.Pixels.Imagem)

% Habilita a fun��o de zoom na tela
zoom on

% Inicia a vari�vel de valor dos pixels
Calib.Pixels.Valores = [];