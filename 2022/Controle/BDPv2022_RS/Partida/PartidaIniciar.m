clc

% Relacionar time, camisa e função
PartidaSelecionar
% ==============================================
% Comunicação com o robô
ComunicacaoIniciar

% ==============================================
% Iniciar Partida
set(Partida.Botoes(4),'Enable','off')
Partida.emJogo = 1;

% Log de início
set(Partida.status(1),'string','Partida em modo JOGO')
set(Partida.status(2),'string','')

% Variáveis de processamento de imagem
PDI.pPar.AreaMin  = 10;  % Área mínima em pixels

% Tempo de controle
Partida.tc = tic;

% Tempo de jogo
Partida.tji = tic;
% Contator de iterações
Partida.it  = 0;

% Laço infinito
while Partida.emJogo
    if toc(Partida.tc) > Partida.ta
        set(Partida.status(1),'string',['Partida em modo JOGO ||||| SCAN :: ' num2str(toc(Partida.tc),'%0.3f') ' ms'])
        Partida.tc = tic;
        
        % ==============================================
        % PDI - Processamento de Imagem
        disp('-------------------------------------')
        tic,PDIsegmentar,toc
        tic,PDIpopular,toc
        tic,PDIexibir,toc
        % ==============================================
        % Estrutura de controle da plataforma
        tic,JogadorControlar,toc
        
        % ==============================================
        % Enviar comandos aos robôs
%         tic,ComunicacaoEnviar,toc
        
        % ==============================================
        % Forçar exibição dos dados
        tic,PartidaDadosExibir,toc
        drawnow
        % ==============================================
        % Incremento de interações realizadas
        Partida.it = Partida.it+1;
    end
end

% Tempo de jogo
Partida.tjf = toc(Partida.tji);
set(Partida.status(1),'string',['Log de interações ::::: Tempo médio por ciclo = ' num2str(Partida.tjf/Partida.it,'%0.3f') ' ms'])
set(Partida.status(2),'string',['Iterações Possíveis: ' num2str(floor(Partida.tjf/Partida.ta)) '  ::: Realizadas: ' num2str(Partida.it)])