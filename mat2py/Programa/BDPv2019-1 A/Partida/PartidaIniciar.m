clc

% Relacionar time, camisa e fun��o
PartidaSelecionar
% ==============================================
% Comunica��o com o rob�
ComunicacaoIniciar

% ==============================================
% Iniciar Partida
set(Partida.Botoes(4),'Enable','on')
Partida.emJogo = 0;
Partida.emOperacao = 1;
Partida.cont = 0;

% Log de in�cio
set(BDP.status(1),'string','Partida em modo JOGO')
set(BDP.status(2),'string','')

% Vari�veis de processamento de imagem
PDI.pPar.AreaMin  = 10;  % �rea m�nima em pixels

%Dados do ROI
PDI.ROI.Tamanho = 15;
PDI.ROI.TamanhoP = 30;
Campo.Real.Im  = flipud(imresize(getsnapshot(Cam.Video),Cam.Redimensionar));
[PDI.ROI.Xm, PDI.ROI.Ym] = size(Campo.Real.Im(:,:,1));
PDI.ROI.POSIDEN(1:2,1:3) = 0;

if get(Partida.CorTime(1),'Value')
    PDI.ROI.CP(1)=3;
    PDI.ROI.CP(2)=5;
else
    PDI.ROI.CP(1)=5;
    PDI.ROI.CP(2)=3;
end

% Tempo de controle
Partida.tc = tic;

% Tempo de jogo
Partida.tji = tic;
% Contator de itera��es
Partida.it  = 0;

% La�o infinito
while Partida.emOperacao
    if toc(Partida.tc) > .05
        set(BDP.status(1),'string',['Partida em modo JOGO ||||| SCAN :: ' num2str(toc(Partida.tc),'%0.3f') ' ms'])
        Partida.tc = tic;
        
        % ==============================================
        % PDI - Processamento de Imagem
        PDIsegmentar
        PDIpopular
        PDIexibir
        
        % ==============================================
        % Estrutura de controle da plataforma       
        
        JogadorControlar
  
        if Partida.emJogo
            ComunicacaoEnviar
        end
        
      

        % ==============================================
        % For�ar exibi��o dos dados
        PartidaDadosExibir
        drawnow
        % ==============================================
        % Incremento de intera��es realizadas
        Partida.it = Partida.it+1;
    end
end

% Tempo de jogo
Partida.tjf = toc(Partida.tji);
set(BDP.status(1),'string',['Log de intera��es ::::: Tempo m�dio por ciclo = ' num2str(Partida.tjf/Partida.it,'%0.3f') ' ms'])
set(BDP.status(2),'string',['Itera��es Poss�veis: ' num2str(floor(Partida.tjf/Partida.ta)) '  ::: Realizadas: ' num2str(Partida.it)])
    