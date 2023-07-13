
if Partida.cobrarPenalti
    % na cobrança de pênalti, somente envia sinais de controle para o Atacante
    for idx = 1:3
        if ~strcmp(JogBDP(idx).pFuncao,'a')
            JogBDP(idx).pSC.PWM = [0 0]';
        end
    end
end

COM.msg = ['B' 'D' 150+round(JogBDP(1).pSC.PWM') 150+round(JogBDP(2).pSC.PWM'); 150+round(JogBDP(3).pSC.PWM') 'P' 10];

% 
%    COM.msg = ['B' 'D' 150 150 250 250 250 250 'P' 10];
 fwrite(COM.Porta,COM.msg,'char');
% disp(uint8(COM.msg(3:8)));

% edicao hiago
if toc(t_debug) - debugTime > 10 % A cada 10s verifica a perda de pacote
    Loss = char2array(fscanf(COM.Porta, '%c'));
    disp(Loss);
    debugTime = toc(t_debug);
end
