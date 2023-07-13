function rBDP = JogadorGoleiro(rBDP,Bola, Bola3)
% Controle de posição goleiro
if rBDP.pLado == 1
    % Direção positiva de X
    Baliza =  750;
else
    % Direção negativa de X
    Baliza = -750;
end

dif = ([Bola.X 0]' - rBDP.pPos.X );
if norm(dif) < 80 
 
    if Bola.X(2) > 0 && Baliza == 750
        rBDP.pSC.PWM = [-100 100]';
    end
    if Bola.X(2) < 0 && Baliza == -750
        rBDP.pSC.PWM = [-100 100]';
    end
    if Bola.X(2) < 0 && Baliza == 750
        rBDP.pSC.PWM = [100 -100]';
    end
    if Bola.X(2) > 0 && Baliza == -750
        rBDP.pSC.PWM = [100 -100]';
    end
elseif rBDP.pLado == 1 && Bola.X(1) < -600 && Bola.X(2) > -350 && Bola.X(2) < 350
    rBDP.pPos.Xd = [Bola.X 0]'   ;
    rBDP.pPos.Xtil = (rBDP.pPos.Xd - rBDP.pPos.X);% de posição
    rBDP = ControleAltoNivel(rBDP);
    rBDP = ControleBaixoNivel(rBDP);
elseif rBDP.pLado == -1 && Bola.X(1) > 600 && Bola.X(2) > -350 && Bola.X(2) < 350
    rBDP.pPos.Xd = [Bola.X 0]'   ;
    rBDP.pPos.Xtil = (rBDP.pPos.Xd - rBDP.pPos.X);% de posição
    rBDP = ControleAltoNivel(rBDP);
    rBDP = ControleBaixoNivel(rBDP);
else
    if rBDP.pLado == 1
        rBDP.pPos.Xd = [Bola3.X(1) + 20 Bola.X(2)*250/650 0]';
    else 
         rBDP.pPos.Xd = [-Bola3.X(1) - 20 Bola.X(2)*250/650 0]';
    end
    rBDP.pPos.Xtil = (rBDP.pPos.Xd - rBDP.pPos.X);% de posição
    if norm(rBDP.pPos.Xtil(1:2)) < 50
        rBDP.pSC.PWM = [0 0]';
    else
        
    rBDP = ControleAltoNivel(rBDP);
    rBDP = ControleBaixoNivel(rBDP);
    end
    
end