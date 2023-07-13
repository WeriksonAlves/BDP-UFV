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