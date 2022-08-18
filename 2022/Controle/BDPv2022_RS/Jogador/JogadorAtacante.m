function rBDP = JogadorAtacante(rBDP,Bola)
% Controle de posição atacante

% Direcional para a baliza
if rBDP.pLado == 1
    % Direção positiva de X
    Baliza =  750;
else
    % Direção negativa de X
    Baliza = -750;
end

% Angulo de ataque
ang  = atan2(Bola.X(2),Bola.X(1)-Baliza);
dist = 100;

rBDP.pPos.Xd(1:2,1) = [cos(ang); sin(ang)]*dist + Bola.X';
if ang < 0
    rBDP.pPos.Xd(3) =  pi + ang;
else
    rBDP.pPos.Xd(3) = -pi + ang;
end

% Jogar bola contra a parede
if abs(rBDP.pPos.Xd(2)) > 650
    rBDP.pPos.Xd(2) = -sin(ang)*dist + Bola.X(2);
end

% % Seguidor de bola
% if norm(rBDP.pPos.X(1:2,1) - rBDP.pPos.Xd(1:2,1)) < (dist+100)
%     rBDP.pPos.Xd(1:2,1) = Bola.X';
% end

% =======
% Funções a criar
% Desviar da bola

% Girar como forma de chute
% Criar temporizador de robô parado

% if abs(rBDP.pPos.Xtil(3)) > 5/180*pi || norm(rBDP.pPos.Xtil(1:2,1)) > (dist)
%     % Cinemática Inversa
%     
% else
%     % Forçar velocidades linear para chute
%     disp('entrou......')
%     rBDP.pSC.U(1) = 150;
%     rBDP.pSC.U(2) = 0;
% end

rBDP = ControleAltoNivel(rBDP);
rBDP = ControleBaixoNivel(rBDP);

% Forçar velocidades
% rBDP.pSC.U(1) = 200;
% rBDP.pSC.U(2) = 0;

% % Controle de orientação para chute
% rBDP.pSC.U(1) = 0;
% rBDP.pSC.U(2) = 0.5*(tanh(0.1*rBDP.pPos.Xtil(3)));

end