function rBDP = ControleAltoNivel(rBDP)

if norm(rBDP.pPos.Xtil(1:2)) < 300
% 
k1 = 0.7;%0.01
k2 = 50;%5 

a = 50;
gl = .1; 
ga = .1;
rBDP.pPos.Xtil = (rBDP.pPos.Xd - rBDP.pPos.X);% de posição                
A = [k1*(1-exp(-k2* (norm(rBDP.pPos.Xtil(1:2)))))*rBDP.pPos.Xtil(1);% matriz de controle
      k1*(1-exp(-k2* norm(rBDP.pPos.Xtil(1:2))))*rBDP.pPos.Xtil(2)];% matriz de controle

G = [gl 0;
      0 ga];
K = [cos(rBDP.pPos.X(3)) -a*sin(rBDP.pPos.X(3));% K é a matriz de rotação
       sin(rBDP.pPos.X(3)) a*cos(rBDP.pPos.X(3))];% do modelo cinemático 
Ud = K\G*A;

rBDP.pSC.U(1) = Ud(1);% velocidade linear
rBDP.pSC.U(2) = Ud(2);% velocidade angular

% Controlador 
else
kx   = 0.25;
ky   = 0.2;

rBDP.pSC.a = 300;
ux = rBDP.pPos.dXd(1) + kx*(rBDP.pPos.Xd(1)-rBDP.pPos.X(1));
uy = rBDP.pPos.dXd(2) + ky*(rBDP.pPos.Xd(2)-rBDP.pPos.X(2));

Ud(2) = (-sin(rBDP.pPos.X(3) )*ux + cos(rBDP.pPos.X(3) )*uy)/(-rBDP.pSC.a*cos(rBDP.pSC.alpha));
Ud(1) = ux*cos(rBDP.pPos.X(3) ) + uy*sin(rBDP.pPos.X(3) ) + rBDP.pSC.a*sin(rBDP.pSC.alpha)*Ud(2);

rBDP.pSC.U(1) = Ud(1);
rBDP.pSC.U(2) = Ud(2);


end
end
