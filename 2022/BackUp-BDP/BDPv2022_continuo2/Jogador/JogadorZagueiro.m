function rBDP = JogadorZagueiro(rBDP,Bola, Bola3)
dif = ([Bola.X 0]' - rBDP.pPos.X );
if rBDP.pLado == 1
    if Bola.X(1) > 0  
        rBDP.pPos.Xd = [Bola3.X(1) + 350 Bola3.X(2)*3 0]';
    %caso contrário repetir comportamento do atacante
    end
    if Bola.X(1) < 0 && Bola.X(1) > -650 || (norm(dif) < 100) 
    %
    if ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' - [2*Bola.dX(1) 0 0]';
   
    elseif  ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
    end
    if Bola.X(1) < -650 && Bola.X(2) > 380 || (norm(dif) < 100)
    %
    if ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' - [2*Bola.dX(1) 0 0]';
   
    elseif  ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
    %
    end
    if Bola.X(1) < -650 && Bola.X(2) < -380 || (norm(dif) < 100)
    if ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' - [2*Bola.dX(1) 0 0]';
   
    elseif  ((Bola.dX(1) < 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
    end

if (norm(dif) < 60)
 
    if rBDP.pPos.X(2) > -200 && rBDP.pPos.X(2) < 200 
 
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [-100 100]';
            else
                rBDP.pSC.PWM = [100 -100]';
            end

    end
    if rBDP.pPos.X(2) < -200 || rBDP.pPos.X(2) > 200
   

            if Bola.X(2) < 0
                rBDP.pSC.PWM = [100 -100]';
            else
                rBDP.pSC.PWM = [-100 100]';
            end

    end
else
rBDP.pPos.Xtil = (rBDP.pPos.Xd - rBDP.pPos.X);% de posição
rBDP = ControleAltoNivel(rBDP);
rBDP = ControleBaixoNivel(rBDP);
end
end
%%
if rBDP.pLado == -1
    if Bola.X(1) < 0  
        rBDP.pPos.Xd = [Bola3.X(1) + 1100 Bola3.X(2)*3 0]';
    %caso contrário repetir comportamento do atacante
    end
    if Bola.X(1) > 0 && Bola.X(1) < 650 || (norm(dif) < 100) 
    %
    if ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' + [1*Bola.dX(1) 0 0]';
   
    elseif  ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
    end
    if Bola.X(1) > 650 && Bola.X(2) > 380 || (norm(dif) < 100)
    %
    if ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' + [1*Bola.dX(1) 0 0]';
   
    elseif  ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
    %
    end
    if Bola.X(1) > 650 && Bola.X(2) < -380 || (norm(dif) < 100)
    if ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) < Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]' + [1*Bola.dX(1) 0 0]';
   
    elseif  ((Bola.dX(1) > 0)) && ((rBDP.pPos.X(1) > Bola.X(1)))
        rBDP.pPos.Xd = [Bola.X 0]';
 
    else
        rBDP.pPos.Xd = [Bola.X 0]';
    end
    end

if (norm(dif) < 60)
 
    if rBDP.pPos.X(2) > -200 && rBDP.pPos.X(2) < 200 
 
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [100 -100]';
            else
                rBDP.pSC.PWM = [-100 100]';
            end

    end
    if rBDP.pPos.X(2) < -200 || rBDP.pPos.X(2) > 200
   
            if Bola.X(2) < 0
                rBDP.pSC.PWM = [-100 100]';
            else
                rBDP.pSC.PWM = [100 -100]';
            end
    end
else
rBDP.pPos.Xtil = (rBDP.pPos.Xd - rBDP.pPos.X);% de posição
rBDP = ControleAltoNivel(rBDP);
rBDP = ControleBaixoNivel(rBDP);
end
end
end