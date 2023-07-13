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
Partida.cobrarPenalti = 0;

Partida.PDI_Flag = 0;
PDI.pPar.AreaMin  = 10;  
PDIsegmentar
PDIpopular
PDIexibir
% Log de in�cio
for idx = 1:3
    if strcmp(JogBDP(idx).pFuncao,'a')
%         if rBDP.pLado == 1 && JogBDP(idx).pPos.X(1) < 0 % Jogador Atacante no campo advers�rio
        % Dire��o positiva de X
            if norm(JogBDP(idx).pPos.X(1:2)' - [350 0]) < 150 && norm(Bola.X - [350 0]) < 100
            % jogador atacante e bola em posi��o de cobran�a de p�nalti
                set(Partida.status(1),'string','Cobran�a de P�nalti!!!');
                set(Partida.status(2),'string','');
                Partida.cobrarPenalti = 1;
            end

%         elseif rBDP.pLado == -1 && JogBDP(idx).pPos.X(1) > 0 % Jogador Atacante no campo advers�rio
%         % Dire��o negatica de X
            if norm(JogBDP(idx).pPos.X(1:2)' - [-350 0]) < 150 && norm(Bola.X - [-350 0]) < 100
            % jogador atacante e bola em posi��o de cobran�a de p�nalti
                set(Partida.status(1),'string','Cobran�a de P�nalti!!!');
                set(Partida.status(2),'string','');
                Partida.cobrarPenalti = 1;
            end
%         
%         else % caso contr�rio -> sa�da de bola normal
            set(Partida.status(1),'string','Partida em modo JOGO')
            set(Partida.status(2),'string','')
%         end
    end
end

% Vari�veis de processamento de imagem
PDI.pPar.AreaMin  = 10;  % �rea m�nima em pixels

% Tempo de controle
Partida.tc = tic;

% Tempo de jogo
Partida.tji = tic;
% Contator de itera��es
Partida.it  = 0;
if Partida.cobrarPenalti == 1
    timer = tic;
end 
% Partida.PDI_Flag = 0; 
% La�o infinito
while Partida.emJogo
    if toc(Partida.tc) > Partida.ta
        if Partida.cobrarPenalti == 1
        if toc(timer)>2
            Partida.cobrarPenalti = 0;
        end
        end
        if Partida.cobrarPenalti
            set(Partida.status(1),'string',['Cobr�n�a de P�nalti ||||| SCAN :: ' num2str(toc(Partida.tc),'%0.3f') ' ms'])
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
        % Enviar comandos aos rob�s
        ComunicacaoEnviar_backUp
        
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