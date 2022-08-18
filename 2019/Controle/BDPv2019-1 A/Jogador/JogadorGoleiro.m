function rBDP = JogadorGoleiro(rBDP,Bola)
% Controle de posição atacante

% Direcional para a baliza
if rBDP.pLado == 1
    % Direção positiva de X
    Baliza = -700;
else
    % Direção negativa de X
    Baliza =  700;
end

rBDP.pPos.Xd(1:2,1) = [Baliza;Bola.X(2)*0.5];

% if norm(Bola.X'-rBDP.pPos.X(1:2,1)) < 200
%     % Girar para atacar a bola
%     if rBDP.pLado == 1 % -->
%         if Bola.X(2) > rBDP.pPos.X(2)
%             rBDP.pSC.PWM(1) = -100;
%             rBDP.pSC.PWM(2) = +100;
%         else
%             rBDP.pSC.PWM(1) = +100;
%             rBDP.pSC.PWM(2) = -100;
%         end
%     else        
%         if Bola.X(2) > rBDP.pPos.X(2)
%             rBDP.pSC.PWM(1) = +100;
%             rBDP.pSC.PWM(2) = -100;
%         else
%             rBDP.pSC.PWM(1) = -100;
%             rBDP.pSC.PWM(2) = +100;
%         end
%     end
% else
%     rBDP = ControleAltoNivel(rBDP);
%     rBDP = ControleBaixoNivel(rBDP);
% end

end