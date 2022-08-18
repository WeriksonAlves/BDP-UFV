% Controlar jogador de acordo com sua função em campo
for ii = 1:3
    
    switch JogBDP(ii).pFuncao
        case 'g' % Goleiro
            JogBDP(ii) = JogadorGoleiro(JogBDP(ii),Bola);
        case 'd' % Defesa
        case 'a' % Atacante
            JogBDP(ii) = JogadorAtacante(JogBDP(ii),Bola);
    end
    
    % 19/05/19: Brandão Retiro do código a ação de atacar a bola com giro
    %     if norm(Bola.X'-JogBDP(ii).pPos.X(1:2,1)) < 75
    %         % Girar para atacar a bola
    %         if JogBDP(ii).pLado == 1 % -->
    %             if Bola.X(2) > JogBDP(ii).pPos.X(2)
    %                 JogBDP(ii).pSC.PWM(1) = -100;
    %                 JogBDP(ii).pSC.PWM(2) = +100;
    %             else
    %                 JogBDP(ii).pSC.PWM(1) = +100;
    %                 JogBDP(ii).pSC.PWM(2) = -100;
    %             end
    %         else
    %             if Bola.X(2) > JogBDP(ii).pPos.X(2)
    %                 JogBDP(ii).pSC.PWM(1) = +100;
    %                 JogBDP(ii).pSC.PWM(2) = -100;
    %             else
    %                 JogBDP(ii).pSC.PWM(1) = -100;
    %                 JogBDP(ii).pSC.PWM(2) = +100;
    %             end
    %         end
    %     else
    %         JogBDP(ii) = ControleAltoNivel(JogBDP(ii));
    %         JogBDP(ii) = ControleBaixoNivel(JogBDP(ii));
    %     end
    % 19/05/19: Brandão Retiro do código a ação de atacar a bola com giro
    
    JogBDP(ii) = ControleAltoNivel(JogBDP(ii));
    JogBDP(ii) = ControleBaixoNivel(JogBDP(ii));
    
end