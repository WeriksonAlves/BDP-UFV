% Parâmetros partida

Partida.Dados = get(Partida.Tabela,'Data');


Partida.Dados(1,:) = [JogBDP(1).pPos.X(1:2,1)'  JogBDP(2).pPos.X(1:2,1)'  JogBDP(3).pPos.X(1:2,1)' ];
Partida.Dados(2,:) = [JogBDP(1).pPos.Xd(1:2,1)' JogBDP(2).pPos.Xd(1:2,1)' JogBDP(3).pPos.Xd(1:2,1)'];
Partida.Dados(3,:) = [JogBDP(1).pPos.X(3,1) 0   JogBDP(2).pPos.X(3,1) 0   JogBDP(3).pPos.X(3,1) 0  ]*180/pi;
Partida.Dados(4,:) = [JogBDP(1).pSC.U'   JogBDP(2).pSC.U'   JogBDP(3).pSC.U'];
Partida.Dados(5,:) = [JogBDP(1).pSC.W'   JogBDP(2).pSC.W'   JogBDP(3).pSC.W'];
Partida.Dados(6,:) = [JogBDP(1).pSC.PWM' JogBDP(2).pSC.PWM' JogBDP(3).pSC.PWM'];
Partida.Dados(7,:) = [JogBDP(1).pSC.GAN' JogBDP(2).pSC.GAN' JogBDP(3).pSC.GAN'];
% Partida.Dados(8,:) = [JogBDP(1).pSC.GBN' JogBDP(2).pSC.GBN' JogBDP(3).pSC.GBN'];
% Partida.Dados(8,:) = [Bola.X(1) Bola.X(2) (ang + sign(-atan2(Bola.X(2)-JogBDP(1).pPos.X(2,1),(Bola.X(1)-JogBDP(1).pPos.X(1,1))))*rad2deg(JogBDP(1).pPos.X(3,1))) 0 0 0 ];
Partida.Dados(8,:) = [Bola.X(1) Bola.X(2) ang_dif Bola2.X(1) Bola2.X(2) rad2deg(Bola2.ang)];


set(Partida.Tabela,'Data',Partida.Dados);
