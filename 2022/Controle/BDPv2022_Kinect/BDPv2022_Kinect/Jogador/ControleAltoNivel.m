function rBDP = ControleAltoNivel(rBDP)

kx   = 0.02;
ky   = 0.02;
kpsi = 0.05;

rBDP.pSC.a = 10;

% Error
ux = rBDP.pPos.dXd(1) + kx*(rBDP.pPos.Xd(1)-rBDP.pPos.X(1));
uy = rBDP.pPos.dXd(2) + ky*(rBDP.pPos.Xd(2)-rBDP.pPos.X(2));

% Variables definition
% Inverse Kinematic matrix
if abs(rBDP.pSC.alpha) ~= pi/2 && rBDP.pSC.alpha ~= 0
    % Controller
    Ud(2) = (-sin(rBDP.pPos.X(3) )*ux + cos(rBDP.pPos.X(3) )*uy)/(-rBDP.pSC.a*cos(rBDP.pSC.alpha));
    Ud(1) = ux*cos(rBDP.pPos.X(3) ) + uy*sin(rBDP.pPos.X(3) ) + rBDP.pSC.a*sin(rBDP.pSC.alpha)*Ud(2);
else
    urBDP.pPos.X(3)  = atan2(uy,ux) - rBDP.pPos.X(3) ;
    Ud(2) = kpsi*urBDP.pPos.X(3) ;
    Ud(1) = cos(rBDP.pPos.X(3) )*ux + sin(rBDP.pPos.X(3) )*uy + rBDP.pSC.a*Ud(2);
end

rBDP.pSC.U(1) = Ud(1);
rBDP.pSC.U(2) = Ud(2);
end