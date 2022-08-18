Partida.Dados = get(Partida.Tabela,'Data');

for ii = 1:3
    JogBDP(ii).pPos.X   = [Partida.Dados(1,2*ii-1:2*ii) Partida.Dados(3,2*ii-1)*pi/180]';
    JogBDP(ii).pPos.Xd  = [Partida.Dados(2,2*ii-1:2*ii) 0]';
    JogBDP(ii).pSC.U    =  Partida.Dados(4,2*ii-1:2*ii)';
    JogBDP(ii).pSC.W    =  Partida.Dados(5,2*ii-1:2*ii)';
    JogBDP(ii).pSC.PWM  =  Partida.Dados(6,2*ii-1:2*ii)';
    JogBDP(ii).pSC.GAN  =  Partida.Dados(7,2*ii-1:2*ii)';
    JogBDP(ii).pSC.GBN  =  Partida.Dados(8,2*ii-1:2*ii)';
end
disp('oi')
PDIexibir