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
Partida.cobrarPenalti = 0;

Partida.PDI_Flag = 0;
PDI.pPar.AreaMin  = 10;  
PDIsegmentar
PDIpopular
PDIexibir
% Log de início
for idx = 1:3
    if strcmp(JogBDP(idx).pFuncao,'a')
%         if rBDP.pLado == 1 && JogBDP(idx).pPos.X(1) < 0 % Jogador Atacante no campo adversário
        % Direção positiva de X
            if norm(JogBDP(idx).pPos.X(1:2)' - [350 0]) < 150 && norm(Bola.X - [350 0]) < 100
            % jogador atacante e bola em posição de cobrança de pênalti
                set(Partida.status(1),'string','Cobrança de Pênalti!!!');
                set(Partida.status(2),'string','');
                Partida.cobrarPenalti = 1;
            end

%         elseif rBDP.pLado == -1 && JogBDP(idx).pPos.X(1) > 0 % Jogador Atacante no campo adversário
%         % Direção negatica de X
            if norm(JogBDP(idx).pPos.X(1:2)' - [-350 0]) < 150 && norm(Bola.X - [-350 0]) < 100
            % jogador atacante e bola em posição de cobrança de pênalti
                set(Partida.status(1),'string','Cobrança de Pênalti!!!');
                set(Partida.status(2),'string','');
                Partida.cobrarPenalti = 1;
            end
%         
%         else % caso contrário -> saída de bola normal
            set(Partida.status(1),'string','Partida em modo JOGO')
            set(Partida.status(2),'string','')
%         end
    end
end

% Variáveis de processamento de imagem
PDI.pPar.AreaMin  = 10;  % Área mínima em pixels

% Tempo de controle
Partida.tc = tic;

% Tempo de jogo
Partida.tji = tic;
% Contator de iterações
Partida.it  = 0;
if Partida.cobrarPenalti == 1
    timer = tic;
end 
% Partida.PDI_Flag = 0; 
% Laço infinito
while Partida.emJogo
    if toc(Partida.tc) > Partida.ta
        if Partida.cobrarPenalti == 1
        if toc(timer)>2
            Partida.cobrarPenalti = 0;
        end
        end
        if Partida.cobrarPenalti
            set(Partida.status(1),'string',['Cobrânça de Pênalti ||||| SCAN :: ' num2str(toc(Partida.tc),'%0.3f') ' ms'])
        else
            set(Partida.status(1),'string',['Partida em modo JOGO ||||| SCAN :: ' num2str(toc(Partida.tc),'%0.3f') ' ms'])
            %Partida.cobrarPenalti = 0;
        end
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
        ComunicacaoEnviar_backUp
        
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