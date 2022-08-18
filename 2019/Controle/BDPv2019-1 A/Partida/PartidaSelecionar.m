% Selecionar itens  da partida

% Cor do time: 1: Amarelo || 2: Ciano
for ii = 1:3
    if get(Partida.CorTime(1),'Value')
        JogBDP(ii).pTime = 'y';
        JogAdv(ii).pTime = 'c';
    else
        JogBDP(ii).pTime = 'c';
        JogAdv(ii).pTime = 'y';
    end
    
    % Lado de ataque:
    % 1: Direção nevativa de x
    % 2: Direção positiva de x
    if get(Partida.Lado(1),'Value')
        JogBDP(ii).pLado = -1;
    else
        JogBDP(ii).pLado =  1;
    end
    
    % Habilitar jogador
    switch get(Partida.Camisa(ii),'Value')
        case 1
            JogBDP(ii).pCor = 'r';
        case 2
            JogBDP(ii).pCor = 'g';
        case 3
            JogBDP(ii).pCor = 'b';
        case 4
            JogBDP(ii).pCor = 'm';
    end
    
    switch get(Partida.Funcao(ii),'Value')
        case 1
            JogBDP(ii).pFuncao = 'g';
        case 2
            JogBDP(ii).pFuncao = 'd';
        case 3
            JogBDP(ii).pFuncao = 'a';
    end
end

if Partida.Camisa(1).Value==1||Partida.Camisa(2).Value==1||Partida.Camisa(3).Value==1
    Cores.Usadas(1)=1; % Vermelho
else
    Cores.Usadas(1)=0;
end
if Partida.Camisa(1).Value==2||Partida.Camisa(2).Value==2||Partida.Camisa(3).Value==2
    Cores.Usadas(4)=1; % Verde
else
    Cores.Usadas(4)=0;
end
if Partida.Camisa(1).Value==3||Partida.Camisa(2).Value==3||Partida.Camisa(3).Value==3
    Cores.Usadas(6)=1; % Azul
else
    Cores.Usadas(6)=0;
end
if Partida.Camisa(1).Value==4||Partida.Camisa(2).Value==4||Partida.Camisa(3).Value==4
    Cores.Usadas(7)=1; % Magenta
else
    Cores.Usadas(7)=0;
end


