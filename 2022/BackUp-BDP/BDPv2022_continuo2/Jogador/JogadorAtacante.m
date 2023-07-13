function rBDP = JogadorAtacante(rBDP,Bola)

% Controle de posição atacante

% rBDP.pPos.Xa = rBDP.pPos.Xd;

rBDP.pPos.Xd = [Bola.X 0]';
% Chegar em um ponto atrás da bola caso o robo esteja a frente da bola

if rBDP.pLado == 1 
    if ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' - [1*Bola.dX(1) 0 0]';
   
    elseif  ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
end
if rBDP.pLado == -1 
    if ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' + [1*Bola.dX(1) 0 0]';
   
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
if (norm(dif) < 60)
    
    if rBDP.pPos.X(2) > -200 && rBDP.pPos.X(2) < 200 
 
    if rBDP.pLado == 1 
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [-100 100]';
            else
                rBDP.pSC.PWM = [100 -100]';
            end
    end
    if rBDP.pLado == -1
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [100 -100]';
            else
                rBDP.pSC.PWM = [-100 100]';
            end
    end
    end
    if rBDP.pPos.X(2) < -200 || rBDP.pPos.X(2) > 200
   
     if rBDP.pLado == 1 
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [100 -100]';
            else
                rBDP.pSC.PWM = [-100 100]';
            end
     end
        if rBDP.pLado == -1
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [-100 100]';
            else
                rBDP.pSC.PWM = [100 -100]';
            end
        end

    end
%%%% Caso a bola não esteja perto o suficiente do robô ele se encaminha até
%%%% a bola
else
        if Bola.X(1) <0 && rBDP.pLado == 1
            rBDP.pPos.Xd(1:2) = [150 Bola.X(2)];
        end
        if Bola.X(1) >0 && rBDP.pLado == -1
            rBDP.pPos.Xd(1:2) = [-150 Bola.X(2)];
        end

        rBDP.pPos.Xtil = (rBDP.pPos.Xd - rBDP.pPos.X);
        rBDP = ControleAltoNivel(rBDP);
        rBDP = ControleBaixoNivel(rBDP);
end


    
    
end
%Implementar corrida com a bola na direção do gol 

%Implementar cobrança de pênalti



    


%limitar atuação do robô ao campo de ataque

