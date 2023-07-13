%% Atualiza os valores do padr�o de cores de acordo com os pixels selecionados
Calib.Pixels.RGB(1,1,:) = reshape(uint8(mean(Calib.Pixels.Valores)-std(Calib.Pixels.Valores)),1,1,3);
Calib.Pixels.RGB(1,2,:) = reshape(uint8(mean(Calib.Pixels.Valores)+std(Calib.Pixels.Valores)),1,1,3);

Calib.LimitesHSV(Calib.Imagem.Cor,[1 3 5]) = round(reshape(rgb2hsv(Calib.Pixels.RGB(1,1,:)),1,3).*[360 100 100]);
Calib.LimitesHSV(Calib.Imagem.Cor,[2 4 6]) = round(reshape(rgb2hsv(Calib.Pixels.RGB(1,2,:)),1,3).*[360 100 100]);

for ii = 1:2:6
    if Calib.LimitesHSV(Calib.Imagem.Cor,ii) > Calib.LimitesHSV(Calib.Imagem.Cor,ii+1)
        Calib.LimitesHSV(Calib.Imagem.Cor,[ii ii+1]) = Calib.LimitesHSV(Calib.Imagem.Cor,[ii+1 ii]);
    end
end

% Chama a fun��o para exibir a segmenta��o da cor escolhida
CalibProcessarImagem

% Fecha a figura dos pixels
closereq