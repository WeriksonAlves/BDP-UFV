% Controlar jogador de acordo com sua função em campo
for ii = 1:3
    switch JogBDP(ii).pFuncao
        case 'g' % Goleiro
            JogBDP(ii) = JogadorGoleiro(JogBDP(ii), Bola, Bola3);
        case 'd' % Defesa
            JogBDP(ii) = JogadorZagueiro(JogBDP(ii), Bola, Bola3);
        case 'a' % Atacante
            JogBDP(ii) = JogadorAtacante(JogBDP(ii),Bola,Partida);

    end    
end