function rBDP = JogadorAtacante(rBDP,Bola,Partida)

% Controle de posição atacante

rBDP.pPos.Xa = rBDP.pPos.Xd;

rBDP.pPos.Xd = [Bola.X 0]';

% rBDP.pPos.dXd = [Bola.dX*0.1 0]'; 

% Chegar em um ponto atrás da bola caso o robo esteja a frente da bola
if rBDP.pLado == 1 
    angbolagol = atan2(-Bola.X(2), 750 - Bola.X(1));
    if ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' - [cos(angbolagol) -sin(angbolagol) 0; sin(angbolagol) cos(angbolagol) 0;0 0 1]*[100 0 0]';
%         rBDP.pPos.Xd = [Bola.X 0]';
   
    elseif  ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
end
if rBDP.pLado == -1 
    angbolagol = atan2(-Bola.X(2), 750 - Bola.X(1));
    if ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
%         rBDP.pPos.Xd = [Bola.X 0]';
        rBDP.pPos.Xd = [Bola.X 0]' + [cos(angbolagol) -sin(angbolagol) 0; sin(angbolagol) cos(angbolagol) 0;0 0 1]*[100 0 0]';
    elseif  ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
end


%%%%Chuta a bola para o gol caso a distância entre o jogador e a bola seja
%%%%menor que determinado valor.
%%%%O sentido do giro para o chute depende da posição do jogador no campo

dif = ([Bola.X 0]' - rBDP.pPos.X );
if (norm(dif) < 80)
    
    if rBDP.pPos.X(2) > -350 && rBDP.pPos.X(2) < 350 
 
    if rBDP.pLado == 1 
            if Bola.X(2) < 0
                if rBDP.pPos.X(2) < Bola.X(2)
                    rBDP.pSC.PWM = [-90 90]';
                else
                    rBDP.pSC.PWM = [90 -90]';
                end
                if ((-rad2deg(angbolagol) + rad2deg(rBDP.pPos.X(3))) < 30) && Bola.X(1) > -50
                    rBDP.pSC.PWM = [100 100]';
                end

            else
                if rBDP.pPos.X(2) > Bola.X(2)
                    rBDP.pSC.PWM = [90 -90]';
                else
                    rBDP.pSC.PWM = [-90 90]';
                end
                if ((-rad2deg(angbolagol) + rad2deg(rBDP.pPos.X(3))) < 30) && Bola.X(1) > -50
                    rBDP.pSC.PWM = [100 100]';
                end
            end
    end
    if rBDP.pLado == -1
            if Bola.X(2) < 0
                if rBDP.pPos.X(2) < Bola.X(2)
                rBDP.pSC.PWM = [90 -90]';
                else
                    rBDP.pSC.PWM = [-90 90]';
                end
                if (((-rad2deg(angbolagol) + rad2deg(rBDP.pPos.X(3)))) < 30) && Bola.X(1) < 50
                        rBDP.pSC.PWM = [100 100]';
                end
            else
                if rBDP.pPos.X(2) > Bola.X(2)   
                    rBDP.pSC.PWM = [-90 90]';
                else
                    rBDP.pSC.PWM = [90 -90]';
                end
                if (((-rad2deg(angbolagol) + rad2deg(rBDP.pPos.X(3)))) < 30) && (Bola.X(1) < 50)
                    rBDP.pSC.PWM = [100 100]';
                end
            end
    end
    end
    if rBDP.pPos.X(2) < -350 || rBDP.pPos.X(2) > 350
   
     if rBDP.pLado == 1 
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [90 -90]';
            else
                rBDP.pSC.PWM = [-90 90]';
            end
     end
        if rBDP.pLado == -1
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [-90 90]';
            else
                rBDP.pSC.PWM = [90 -90]';
            end
        end

    end
%%%% Caso a bola não esteja perto o suficiente do robô ele se encaminha até
%%%% a bola
else
        if Bola.X(1) < -300 && rBDP.pLado == 1
            rBDP.pPos.Xd(1:2) = [-300 Bola.X(2)];
        end
        if Bola.X(1) > 300 && rBDP.pLado == -1
            rBDP.pPos.Xd(1:2) = [300 Bola.X(2)];
        end

        rBDP.pPos.Xtil = (rBDP.pPos.Xd - rBDP.pPos.X);
        rBDP = ControleAltoNivel(rBDP);
        rBDP = ControleBaixoNivel(rBDP);
end

%Implementar cobrança de pênalti
if Partida.cobrarPenalti == 1
    cobrarPenalti(rBDP,Bola,Partida);
    
    rBDP.pPar.timerPenalti = tic;
end
    
    
end
%Implementar corrida com a bola na direção do gol 



function rBDP = cobrarPenalti(rBDP,Bola,Partida)
disp('oi')
% Direção positiva de X                          % Direção negatica de X
if (rBDP.pLado == 1 && rBDP.pPos.X(1) > 0) || (rBDP.pLado == -1 && rBDP.pPos.X(1) < 0)
    % Jogador Atacante no campo do BDP
    Partida.cobrarPenalti = 0;
    disp('1')
    PWMmax = 70; % chute com impacto; para empurrar, testar valores menores que 70
%     rBDP.pSC.PWM = [70+tanh(toc(rBDP.pPar.timerPenalti))*PWMmax 70+tanh(toc(rBDP.pPar.timerPenalti))*PWMmax]';
    rBDP.pSC.PWM = [90 90]';
    return;
elseif (rBDP.pLado == 1 && rBDP.pPos.X(1) < 0) || (rBDP.pLado == -1 && rBDP.pPos.X(1) > 0)
    % Jogador Atacante no campo adversário
    if norm(Bola.X - [375 0])> 150 % Chutou a bola -> volta para condição normal de jogo
        disp(Partida.cobrarPenalti)
        Partida.cobrarPenalti = 0;
        disp(Partida.cobrarPenalti)
        disp('2')
        PWMmax = 100; % chute com impacto; para empurrar, testar valores menores que 70
        rBDP.pSC.PWM = [90 90]';%[70+tanh(toc(rBDP.pPar.timerPenalti))*PWMmax 70+tanh(toc(rBDP.pPar.timerPenalti))*PWMmax];
        return ;
    end
end


    


%limitar atuação do robô ao campo de ataque
end
