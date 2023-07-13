clc

% Relacionar time, camisa e fun��o
PartidaSelecionar
% ==============================================
% Comunica��o com o rob�
ComunicacaoIniciar

% ==============================================
% Iniciar Partida
set(Partida.Botoes(4),'Enable','off')
Partida.emJogo = 1;

% Log de in�cio
set(Partida.status(1),'string','Partida em modo JOGO')
set(Partida.status(2),'string','')

% Vari�veis de processamento de imagem
PDI.pPar.AreaMin  = 10;  % �rea m�nima em pixels

% Tempo de controle
Partida.tc = tic;

% Tempo de jogo
Partida.tji = tic;
% Contator de itera��es
Partida.it  = 0;
Partida.PDI_Flag = 0; 
% La�o infinito
while Partida.emJogo
    if toc(Partida.tc) > Partida.ta
        set(Partida.status(1),'string',['Partida em modo JOGO ||||| SCAN :: ' num2str(toc(Partida.tc),'%0.3f') ' ms'])
        Partida.tc = tic;
        
        % ==============================================
        % PDI - Processamento de Imagem
  %      disp('-------------------------------------')
        PDIsegmentar
        PDIpopular
        PDIexibir
        % ==============================================
        % Estrutura de controle da plataforma
        JogadorControlar
        
        % ==============================================
        % Enviar comandos aos rob�s
        ComunicacaoEnviar
        
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
set(Partida.status(1),'string',['Log de intera��es ::::: Tempo m�dio por ciclo = ' num2str(Partida.tjf/Partida.it,'%0.3f') ' ms'])
set(Partida.status(2),'string',['Itera��es Poss�veis: ' num2str(floor(Partida.tjf/Partida.ta)) '  ::: Realizadas: ' num2str(Partida.it)])