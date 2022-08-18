%% Alteração dos valores definidos pelas caixas de texto

% Percorre todas as caixas de texto
for ii = 1:6
    % Verifica se o valor digitado é um número real
    if ~isnan(str2double(Calib.Edit(ii).String)) && isreal(str2double(Calib.Edit(ii).String))
        if mod(ii,2)
            % Verifica se os valores mínimos são menores que 0
            if str2double(Calib.Edit(ii).String) < 0
                Calib.Edit(ii).String = '0';
            end
        else
            if ii < 3
                if str2double(Calib.Edit(ii).String) > 360
                    Calib.Edit(ii).String = '360';
                end
            else
                
                if str2double(Calib.Edit(ii).String) > 100
                    Calib.Edit(ii).String = '100';
                end
            end
        end
    else
        Calib.Edit(ii).String = '0';
    end
end

for ii = 3:2:6
    if str2double(Calib.Edit(ii).String) > str2double(Calib.Edit(ii+1).String)
        Calib.Edit(ii).String = Calib.Edit(ii+1).String;
    end
end

for ii = 1:6
    Calib.LimitesHSV(Calib.Imagem.Cor,ii) = round(str2double(Calib.Edit(ii).String));
end

% Chama a função para exibir a segmentação da cor escolhida
CalibProcessarImagem
