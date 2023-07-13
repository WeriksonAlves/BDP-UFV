function rBDP = ControleBaixoNivel(rBDP)

% Cálculos dos valores de PWN a ser enviado aos robôs
% Definição dos limites
% Velocidade máxima das rodas
Wmax = 17; % 340 umax / 20 raio da roda/// tava 17

% Limites para envia PWM
limPWMp = [30 50];  % Velocidade positiva
limPWMn = [-50 -30]; % Velocidade negativa

K2 = [1/2, 1/2; 1/rBDP.pSC.d, -1/rBDP.pSC.d];

%  CRIAR: Normalizar valores entre -100 e 100%
rBDP.pSC.W = 1/rBDP.pSC.r*(K2\rBDP.pSC.U);

for ii = 1:2
    if abs(rBDP.pSC.W(ii)) > Wmax
        rBDP.pSC.W(ii) = sign(rBDP.pSC.W(ii))*Wmax;
    end
    if rBDP.pSC.W(ii) > 0
        rBDP.pSC.PWM(ii) =  (limPWMp(2)-limPWMp(1))/Wmax*rBDP.pSC.W(ii) + limPWMp(1);
    else
        rBDP.pSC.PWM(ii) = -(limPWMn(2)-limPWMn(1))/Wmax*rBDP.pSC.W(ii) + limPWMn(1);
    end
end

rD = rBDP.pSC.PWM(1);
rE = rBDP.pSC.PWM(2);

rBDP.pSC.PWM(1) = rE;
rBDP.pSC.PWM(2) = rD;
