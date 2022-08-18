function rBDP = ControleAltoNivel(rBDP)

kx   = 1;
ky   = 1;
% kpsi = 5;

rBDP.pSC.a = 100;

% Error

ux = rBDP.pPos.dXd(1) + kx*(rBDP.pPos.Xd(1)-rBDP.pPos.X(1))
uy = rBDP.pPos.dXd(2) + ky*(rBDP.pPos.Xd(2)-rBDP.pPos.X(2));

% Variables definition
% Inverse Kinematic matrix
% if abs(rBDP.pSC.alpha) ~= pi/2 && rBDP.pSC.alpha ~= 0
%     % Controller
%     Ud(2) = (-sin(rBDP.pPos.X(3) )*ux + cos(rBDP.pPos.X(3) )*uy)/(-rBDP.pSC.a*cos(rBDP.pSC.alpha));
%     Ud(1) = ux*cos(rBDP.pPos.X(3) ) + uy*sin(rBDP.pPos.X(3) ) + rBDP.pSC.a*sin(rBDP.pSC.alpha)*Ud(2);
% else
%     urBDP.pPos.X(3)  = atan2(uy,ux) - rBDP.pPos.X(3) ;
%     Ud(2) = kpsi*urBDP.pPos.X(3) ;
%     Ud(1) = cos(rBDP.pPos.X(3) )*ux + sin(rBDP.pPos.X(3) )*uy + rBDP.pSC.a*Ud(2);
% end

Ud = [cos(rBDP.pPos.X(3)), -rBDP.pSC.a*sin(rBDP.pPos.X(3)); ...
    sin(rBDP.pPos.X(3)), rBDP.pSC.a*cos(rBDP.pPos.X(3))]\[ux; uy];


rBDP.pSC.U(1) = 250*tanh(Ud(1)/250); % umax = 340 [mm/s]/// tava 250*
rBDP.pSC.U(2) = 1*tanh(Ud(2));      % wmax = 10 [rad/s] ou 600 [°/s]
end