function rBDP = JogadorAtacante(rBDP,Bola)
% Controle de posição atacante
if abs(rBDP.pPos.Xtil(3)) < 5/180*pi && 


% -----------------------------------------
% Controle de orientação
rBDP.pPos.Xd(3) = atan2(Bola.X(2)-rBDP.pPos.X(2),Bola.X(1)-rBDP.pPos.X(1));


rBDP.pPos.Xtil(3) = rBDP.pPos.Xd(3) - rBDP.pPos.X(3);
if abs(rBDP.pPos.Xtil(3)) > pi
    if rBDP.pPos.Xtil(3) > 0
        rBDP.pPos.Xtil(3) = rBDP.pPos.Xtil(3) - 2*pi;
    else
        rBDP.pPos.Xtil(3) = rBDP.pPos.Xtil(3) + 2*pi;
    end
end
        
disp(rBDP.pPos.Xtil(3))

rBDP.pSC.U(2) = 0.075*tanh(2.5*rBDP.pPos.Xtil(3));
disp(rBDP.pSC.U(2))

% if abs(rBDP.pPos.Xtil(3)) < 5/180*pi
%     rBDP.pPos.Xd(1:2) = Bola.X(1:2);
%     rBDP.pPos.Xtil(1:2) = rBDP.pPos.Xd(1:2) - rBDP.pPos.X(1:2);
%     rBDP.pPos.dXd(1:2) = Bola.dX;
%     rBDP.pPos.dXtil(1:2) = rBDP.pPos.dXd(1:2) - rBDP.pPos.dX(1:2);
% end
% 
% if abs(norm(rBDP.pPos.Xtil(1:2))) > 5 % mm
%     rBDP.pSC.U(1) = tanh(norm(rBDP.pPos.dXtil(1:2))) + 1*tanh(5*norm(rBDP.pPos.Xd(1:2)));
% else
%     rBDP.pSC.U(2) = 0.075*tanh(5*rBDP.pPos.Xtil(3));
% end


rBDP.pPos.Xd(1:2) = Bola.X;
rBDP.pPos.Xtil(1:2) = rBDP.pPos.Xd(1:2) - rBDP.pPos.X(1:2);
rBDP.pPos.dXd(1:2) = Bola.dX;
Bola.dX
rBDP.pPos.dXtil(1:2) = rBDP.pPos.dXd(1:2) - rBDP.pPos.dX(1:2);

% Testando a posição nos quatro quadrantes -> parar atrás da bola:
% if Bola.X(1) > 0
    if Bola.X(2) > 0
        rBDP.pPos.Xd(1:2) = Bola.X + 10*[-cos(rBDP.pPos.Xd(3)) sin(rBDP.pPos.Xd(3))];
    else
        rBDP.pPos.Xd(1:2) = Bola.X + [-50 -50];
    end
% else
%     if Bola.X(2) > 0
%         rBDP.pPos.Xd(1:2) = Bola.X + [50 50];
%     else
%         rBDP.pPos.Xd(1:2) = Bola.X + [50 -50];
%     end
% end


% Controlador de Alto Nível
kx = 0.02;
ky = 0.01;

Vx = rBDP.pPos.dXd(1) + kx*rBDP.pPos.Xtil(1);
Vy = rBDP.pPos.dXd(2) + ky*rBDP.pPos.Xtil(2);
Vp = -Vx/(rBDP.pSC.a*cos(rBDP.pSC.alpha))*sin(rBDP.pPos.X(3)) + Vy/(rBDP.pSC.a*cos(rBDP.pSC.alpha))*cos(rBDP.pPos.X(3));

rBDP.pSC.U(1) = Vx*cos(rBDP.pPos.X(3)) + Vy*sin(rBDP.pPos.X(3)) + Vp*rBDP.pSC.a*sin(rBDP.pSC.alpha);
% rBDP.pSC.U(2) = Vp;
disp(rBDP.pSC.U)


% Controlador de Baixo Nível 
% [u w] -> [w_l w_r]
% Cálculos dos valores de PWN a ser enviado aos robôs
% Definição dos limites
% Velocidade máxima das rodas
Wmax = 2;

% Limites para envia PWM
rBDP.pSC.rL = 10;
rBDP.pSC.rR = 10;
rBDP.pSC.W = [1/rBDP.pSC.rL -rBDP.pSC.d/(2*rBDP.pSC.rL); 1/rBDP.pSC.rR rBDP.pSC.d/(2*rBDP.pSC.rR)]*rBDP.pSC.U;
% rBDP.pSC.W = [1/rBDP.pSC.r -rBDP.pSC.d/(2*rBDP.pSC.r); 1/rBDP.pSC.r rBDP.pSC.d/(2*rBDP.pSC.r)]*rBDP.pSC.U;

for ii = 1:2
    if abs(rBDP.pSC.W(ii)) > Wmax
        rBDP.pSC.W(ii) = sign(rBDP.pSC.W(ii))*Wmax;
    end
    rBDP.pSC.PWM(ii) = 50*rBDP.pSC.W(ii) + 150;

end

% disp(rBDP.pSC.PWM)

end