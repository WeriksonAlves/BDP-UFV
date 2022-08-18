% Somar 100 para casos de valores negativos

% COM.msg = ['B' 'D' 22 uint8(JogBDP(1).pSC.PWM') uint8(JogBDP(2).pSC.PWM')+16 uint8(JogBDP(3).pSC.PWM')+16 'P'];

COM.msg = ['B' 'D' 150 150 150 150 180 250, 'P' 10]; % Valor real é -150

COM.msg = ['B' 'D' uint8(JogBDP(1).pSC.PWM'+150) uint8(JogBDP(2).pSC.PWM'+150) uint8(JogBDP(3).pSC.PWM'+150) 'P' 10];
 
% fprintf(COM.Porta,COM.msg);

fwrite(COM.Porta,COM.msg,'char');
