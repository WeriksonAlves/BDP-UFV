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
Partida.PDI_Flag = 0; 
% Laço infinito
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
        % Enviar comandos aos robôs
        ComunicacaoEnviar
        
        % ==============================================
        % Forçar exibição dos dados
        PartidaDadosExibir
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