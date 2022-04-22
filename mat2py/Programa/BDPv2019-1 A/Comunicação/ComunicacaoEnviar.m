% VALORES ATUALIZADOS
% 23/10/2019: Brandão
% Código padrão para envio de dados
% Analisar, pois foi alterado durante o SIA2019
COM.msg = ['B' 'D' uint8(JogBDP(1).pSC.PWM'+150) uint8(JogBDP(2).pSC.PWM'+150) uint8(JogBDP(3).pSC.PWM'+150) 'P' 10];
 

% COM.msg = ['B' 'D' Ex01_joyP3DX.m uint8(JogBDP(1).pSC.PWM'+150) uint8(JogBDP(2).pSC.PWM'+150) uint8(JogBDP(3).pSC.PWM'+150) 'P' 10];

% 19/05/19: Brandão ==================
% Teste em jogo para verificar se a visão acompanha a rotação do robô sobre
% o próprio eixo
% COM.msg = ['B' 'D' 190 110 190 110 190 110 'P' 10];
% 19/05/19: Brandão ==================
disp(JogBDP(1).pSC.PWM')
for i = 1:10%100
    fwrite(COM.Porta,COM.msg,'char');
end