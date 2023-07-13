function rBDP = ControleBaixoNivel(rBDP)

% Cálculos dos valores de PWN a ser enviado aos robôs
% Definição dos limites
% Velocidade máxima das rodas
Wmax = 2;

% Limites para envia PWM
limPWMp = [22 90];  % Velocidade positiva
limPWMn = [-22 -90]; % Velocidade negativa
%%
% ?????
K2 = [1/2, 1/2; 1/rBDP.pSC.d, -1/rBDP.pSC.d];

%  rBDP.pSC.W = 1/diametro da roda * inv(K2)*rBDP.pSC.U
rBDP.pSC.W = 1/rBDP.pSC.r*(K2\rBDP.pSC.U);
%%
%seguindo https://edisciplinas.usp.br/pluginfile.php/5152060/mod_resource/content/1/PMR3502_Aula3_Modelo_Robos_Rodas_Final.pdf
%pg31  d = distancia entre rodas q é 75mm
% wd = (v + d/2*w)/(2*raio da roda)
% we = (v - d/2*w)/(2*raio da roda)
% rBDP.pSC.W(1) = (10*rBDP.pSC.U(1) + rBDP.pSC.d / 2 * rBDP.pSC.U(2))/(2 * 0.01*rBDP.pSC.r);
% rBDP.pSC.W(2) = (10*rBDP.pSC.U(1) - rBDP.pSC.d / 2 * rBDP.pSC.U(2))/(2 * 0.01*rBDP.pSC.r);
%%
%saturar o se for maior q Wmax
%%
%ta certo saturar o Velocidade linear e angular???????
%%
 for ii = 1:2
%      rBDP.pSC.W(ii)
    if abs(rBDP.pSC.W(ii)) > Wmax
        rBDP.pSC.W(ii) = sign(rBDP.pSC.W(ii))*Wmax;
    end

    if rBDP.pSC.W(ii) > 0
        rBDP.pSC.PWM(ii) =  (limPWMp(2)-limPWMp(1))/Wmax*rBDP.pSC.W(ii) + limPWMp(1);

    else
        rBDP.pSC.PWM(ii) = -(limPWMn(2)-limPWMn(1))/Wmax*rBDP.pSC.W(ii) + limPWMn(1);

    end
 end
 
