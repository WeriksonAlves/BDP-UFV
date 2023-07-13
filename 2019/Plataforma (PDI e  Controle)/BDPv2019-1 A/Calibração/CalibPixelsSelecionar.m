%% Determinação dos pixels a serem utilizados na segmentação

% Desabilita o botão de selecionar pixels
set(Calib.Pixels.Botao(1),'enable','off')

% Salva os valores das cores dos pixels selecionados em RGB
Calib.Pixels.FH.ID = imfreehand;
Calib.Pixels.FH.pos = int16(Calib.Pixels.FH.ID.getPosition);
delete(imfreehand)
Calib.Pixels.FH.RGB = [];
for ii = 1:size(Calib.Pixels.FH.pos,1)
    for jj = 1:3
        Calib.Pixels.FH.RGB(ii,jj) = Calib.Pixels.Atual(Calib.Pixels.FH.pos(ii,1),Calib.Pixels.FH.pos(ii,2),jj);
    end
end
Calib.Pixels.Valores = [Calib.Pixels.Valores; Calib.Pixels.FH.RGB];

% Calib.Pixels.Valores = [Calib.Pixels.Valores;impixel];

% Habilita o botão de selecionar pixels
set(Calib.Pixels.Botao(1),'enable','on')

% Exclui os pixels selecionados fora da imagem
for ii = size(Calib.Pixels.Valores,1):-1:1
    if isnan(Calib.Pixels.Valores(ii,:))
        Calib.Pixels.Valores(ii,:) = [];
    end
end

% Verifica se foi selecionado algum pixel válido
if ~isempty(Calib.Pixels.Valores)
    
    % Habilita o botão de segmentar pixels
    set(Calib.Pixels.Botao(2),'enable','on')
    
end

% Habilita a função de zoom
zoom on
