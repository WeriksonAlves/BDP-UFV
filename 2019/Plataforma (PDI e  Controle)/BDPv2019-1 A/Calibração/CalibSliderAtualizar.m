%% Altera��o dos valores definidos pelos sliders
for ii = 1:2:6
    if Calib.Imagem.Cor ~= 1 || ii >= 3
    if Calib.Slider(ii).Value > Calib.Slider(ii+1).Value
        Calib.Slider(ii).Value = Calib.Slider(ii+1).Value;
    end
    end
end

for ii = 1:6
    Calib.LimitesHSV(Calib.Imagem.Cor,ii) = round(Calib.Slider(ii).Value);
end

% Chama a fun��o para exibir a segmenta��o da cor escolhida
CalibProcessarImagem