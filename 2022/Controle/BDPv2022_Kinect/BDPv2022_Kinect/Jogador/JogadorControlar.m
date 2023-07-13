% Controlar jogador de acordo com sua função em campo
for ii = 1:3
    switch JogBDP(ii).pFuncao
        case 'g' % Goleiro
        case 'd' % Defesa
        case 'a' % Atacante
            JogBDP(ii) = JogadorAtacante(JogBDP(ii),Bola);
    end    
end