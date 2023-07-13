% Rotina para teste
% COM.msg = ['B' 'D' 160 140 160 140 160 140 'P' 10];

% Descrição da mensagem
% Com.msg =
% 1- caracter de cabeçalho = B
% 2- caracter de cabeçalho = D
% 3- caracter da roda Esquerda R1 (< 150 p/ trás)
% 4- caracter da roda Direita R1 (< 150 p/ trás)

% COM.msg = ['B' 'D' 100 150 150 150 150 150 'P' 10];

Wmax = 2;

% Atuar usando Joystick
% if sum(button(joy))
%     for ii = 1:3
%         JogBDP(ii).pSC.U = [-axis(joy,2)*100; axis(joy,3)]*button(joy,ii);
% 
%         % Limites para envia PWM
%         JogBDP(ii).pSC.rL = 10;
%         JogBDP(ii).pSC.rR = 10;
%         JogBDP(ii).pSC.W = [1/JogBDP(ii).pSC.rL -JogBDP(ii).pSC.d/(2*JogBDP(ii).pSC.rL); 1/JogBDP(ii).pSC.rR JogBDP(ii).pSC.d/(2*JogBDP(ii).pSC.rR)]*JogBDP(ii).pSC.U;
%         % rBDP.pSC.W = [1/rBDP.pSC.r -rBDP.pSC.d/(2*rBDP.pSC.r); 1/rBDP.pSC.r rBDP.pSC.d/(2*rBDP.pSC.r)]*rBDP.pSC.U;
% 
%         for jj = 1:2
%             if abs(JogBDP(ii).pSC.W(jj)) > Wmax
%                 JogBDP(ii).pSC.W(jj) = sign(JogBDP(ii).pSC.W(jj))*Wmax;
%             end
%             JogBDP(ii).pSC.PWM(jj) = 50*JogBDP(ii).pSC.W(jj) + 150;
% 
%         end
% 
%     end
% end

% for ii = 1:3
%     disp(JogBDP(ii).pSC.W)
% end

COM.msg = ['B' 'D' uint8(JogBDP(1).pSC.PWM(1)) uint8(JogBDP(1).pSC.PWM(2)) ...
    uint8(JogBDP(2).pSC.PWM(1)) uint8(JogBDP(2).pSC.PWM(2)) ...
    uint8(JogBDP(3).pSC.PWM(1)) uint8(JogBDP(3).pSC.PWM(2)) 'P' 10];


fwrite(COM.Porta,COM.msg,'char');

