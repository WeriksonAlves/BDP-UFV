% VALORES ATUALIZADOS
% 23/10/2019: Brand�o
% C�digo padr�o para envio de dados
% Analisar, pois foi alterado durante o SIA2019
COM.msg = ['B' 'D' uint8(JogBDP(1).pSC.PWM'+150) uint8(JogBDP(2).pSC.PWM'+150) uint8(JogBDP(3).pSC.PWM'+150) 'P' 10];
 

% COM.msg = ['B' 'D' Ex01_joyP3DX.m uint8(JogBDP(1).pSC.PWM'+150) uint8(JogBDP(2).pSC.PWM'+150) uint8(JogBDP(3).pSC.PWM'+150) 'P' 10];

% 19/05/19: Brand�o ==================
% Teste em jogo para verificar se a vis�o acompanha a rota��o do rob� sobre
% o pr�prio eixo
% COM.msg = ['B' 'D' 190 110 190 110 190 110 'P' 10];
% 19/05/19: Brand�o ==================
disp(JogBDP(1).pSC.PWM')
for i = 1:10%100
    fwrite(COM.Porta,COM.msg,'char');
end