function iVariaveisControle(rBDP)

% Dados do jogador
rBDP.pPos.X   = zeros(3,1);  % Postura atual
rBDP.pPos.Xa  = zeros(3,1);  % Postura anterior
rBDP.pPos.Xd  = zeros(3,1);  % Postura desejada
rBDP.pPos.dX  = zeros(3,1);  % Derivada da postura atual
rBDP.pPos.dXd = zeros(3,1);  % Derivada da postura desejada

rBDP.pSC.a     = 0; % Distância centro ao ponto de controle
rBDP.pSC.alpha = 0;  % Angulo de controle
rBDP.pSC.r     = 20; % Raio da roda
rBDP.pSC.d     = 75; % Larguda do robôs
rBDP.pSC.U     = zeros(2,1);
rBDP.pSC.W     = zeros(2,1);
rBDP.pSC.PWM   = zeros(2,1);
rBDP.pSC.GAN   = [80; 0.001];
rBDP.pSC.GBN   = zeros(2,1);

end